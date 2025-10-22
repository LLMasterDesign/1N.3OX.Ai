"""
Website Monitor Module
Provides asynchronous website availability and performance monitoring
"""

import asyncio
import aiohttp
import time
from typing import Dict, Optional
from datetime import datetime


class WebsiteMonitor:
    """
    Monitors website availability and performance metrics
    """
    
    def __init__(self, max_retries: int = 3, backoff_factor: int = 2):
        """
        Initialize the website monitor
        
        Args:
            max_retries: Maximum number of retry attempts
            backoff_factor: Exponential backoff multiplier
        """
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.session: Optional[aiohttp.ClientSession] = None
    
    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()
    
    async def check_website(self, url: str, timeout: int = 10) -> Dict:
        """
        Asynchronously check website availability and performance
        
        Args:
            url (str): Target website URL
            timeout (int): Request timeout in seconds
        
        Returns:
            Dict with monitoring metrics including:
                - status_code: HTTP status code
                - response_time: Response time in milliseconds
                - success: Boolean indicating if check was successful
                - timestamp: Check timestamp
                - error: Error message if failed
        """
        start_time = time.time()
        
        for attempt in range(self.max_retries):
            try:
                if not self.session:
                    self.session = aiohttp.ClientSession()
                
                async with self.session.get(
                    url, 
                    timeout=aiohttp.ClientTimeout(total=timeout)
                ) as response:
                    end_time = time.time()
                    response_time = (end_time - start_time) * 1000  # Convert to ms
                    
                    return {
                        "url": url,
                        "status_code": response.status,
                        "response_time": round(response_time, 2),
                        "success": 200 <= response.status < 300,
                        "timestamp": datetime.now().isoformat(),
                        "attempt": attempt + 1,
                        "error": None
                    }
            
            except asyncio.TimeoutError:
                if attempt < self.max_retries - 1:
                    await asyncio.sleep(self.backoff_factor ** attempt)
                    continue
                
                end_time = time.time()
                return {
                    "url": url,
                    "status_code": None,
                    "response_time": round((end_time - start_time) * 1000, 2),
                    "success": False,
                    "timestamp": datetime.now().isoformat(),
                    "attempt": attempt + 1,
                    "error": f"Timeout after {timeout}s"
                }
            
            except aiohttp.ClientError as e:
                if attempt < self.max_retries - 1:
                    await asyncio.sleep(self.backoff_factor ** attempt)
                    continue
                
                end_time = time.time()
                return {
                    "url": url,
                    "status_code": None,
                    "response_time": round((end_time - start_time) * 1000, 2),
                    "success": False,
                    "timestamp": datetime.now().isoformat(),
                    "attempt": attempt + 1,
                    "error": f"Client error: {str(e)}"
                }
            
            except Exception as e:
                if attempt < self.max_retries - 1:
                    await asyncio.sleep(self.backoff_factor ** attempt)
                    continue
                
                end_time = time.time()
                return {
                    "url": url,
                    "status_code": None,
                    "response_time": round((end_time - start_time) * 1000, 2),
                    "success": False,
                    "timestamp": datetime.now().isoformat(),
                    "attempt": attempt + 1,
                    "error": f"Unexpected error: {str(e)}"
                }
        
        # Should not reach here, but return error state
        return {
            "url": url,
            "status_code": None,
            "response_time": None,
            "success": False,
            "timestamp": datetime.now().isoformat(),
            "attempt": self.max_retries,
            "error": "Max retries exceeded"
        }
    
    async def check_multiple_websites(self, urls: list, timeout: int = 10) -> list:
        """
        Check multiple websites concurrently
        
        Args:
            urls: List of URLs to check
            timeout: Request timeout in seconds
        
        Returns:
            List of monitoring results
        """
        tasks = [self.check_website(url, timeout) for url in urls]
        return await asyncio.gather(*tasks)
    
    async def close(self):
        """Close the aiohttp session"""
        if self.session:
            await self.session.close()
