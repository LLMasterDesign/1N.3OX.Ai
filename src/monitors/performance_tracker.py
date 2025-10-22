"""
Performance Tracker Module
Tracks and analyzes website performance metrics over time
"""

from collections import deque
from typing import Dict, List, Optional
from datetime import datetime, timedelta
from prometheus_client import Gauge, Counter, Histogram


class PerformanceTracker:
    """
    Tracks performance metrics and provides statistical analysis
    """
    
    def __init__(self, window_size: int = 100, enable_prometheus: bool = True):
        """
        Initialize the performance tracker
        
        Args:
            window_size: Number of recent measurements to keep
            enable_prometheus: Enable Prometheus metrics export
        """
        self.window_size = window_size
        self.enable_prometheus = enable_prometheus
        self.metrics_history: Dict[str, deque] = {}
        
        # Prometheus metrics
        if self.enable_prometheus:
            self.response_time_gauge = Gauge(
                'website_response_time_ms',
                'Website response time in milliseconds',
                ['url']
            )
            self.status_code_counter = Counter(
                'website_status_code_total',
                'Total count of HTTP status codes',
                ['url', 'status_code']
            )
            self.availability_gauge = Gauge(
                'website_availability',
                'Website availability (1=up, 0=down)',
                ['url']
            )
            self.response_time_histogram = Histogram(
                'website_response_time_histogram',
                'Histogram of website response times',
                ['url'],
                buckets=[50, 100, 200, 500, 1000, 2000, 5000]
            )
    
    def record_check(self, result: Dict):
        """
        Record a website check result
        
        Args:
            result: Check result dictionary from WebsiteMonitor
        """
        url = result.get('url')
        if not url:
            return
        
        # Initialize history for URL if needed
        if url not in self.metrics_history:
            self.metrics_history[url] = deque(maxlen=self.window_size)
        
        # Store the result
        self.metrics_history[url].append(result)
        
        # Update Prometheus metrics
        if self.enable_prometheus:
            if result.get('response_time') is not None:
                self.response_time_gauge.labels(url=url).set(result['response_time'])
                self.response_time_histogram.labels(url=url).observe(result['response_time'])
            
            if result.get('status_code'):
                self.status_code_counter.labels(
                    url=url,
                    status_code=result['status_code']
                ).inc()
            
            self.availability_gauge.labels(url=url).set(
                1 if result.get('success') else 0
            )
    
    def get_statistics(self, url: str) -> Optional[Dict]:
        """
        Get statistical analysis for a URL
        
        Args:
            url: Website URL
        
        Returns:
            Dictionary with statistics or None if no data
        """
        if url not in self.metrics_history or not self.metrics_history[url]:
            return None
        
        history = list(self.metrics_history[url])
        response_times = [
            r['response_time'] for r in history 
            if r.get('response_time') is not None
        ]
        
        if not response_times:
            return {
                'url': url,
                'total_checks': len(history),
                'successful_checks': sum(1 for r in history if r.get('success')),
                'availability_percent': 0,
                'avg_response_time': None,
                'min_response_time': None,
                'max_response_time': None,
                'median_response_time': None
            }
        
        successful_checks = sum(1 for r in history if r.get('success'))
        sorted_times = sorted(response_times)
        median_index = len(sorted_times) // 2
        
        return {
            'url': url,
            'total_checks': len(history),
            'successful_checks': successful_checks,
            'availability_percent': round((successful_checks / len(history)) * 100, 2),
            'avg_response_time': round(sum(response_times) / len(response_times), 2),
            'min_response_time': round(min(response_times), 2),
            'max_response_time': round(max(response_times), 2),
            'median_response_time': round(sorted_times[median_index], 2),
            'last_check': history[-1]['timestamp']
        }
    
    def get_all_statistics(self) -> List[Dict]:
        """
        Get statistics for all monitored URLs
        
        Returns:
            List of statistics dictionaries
        """
        return [
            self.get_statistics(url) 
            for url in self.metrics_history.keys()
        ]
    
    def check_threshold_breach(self, url: str, threshold: float) -> bool:
        """
        Check if recent response times exceed threshold
        
        Args:
            url: Website URL
            threshold: Response time threshold in ms
        
        Returns:
            True if threshold is breached
        """
        if url not in self.metrics_history:
            return False
        
        # Check last 3 measurements
        recent = list(self.metrics_history[url])[-3:]
        breaches = sum(
            1 for r in recent 
            if r.get('response_time') and r['response_time'] > threshold
        )
        
        return breaches >= 2  # Threshold breached if 2 out of 3 checks exceeded
    
    def get_downtime_events(self, url: str, since: Optional[datetime] = None) -> List[Dict]:
        """
        Get downtime events for a URL
        
        Args:
            url: Website URL
            since: Only return events since this datetime
        
        Returns:
            List of downtime event dictionaries
        """
        if url not in self.metrics_history:
            return []
        
        downtime_events = []
        history = list(self.metrics_history[url])
        
        for result in history:
            if not result.get('success'):
                event_time = datetime.fromisoformat(result['timestamp'])
                
                if since and event_time < since:
                    continue
                
                downtime_events.append({
                    'timestamp': result['timestamp'],
                    'error': result.get('error'),
                    'status_code': result.get('status_code')
                })
        
        return downtime_events
    
    def clear_history(self, url: Optional[str] = None):
        """
        Clear history for a specific URL or all URLs
        
        Args:
            url: URL to clear, or None to clear all
        """
        if url:
            if url in self.metrics_history:
                self.metrics_history[url].clear()
        else:
            self.metrics_history.clear()
