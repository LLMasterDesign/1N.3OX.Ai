"""
Unit tests for PerformanceTracker
"""

import pytest
from datetime import datetime
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from monitors.performance_tracker import PerformanceTracker


class TestPerformanceTracker:
    """Test suite for PerformanceTracker class"""
    
    def test_initialization(self):
        """Test tracker initialization"""
        tracker = PerformanceTracker(window_size=50, enable_prometheus=False)
        
        assert tracker.window_size == 50
        assert tracker.enable_prometheus is False
        assert len(tracker.metrics_history) == 0
    
    def test_record_check(self):
        """Test recording a check result"""
        tracker = PerformanceTracker(enable_prometheus=False)
        
        result = {
            'url': 'https://example.com',
            'success': True,
            'status_code': 200,
            'response_time': 150,
            'timestamp': datetime.now().isoformat()
        }
        
        tracker.record_check(result)
        
        assert 'https://example.com' in tracker.metrics_history
        assert len(tracker.metrics_history['https://example.com']) == 1
    
    def test_get_statistics(self):
        """Test getting statistics"""
        tracker = PerformanceTracker(enable_prometheus=False)
        
        # Record multiple checks
        for i in range(10):
            result = {
                'url': 'https://example.com',
                'success': True,
                'status_code': 200,
                'response_time': 100 + i * 10,
                'timestamp': datetime.now().isoformat()
            }
            tracker.record_check(result)
        
        stats = tracker.get_statistics('https://example.com')
        
        assert stats is not None
        assert stats['total_checks'] == 10
        assert stats['successful_checks'] == 10
        assert stats['availability_percent'] == 100.0
        assert stats['avg_response_time'] > 0
        assert stats['min_response_time'] == 100
        assert stats['max_response_time'] == 190
    
    def test_statistics_with_failures(self):
        """Test statistics with failed checks"""
        tracker = PerformanceTracker(enable_prometheus=False)
        
        # Record successful and failed checks
        for i in range(5):
            result = {
                'url': 'https://example.com',
                'success': True,
                'status_code': 200,
                'response_time': 100,
                'timestamp': datetime.now().isoformat()
            }
            tracker.record_check(result)
        
        for i in range(5):
            result = {
                'url': 'https://example.com',
                'success': False,
                'status_code': None,
                'response_time': None,
                'timestamp': datetime.now().isoformat(),
                'error': 'Timeout'
            }
            tracker.record_check(result)
        
        stats = tracker.get_statistics('https://example.com')
        
        assert stats['total_checks'] == 10
        assert stats['successful_checks'] == 5
        assert stats['availability_percent'] == 50.0
    
    def test_threshold_breach(self):
        """Test threshold breach detection"""
        tracker = PerformanceTracker(enable_prometheus=False)
        
        # Record slow responses
        for i in range(3):
            result = {
                'url': 'https://example.com',
                'success': True,
                'status_code': 200,
                'response_time': 1000,  # Slow
                'timestamp': datetime.now().isoformat()
            }
            tracker.record_check(result)
        
        breached = tracker.check_threshold_breach('https://example.com', threshold=500)
        assert breached is True
    
    def test_no_threshold_breach(self):
        """Test no threshold breach"""
        tracker = PerformanceTracker(enable_prometheus=False)
        
        # Record fast responses
        for i in range(3):
            result = {
                'url': 'https://example.com',
                'success': True,
                'status_code': 200,
                'response_time': 100,  # Fast
                'timestamp': datetime.now().isoformat()
            }
            tracker.record_check(result)
        
        breached = tracker.check_threshold_breach('https://example.com', threshold=500)
        assert breached is False
    
    def test_get_downtime_events(self):
        """Test getting downtime events"""
        tracker = PerformanceTracker(enable_prometheus=False)
        
        # Record downtime
        for i in range(3):
            result = {
                'url': 'https://example.com',
                'success': False,
                'status_code': None,
                'response_time': None,
                'timestamp': datetime.now().isoformat(),
                'error': 'Connection timeout'
            }
            tracker.record_check(result)
        
        downtime = tracker.get_downtime_events('https://example.com')
        assert len(downtime) == 3
    
    def test_multiple_urls(self):
        """Test tracking multiple URLs"""
        tracker = PerformanceTracker(enable_prometheus=False)
        
        urls = ['https://example1.com', 'https://example2.com', 'https://example3.com']
        
        for url in urls:
            result = {
                'url': url,
                'success': True,
                'status_code': 200,
                'response_time': 100,
                'timestamp': datetime.now().isoformat()
            }
            tracker.record_check(result)
        
        all_stats = tracker.get_all_statistics()
        assert len(all_stats) == 3
    
    def test_window_size_limit(self):
        """Test that history respects window size"""
        tracker = PerformanceTracker(window_size=5, enable_prometheus=False)
        
        # Record more than window size
        for i in range(10):
            result = {
                'url': 'https://example.com',
                'success': True,
                'status_code': 200,
                'response_time': 100,
                'timestamp': datetime.now().isoformat()
            }
            tracker.record_check(result)
        
        # Should only keep last 5
        assert len(tracker.metrics_history['https://example.com']) == 5
    
    def test_clear_history(self):
        """Test clearing history"""
        tracker = PerformanceTracker(enable_prometheus=False)
        
        result = {
            'url': 'https://example.com',
            'success': True,
            'status_code': 200,
            'response_time': 100,
            'timestamp': datetime.now().isoformat()
        }
        tracker.record_check(result)
        
        tracker.clear_history('https://example.com')
        
        assert len(tracker.metrics_history.get('https://example.com', [])) == 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
