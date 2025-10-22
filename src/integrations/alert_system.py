"""
Alert System Module
Manages alert lifecycle and notification delivery
"""

import asyncio
from typing import Dict, Set, Optional
from datetime import datetime, timedelta
from .telegram_webhook import TelegramWebhook
import logging


class AlertSystem:
    """
    Centralized alert management system
    """
    
    def __init__(self, telegram_token: str, chat_id: str):
        """
        Initialize the alert system
        
        Args:
            telegram_token: Telegram bot token
            chat_id: Telegram chat ID for alerts
        """
        self.telegram = TelegramWebhook(telegram_token, chat_id)
        self.logger = logging.getLogger(__name__)
        
        # Track active alerts to prevent spam
        self.active_alerts: Dict[str, datetime] = {}
        self.alert_cooldown = timedelta(minutes=5)
        
        # Track website states
        self.website_states: Dict[str, str] = {}  # url -> 'up' or 'down'
    
    async def initialize(self):
        """Initialize the alert system"""
        await self.telegram.initialize()
        self.logger.info("Alert system initialized")
    
    def _can_send_alert(self, alert_key: str) -> bool:
        """
        Check if an alert can be sent (respects cooldown)
        
        Args:
            alert_key: Unique key for the alert type
        
        Returns:
            True if alert can be sent
        """
        if alert_key not in self.active_alerts:
            return True
        
        last_alert_time = self.active_alerts[alert_key]
        return datetime.now() - last_alert_time > self.alert_cooldown
    
    def _record_alert(self, alert_key: str):
        """Record that an alert was sent"""
        self.active_alerts[alert_key] = datetime.now()
    
    async def send_alert(
        self,
        message: str,
        severity: str = "warning",
        alert_key: Optional[str] = None
    ) -> bool:
        """
        Send an alert via configured channels
        
        Args:
            message: Alert message
            severity: Severity level (info, warning, critical)
            alert_key: Optional key for alert deduplication
        
        Severity Levels:
            - info: Standard updates
            - warning: Performance degradation
            - critical: Service down
        
        Returns:
            True if alert sent successfully
        """
        # Check cooldown if alert key provided
        if alert_key and not self._can_send_alert(alert_key):
            self.logger.debug(f"Alert {alert_key} suppressed due to cooldown")
            return False
        
        # Send via Telegram
        success = await self.telegram.send_message(
            message,
            disable_notification=(severity == "info")
        )
        
        if success and alert_key:
            self._record_alert(alert_key)
        
        return success
    
    async def handle_website_check(
        self,
        result: Dict,
        critical_threshold: float
    ):
        """
        Process website check result and send appropriate alerts
        
        Args:
            result: Check result from WebsiteMonitor
            critical_threshold: Response time threshold for critical alerts (ms)
        """
        url = result.get('url')
        success = result.get('success', False)
        response_time = result.get('response_time')
        status_code = result.get('status_code')
        error = result.get('error')
        
        previous_state = self.website_states.get(url)
        current_state = 'up' if success else 'down'
        
        # Website down alert
        if not success:
            if previous_state != 'down':
                await self.send_alert(
                    f"🚨 <b>Website Down Alert</b>\n\n"
                    f"<b>URL:</b> {url}\n"
                    f"<b>Status Code:</b> {status_code or 'N/A'}\n"
                    f"<b>Error:</b> {error or 'Unknown'}\n"
                    f"<b>Time:</b> {result.get('timestamp')}",
                    severity="critical",
                    alert_key=f"down_{url}"
                )
                self.logger.warning(f"Website down: {url}")
        
        # Website recovery alert
        elif previous_state == 'down' and current_state == 'up':
            await self.send_alert(
                f"✅ <b>Website Recovery</b>\n\n"
                f"<b>URL:</b> {url}\n"
                f"<b>Status Code:</b> {status_code}\n"
                f"<b>Response Time:</b> {response_time}ms\n"
                f"<b>Time:</b> {result.get('timestamp')}",
                severity="info",
                alert_key=f"recovery_{url}"
            )
            self.logger.info(f"Website recovered: {url}")
        
        # Performance degradation alert
        elif success and response_time and response_time > critical_threshold:
            alert_key = f"slow_{url}_{int(response_time/1000)}"
            await self.send_alert(
                f"⚠️ <b>Performance Degradation</b>\n\n"
                f"<b>URL:</b> {url}\n"
                f"<b>Response Time:</b> {response_time}ms\n"
                f"<b>Threshold:</b> {critical_threshold}ms\n"
                f"<b>Status Code:</b> {status_code}\n"
                f"<b>Time:</b> {result.get('timestamp')}",
                severity="warning",
                alert_key=alert_key
            )
            self.logger.warning(
                f"Slow response from {url}: {response_time}ms"
            )
        
        # Update state
        self.website_states[url] = current_state
    
    async def send_daily_report(self, statistics: list):
        """
        Send daily monitoring report
        
        Args:
            statistics: List of statistics from PerformanceTracker
        """
        success = await self.telegram.send_status_report(statistics)
        
        if success:
            self.logger.info("Daily report sent successfully")
        else:
            self.logger.error("Failed to send daily report")
    
    async def send_custom_notification(
        self,
        title: str,
        details: dict,
        severity: str = "info"
    ):
        """
        Send a custom formatted notification
        
        Args:
            title: Notification title
            details: Dictionary of notification details
            severity: Severity level
        """
        await self.telegram.send_formatted_alert(title, details, severity)
    
    async def close(self):
        """Cleanup resources"""
        await self.telegram.close()
