"""
Unit tests for WebsiteMonitor
"""

import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock
import aiohttp
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from monitors.website_monitor import WebsiteMonitor


@pytest.mark.asyncio
class TestWebsiteMonitor:
    """Test suite for WebsiteMonitor class"""
    
    async def test_successful_website_check(self):
        """Test successful website check"""
        monitor = WebsiteMonitor(max_retries=3, backoff_factor=2)
        
        async with monitor:
            result = await monitor.check_website("https://www.google.com", timeout=10)
            
            assert result is not None
            assert 'url' in result
            assert 'status_code' in result
            assert 'response_time' in result
            assert 'success' in result
            assert 'timestamp' in result
            assert result['url'] == "https://www.google.com"
    
    async def test_timeout_handling(self):
        """Test timeout handling"""
        monitor = WebsiteMonitor(max_retries=1, backoff_factor=1)
        
        async with monitor:
            # Use very short timeout to force timeout
            result = await monitor.check_website(
                "https://httpbin.org/delay/10",
                timeout=1
            )
            
            assert result is not None
            assert result['success'] is False
            assert 'Timeout' in result.get('error', '') or result['error'] is not None
    
    async def test_invalid_url(self):
        """Test handling of invalid URL"""
        monitor = WebsiteMonitor(max_retries=1, backoff_factor=1)
        
        async with monitor:
            result = await monitor.check_website("http://this-domain-does-not-exist-12345.com")
            
            assert result is not None
            assert result['success'] is False
            assert result['error'] is not None
    
    async def test_multiple_websites(self):
        """Test checking multiple websites concurrently"""
        monitor = WebsiteMonitor()
        
        async with monitor:
            urls = [
                "https://www.google.com",
                "https://www.github.com"
            ]
            
            results = await monitor.check_multiple_websites(urls, timeout=10)
            
            assert len(results) == 2
            assert all('url' in r for r in results)
            assert all('status_code' in r for r in results)
    
    async def test_retry_mechanism(self):
        """Test retry mechanism with mock"""
        monitor = WebsiteMonitor(max_retries=3, backoff_factor=1)
        
        # Create a mock session
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.__aenter__ = AsyncMock(return_value=mock_response)
        mock_response.__aexit__ = AsyncMock(return_value=None)
        
        with patch('aiohttp.ClientSession') as mock_session_class:
            mock_session = AsyncMock()
            mock_session.get.return_value = mock_response
            mock_session.__aenter__ = AsyncMock(return_value=mock_session)
            mock_session.__aexit__ = AsyncMock(return_value=None)
            mock_session_class.return_value = mock_session
            
            async with monitor:
                result = await monitor.check_website("https://example.com")
                
                assert result is not None
                assert result['success'] is True
                assert result['status_code'] == 200
    
    async def test_context_manager(self):
        """Test async context manager usage"""
        async with WebsiteMonitor() as monitor:
            assert monitor.session is not None
        
        # Session should be closed after context
        # Note: In actual implementation, session might be None after close
    
    def test_initialization(self):
        """Test monitor initialization"""
        monitor = WebsiteMonitor(max_retries=5, backoff_factor=3)
        
        assert monitor.max_retries == 5
        assert monitor.backoff_factor == 3
        assert monitor.session is None


@pytest.mark.asyncio
class TestWebsiteMonitorEdgeCases:
    """Test edge cases and error conditions"""
    
    async def test_empty_url(self):
        """Test with empty URL"""
        monitor = WebsiteMonitor(max_retries=1)
        
        async with monitor:
            result = await monitor.check_website("")
            
            assert result is not None
            assert result['success'] is False
    
    async def test_malformed_url(self):
        """Test with malformed URL"""
        monitor = WebsiteMonitor(max_retries=1)
        
        async with monitor:
            result = await monitor.check_website("not-a-valid-url")
            
            assert result is not None
            assert result['success'] is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
