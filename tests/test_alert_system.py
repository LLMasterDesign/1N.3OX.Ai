"""
Unit tests for AlertSystem
"""

import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock
from datetime import datetime, timedelta
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from integrations.alert_system import AlertSystem
from integrations.telegram_webhook import TelegramWebhook


@pytest.mark.asyncio
class TestAlertSystem:
    """Test suite for AlertSystem class"""
    
    @pytest.fixture
    def mock_telegram(self):
        """Create a mock TelegramWebhook"""
        with patch('integrations.alert_system.TelegramWebhook') as mock:
            telegram = AsyncMock()
            telegram.initialize = AsyncMock()
            telegram.send_message = AsyncMock(return_value=True)
            telegram.send_formatted_alert = AsyncMock(return_value=True)
            telegram.send_status_report = AsyncMock(return_value=True)
            telegram.close = AsyncMock()
            mock.return_value = telegram
            yield telegram
    
    async def test_initialization(self, mock_telegram):
        """Test alert system initialization"""
        alert_system = AlertSystem("test_token", "test_chat_id")
        await alert_system.initialize()
        
        assert alert_system.telegram is not None
        mock_telegram.initialize.assert_called_once()
    
    async def test_send_alert(self, mock_telegram):
        """Test sending a basic alert"""
        alert_system = AlertSystem("test_token", "test_chat_id")
        await alert_system.initialize()
        
        success = await alert_system.send_alert(
            "Test alert message",
            severity="warning",
            alert_key="test_alert"
        )
        
        assert success is True
        mock_telegram.send_message.assert_called_once()
    
    async def test_alert_cooldown(self, mock_telegram):
        """Test alert cooldown mechanism"""
        alert_system = AlertSystem("test_token", "test_chat_id")
        await alert_system.initialize()
        
        # Send first alert
        await alert_system.send_alert("Test", alert_key="cooldown_test")
        
        # Immediately send second alert with same key
        success = await alert_system.send_alert("Test", alert_key="cooldown_test")
        
        # Second alert should be suppressed
        assert success is False
    
    async def test_website_down_alert(self, mock_telegram):
        """Test website down alert"""
        alert_system = AlertSystem("test_token", "test_chat_id")
        await alert_system.initialize()
        
        result = {
            'url': 'https://example.com',
            'success': False,
            'status_code': None,
            'error': 'Connection timeout',
            'timestamp': datetime.now().isoformat(),
            'response_time': None
        }
        
        await alert_system.handle_website_check(result, critical_threshold=500)
        
        # Should send critical alert
        mock_telegram.send_message.assert_called()
        call_args = mock_telegram.send_message.call_args
        assert 'Website Down' in call_args[0][0] or 'Down' in str(call_args)
    
    async def test_website_recovery_alert(self, mock_telegram):
        """Test website recovery alert"""
        alert_system = AlertSystem("test_token", "test_chat_id")
        await alert_system.initialize()
        
        # First: website down
        down_result = {
            'url': 'https://example.com',
            'success': False,
            'status_code': None,
            'error': 'Connection timeout',
            'timestamp': datetime.now().isoformat(),
            'response_time': None
        }
        
        await alert_system.handle_website_check(down_result, critical_threshold=500)
        
        # Then: website up
        up_result = {
            'url': 'https://example.com',
            'success': True,
            'status_code': 200,
            'error': None,
            'timestamp': datetime.now().isoformat(),
            'response_time': 150
        }
        
        await alert_system.handle_website_check(up_result, critical_threshold=500)
        
        # Should send recovery alert
        assert mock_telegram.send_message.call_count >= 2
    
    async def test_performance_degradation_alert(self, mock_telegram):
        """Test performance degradation alert"""
        alert_system = AlertSystem("test_token", "test_chat_id")
        await alert_system.initialize()
        
        result = {
            'url': 'https://example.com',
            'success': True,
            'status_code': 200,
            'error': None,
            'timestamp': datetime.now().isoformat(),
            'response_time': 1000  # Above threshold
        }
        
        await alert_system.handle_website_check(result, critical_threshold=500)
        
        # Should send warning alert
        mock_telegram.send_message.assert_called()
    
    async def test_daily_report(self, mock_telegram):
        """Test sending daily report"""
        alert_system = AlertSystem("test_token", "test_chat_id")
        await alert_system.initialize()
        
        statistics = [
            {
                'url': 'https://example.com',
                'availability_percent': 99.5,
                'avg_response_time': 150,
                'total_checks': 1000
            }
        ]
        
        await alert_system.send_daily_report(statistics)
        
        mock_telegram.send_status_report.assert_called_once_with(statistics)
    
    async def test_custom_notification(self, mock_telegram):
        """Test custom notification"""
        alert_system = AlertSystem("test_token", "test_chat_id")
        await alert_system.initialize()
        
        await alert_system.send_custom_notification(
            "Custom Title",
            {"key1": "value1", "key2": "value2"},
            severity="info"
        )
        
        mock_telegram.send_formatted_alert.assert_called_once()
    
    async def test_close(self, mock_telegram):
        """Test cleanup"""
        alert_system = AlertSystem("test_token", "test_chat_id")
        await alert_system.initialize()
        await alert_system.close()
        
        mock_telegram.close.assert_called_once()


@pytest.mark.asyncio
class TestAlertSystemStatTracking:
    """Test alert system state tracking"""
    
    @pytest.fixture
    def mock_telegram(self):
        """Create a mock TelegramWebhook"""
        with patch('integrations.alert_system.TelegramWebhook') as mock:
            telegram = AsyncMock()
            telegram.initialize = AsyncMock()
            telegram.send_message = AsyncMock(return_value=True)
            mock.return_value = telegram
            yield telegram
    
    async def test_state_tracking(self, mock_telegram):
        """Test website state tracking"""
        alert_system = AlertSystem("test_token", "test_chat_id")
        await alert_system.initialize()
        
        # Initial check - up
        result = {
            'url': 'https://example.com',
            'success': True,
            'status_code': 200,
            'timestamp': datetime.now().isoformat(),
            'response_time': 100
        }
        
        await alert_system.handle_website_check(result, critical_threshold=500)
        assert alert_system.website_states.get('https://example.com') == 'up'


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
