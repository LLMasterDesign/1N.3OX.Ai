#!/usr/bin/env python3
"""
Example usage of the Website Monitoring Agent components
Quick demonstrations of core functionality
"""

import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from monitors.website_monitor import WebsiteMonitor
from monitors.performance_tracker import PerformanceTracker
from utils.logging import setup_logging


async def example_basic_monitoring():
    """Example: Basic website monitoring"""
    print("\n" + "="*60)
    print("Example 1: Basic Website Monitoring")
    print("="*60)
    
    async with WebsiteMonitor() as monitor:
        # Check single website
        result = await monitor.check_website("https://www.google.com", timeout=10)
        
        print(f"\n✓ Website Check Result:")
        print(f"  URL: {result['url']}")
        print(f"  Status Code: {result['status_code']}")
        print(f"  Response Time: {result['response_time']}ms")
        print(f"  Success: {result['success']}")
        print(f"  Timestamp: {result['timestamp']}")


async def example_multiple_websites():
    """Example: Monitor multiple websites concurrently"""
    print("\n" + "="*60)
    print("Example 2: Concurrent Website Monitoring")
    print("="*60)
    
    urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.python.org"
    ]
    
    async with WebsiteMonitor() as monitor:
        results = await monitor.check_multiple_websites(urls, timeout=10)
        
        print(f"\n✓ Checked {len(results)} websites:")
        for result in results:
            status = "✓" if result['success'] else "✗"
            print(f"  {status} {result['url']} - {result['response_time']}ms")


async def example_performance_tracking():
    """Example: Performance tracking and statistics"""
    print("\n" + "="*60)
    print("Example 3: Performance Tracking")
    print("="*60)
    
    tracker = PerformanceTracker(window_size=10, enable_prometheus=False)
    
    # Simulate monitoring over time
    async with WebsiteMonitor() as monitor:
        print("\n✓ Running 5 checks...")
        for i in range(5):
            result = await monitor.check_website("https://www.google.com")
            tracker.record_check(result)
            await asyncio.sleep(0.5)  # Small delay between checks
        
        # Get statistics
        stats = tracker.get_statistics("https://www.google.com")
        
        print(f"\n✓ Statistics:")
        print(f"  Total Checks: {stats['total_checks']}")
        print(f"  Successful: {stats['successful_checks']}")
        print(f"  Availability: {stats['availability_percent']}%")
        print(f"  Avg Response Time: {stats['avg_response_time']}ms")
        print(f"  Min Response Time: {stats['min_response_time']}ms")
        print(f"  Max Response Time: {stats['max_response_time']}ms")


async def example_error_handling():
    """Example: Error handling with invalid URL"""
    print("\n" + "="*60)
    print("Example 4: Error Handling")
    print("="*60)
    
    async with WebsiteMonitor(max_retries=2) as monitor:
        # Try to check an invalid URL
        result = await monitor.check_website("http://this-does-not-exist-12345.com", timeout=5)
        
        print(f"\n✓ Error Handling Result:")
        print(f"  Success: {result['success']}")
        print(f"  Error: {result['error']}")
        print(f"  Attempts: {result['attempt']}")


async def example_threshold_detection():
    """Example: Threshold breach detection"""
    print("\n" + "="*60)
    print("Example 5: Threshold Breach Detection")
    print("="*60)
    
    tracker = PerformanceTracker(enable_prometheus=False)
    
    # Simulate slow responses
    print("\n✓ Simulating slow responses...")
    for i in range(3):
        slow_result = {
            'url': 'https://example.com',
            'success': True,
            'status_code': 200,
            'response_time': 1000 + i * 100,  # Slow responses
            'timestamp': '2025-10-22T10:00:00'
        }
        tracker.record_check(slow_result)
    
    # Check threshold
    threshold = 500  # ms
    breached = tracker.check_threshold_breach('https://example.com', threshold)
    
    print(f"\n✓ Threshold Detection:")
    print(f"  Threshold: {threshold}ms")
    print(f"  Breached: {breached}")
    print(f"  Recent checks exceeded the threshold")


async def main():
    """Run all examples"""
    # Setup logging
    setup_logging(log_level="ERROR", enable_colors=True)
    
    print("\n" + "▛▞" + " "*56 + "▹")
    print("  Website Monitoring Agent - Usage Examples")
    print("▛▞" + " "*56 + "▹")
    
    try:
        await example_basic_monitoring()
        await example_multiple_websites()
        await example_performance_tracking()
        await example_error_handling()
        await example_threshold_detection()
        
        print("\n" + "="*60)
        print("✅ All examples completed successfully!")
        print("="*60)
        print("\nFor full monitoring, run: python src/main.py")
        print(":: ∎\n")
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
