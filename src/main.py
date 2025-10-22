"""
Website Monitoring Agent - Main Entry Point
Orchestrates website monitoring, performance tracking, and alerting
"""

import asyncio
import yaml
import signal
import sys
from pathlib import Path
from typing import Dict, List
from prometheus_client import start_http_server

from monitors.website_monitor import WebsiteMonitor
from monitors.performance_tracker import PerformanceTracker
from integrations.alert_system import AlertSystem
from utils.logging import setup_logging, get_logger
from utils.error_handler import async_error_handler


class MonitoringAgent:
    """
    Main monitoring agent orchestrator
    """
    
    def __init__(self, config_path: str = "src/config.yaml"):
        """
        Initialize the monitoring agent
        
        Args:
            config_path: Path to configuration file
        """
        self.config_path = config_path
        self.config = None
        self.logger = None
        self.monitor = None
        self.tracker = None
        self.alert_system = None
        self.running = False
        self.tasks = []
    
    def load_config(self) -> Dict:
        """
        Load configuration from YAML file
        
        Returns:
            Configuration dictionary
        """
        config_file = Path(self.config_path)
        
        if not config_file.exists():
            raise FileNotFoundError(f"Configuration file not found: {self.config_path}")
        
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
        
        self.logger.info(f"Configuration loaded from {self.config_path}")
        return config
    
    async def initialize(self):
        """Initialize all monitoring components"""
        self.logger.info("Initializing Website Monitoring Agent...")
        
        # Load configuration
        self.config = self.load_config()
        
        # Initialize components
        monitoring_config = self.config.get('monitoring_config', {})
        alert_config = self.config.get('alert_settings', {})
        
        # Website Monitor
        self.monitor = WebsiteMonitor(
            max_retries=monitoring_config.get('max_retries', 3),
            backoff_factor=monitoring_config.get('backoff_factor', 2)
        )
        
        # Performance Tracker
        enable_prometheus = monitoring_config.get('enable_prometheus', True)
        self.tracker = PerformanceTracker(
            window_size=100,
            enable_prometheus=enable_prometheus
        )
        
        # Start Prometheus metrics server
        if enable_prometheus:
            prometheus_port = monitoring_config.get('prometheus_port', 8000)
            try:
                start_http_server(prometheus_port)
                self.logger.info(f"Prometheus metrics server started on port {prometheus_port}")
            except Exception as e:
                self.logger.warning(f"Failed to start Prometheus server: {e}")
        
        # Alert System
        telegram_token = alert_config.get('telegram_token')
        chat_id = alert_config.get('chat_id')
        
        if telegram_token and chat_id and telegram_token != "YOUR_TELEGRAM_TOKEN":
            self.alert_system = AlertSystem(telegram_token, chat_id)
            await self.alert_system.initialize()
            self.logger.info("Alert system initialized")
        else:
            self.logger.warning("Telegram credentials not configured - alerts disabled")
        
        self.logger.info("Initialization complete")
    
    @async_error_handler(default_return=None, reraise=False)
    async def monitor_website(self, target: Dict):
        """
        Monitor a single website continuously
        
        Args:
            target: Website target configuration
        """
        url = target.get('url')
        check_interval = target.get('check_interval', 60)
        timeout = target.get('timeout', 10)
        critical_threshold = target.get('critical_threshold', 500)
        
        self.logger.info(f"Starting monitoring for {url} (interval: {check_interval}s)")
        
        while self.running:
            try:
                # Check website
                result = await self.monitor.check_website(url, timeout)
                
                # Record metrics
                self.tracker.record_check(result)
                
                # Handle alerts
                if self.alert_system:
                    await self.alert_system.handle_website_check(
                        result,
                        critical_threshold
                    )
                
                # Log result
                status = "✓" if result['success'] else "✗"
                response_time = result.get('response_time', 'N/A')
                self.logger.info(
                    f"{status} {url} - Status: {result.get('status_code', 'N/A')} - "
                    f"Time: {response_time}ms"
                )
                
                # Wait for next check
                await asyncio.sleep(check_interval)
            
            except asyncio.CancelledError:
                self.logger.info(f"Monitoring cancelled for {url}")
                break
            
            except Exception as e:
                self.logger.error(f"Error monitoring {url}: {e}", exc_info=True)
                await asyncio.sleep(check_interval)
    
    async def send_periodic_reports(self, interval: int = 3600):
        """
        Send periodic status reports
        
        Args:
            interval: Report interval in seconds (default: 1 hour)
        """
        while self.running:
            try:
                await asyncio.sleep(interval)
                
                if self.alert_system:
                    statistics = self.tracker.get_all_statistics()
                    if statistics:
                        await self.alert_system.send_daily_report(statistics)
                        self.logger.info("Periodic report sent")
            
            except asyncio.CancelledError:
                break
            
            except Exception as e:
                self.logger.error(f"Error sending periodic report: {e}")
    
    async def run(self):
        """Run the monitoring agent"""
        self.running = True
        
        # Initialize components
        await self.initialize()
        
        # Create monitoring tasks for each website
        website_targets = self.config.get('website_targets', [])
        
        for target in website_targets:
            task = asyncio.create_task(self.monitor_website(target))
            self.tasks.append(task)
        
        # Start periodic reporting
        report_task = asyncio.create_task(self.send_periodic_reports(3600))
        self.tasks.append(report_task)
        
        self.logger.info(f"Monitoring {len(website_targets)} websites...")
        
        # Wait for all tasks
        try:
            await asyncio.gather(*self.tasks)
        except asyncio.CancelledError:
            self.logger.info("Monitoring tasks cancelled")
    
    async def shutdown(self):
        """Gracefully shutdown the monitoring agent"""
        self.logger.info("Shutting down monitoring agent...")
        self.running = False
        
        # Cancel all tasks
        for task in self.tasks:
            task.cancel()
        
        # Wait for tasks to complete
        await asyncio.gather(*self.tasks, return_exceptions=True)
        
        # Cleanup components
        if self.monitor:
            await self.monitor.close()
        
        if self.alert_system:
            # Send final report
            statistics = self.tracker.get_all_statistics()
            if statistics:
                await self.alert_system.send_custom_notification(
                    "Monitoring Agent Shutdown",
                    {"status": "Agent stopped", "time": str(asyncio.get_event_loop().time())},
                    severity="info"
                )
            await self.alert_system.close()
        
        self.logger.info("Shutdown complete")


async def main():
    """Main entry point"""
    # Setup logging
    logger = setup_logging(log_level="INFO", enable_colors=True)
    
    # Create agent
    agent = MonitoringAgent()
    
    # Setup signal handlers
    def signal_handler(signum, frame):
        logger.info(f"Received signal {signum}")
        asyncio.create_task(agent.shutdown())
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Run agent
    try:
        await agent.run()
    except KeyboardInterrupt:
        await agent.shutdown()
    except Exception as e:
        logger.critical(f"Fatal error: {e}", exc_info=True)
        await agent.shutdown()
        sys.exit(1)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n Monitoring agent stopped")
