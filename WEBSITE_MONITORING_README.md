# Website Monitoring Agent 🔍

A production-ready, asynchronous website monitoring solution with real-time alerting, performance tracking, and Prometheus metrics integration.

...loading.{monitoring-agent} ▛▞//▮▮▮▮▮▮▮▹

---

## Features ✨

### Core Monitoring
- **Async Website Checks** - Non-blocking concurrent monitoring of multiple websites
- **Intelligent Retry Logic** - Exponential backoff with configurable retries
- **Performance Metrics** - Response time tracking, availability monitoring
- **Threshold-Based Alerts** - Configurable performance degradation detection

### Alert System
- **Telegram Integration** - Real-time notifications via Telegram bot
- **Smart Alert Cooldown** - Prevents notification spam
- **Severity Levels** - Info, Warning, Critical alert classification
- **State Tracking** - Detects downtime, recovery, and performance issues

### Analytics & Reporting
- **Prometheus Metrics** - Export metrics for Grafana dashboards
- **Statistical Analysis** - Min/max/avg/median response times
- **Availability Tracking** - Historical uptime percentages
- **Downtime Events** - Track and analyze outages

---

## Project Structure

```
/website-monitoring-agent/
├── src/
│   ├── main.py                      # Main orchestrator
│   ├── config.yaml                  # Configuration file
│   ├── monitors/
│   │   ├── website_monitor.py       # Async website checker
│   │   └── performance_tracker.py   # Metrics & statistics
│   ├── integrations/
│   │   ├── telegram_webhook.py      # Telegram bot integration
│   │   └── alert_system.py          # Alert management
│   └── utils/
│       ├── logging.py               # Colored logging setup
│       └── error_handler.py         # Error handling utilities
├── tests/
│   ├── test_website_monitor.py      # Monitor tests
│   ├── test_alert_system.py         # Alert system tests
│   └── test_performance_tracker.py  # Tracker tests
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

---

## Quick Start 🚀

### 1. Installation

```bash
# Install dependencies
pip install -r requirements.txt
```

### 2. Configuration

Edit `src/config.yaml`:

```yaml
website_targets:
  - url: "https://example.com"
    check_interval: 60        # seconds
    timeout: 10               # seconds
    critical_threshold: 500   # ms

alert_settings:
  telegram_token: "YOUR_BOT_TOKEN"    # Get from @BotFather
  chat_id: "YOUR_CHAT_ID"             # Your Telegram chat ID
  
monitoring_config:
  max_retries: 3
  backoff_factor: 2
  enable_prometheus: true
  prometheus_port: 8000
```

### 3. Setup Telegram Bot (Optional but Recommended)

1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Create new bot: `/newbot`
3. Copy the bot token
4. Get your chat ID: Message [@userinfobot](https://t.me/userinfobot)
5. Update `config.yaml` with your credentials

### 4. Run

```bash
cd /workspace
python src/main.py
```

---

## Usage Examples

### Basic Monitoring

```python
from monitors.website_monitor import WebsiteMonitor

async def check_website():
    async with WebsiteMonitor() as monitor:
        result = await monitor.check_website("https://example.com")
        print(f"Status: {result['status_code']}")
        print(f"Response Time: {result['response_time']}ms")
```

### Performance Tracking

```python
from monitors.performance_tracker import PerformanceTracker

tracker = PerformanceTracker(window_size=100, enable_prometheus=False)

# Record check
tracker.record_check(result)

# Get statistics
stats = tracker.get_statistics("https://example.com")
print(f"Availability: {stats['availability_percent']}%")
print(f"Avg Response: {stats['avg_response_time']}ms")
```

### Alert Management

```python
from integrations.alert_system import AlertSystem

alert_system = AlertSystem(telegram_token, chat_id)
await alert_system.initialize()

# Send custom alert
await alert_system.send_alert(
    "Website is slow!",
    severity="warning",
    alert_key="slow_response"
)
```

---

## Configuration Reference

### Website Targets

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `url` | string | required | Website URL to monitor |
| `check_interval` | int | 60 | Seconds between checks |
| `timeout` | int | 10 | Request timeout in seconds |
| `critical_threshold` | int | 500 | Response time alert threshold (ms) |

### Alert Settings

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `telegram_token` | string | required | Telegram bot token |
| `chat_id` | string | required | Telegram chat ID |

### Monitoring Config

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `max_retries` | int | 3 | Maximum retry attempts |
| `backoff_factor` | int | 2 | Exponential backoff multiplier |
| `enable_prometheus` | bool | true | Enable Prometheus metrics |
| `prometheus_port` | int | 8000 | Prometheus HTTP port |

---

## Prometheus Metrics

Access metrics at `http://localhost:8000`

### Available Metrics

- `website_response_time_ms` - Current response time per URL
- `website_status_code_total` - Counter of HTTP status codes
- `website_availability` - Current availability (1=up, 0=down)
- `website_response_time_histogram` - Response time distribution

### Grafana Dashboard

```promql
# Average response time (5m window)
avg_over_time(website_response_time_ms[5m])

# Availability percentage
avg_over_time(website_availability[1h]) * 100

# Request rate
rate(website_status_code_total[5m])
```

---

## Alert Types

### 🚨 Critical: Website Down
Triggered when website is unreachable

```
🚨 Website Down Alert

URL: https://example.com
Status Code: N/A
Error: Connection timeout
Time: 2025-10-22 10:30:45
```

### ⚠️ Warning: Performance Degradation
Triggered when response time exceeds threshold

```
⚠️ Performance Degradation

URL: https://example.com
Response Time: 1250ms
Threshold: 500ms
Status Code: 200
Time: 2025-10-22 10:35:12
```

### ✅ Info: Website Recovery
Triggered when website recovers from downtime

```
✅ Website Recovery

URL: https://example.com
Status Code: 200
Response Time: 180ms
Time: 2025-10-22 10:40:03
```

---

## Testing

### Run All Tests

```bash
cd /workspace
pytest tests/ -v
```

### Run Specific Tests

```bash
# Test website monitor
pytest tests/test_website_monitor.py -v

# Test alert system
pytest tests/test_alert_system.py -v

# Test performance tracker
pytest tests/test_performance_tracker.py -v
```

### Test Coverage

```bash
pytest --cov=src tests/
```

---

## Architecture

### Component Diagram

```
┌─────────────────────────────────────────────┐
│              MonitoringAgent                │
│         (Main Orchestrator)                 │
└──────────────┬──────────────────────────────┘
               │
       ┌───────┴───────┐
       │               │
       ▼               ▼
┌──────────────┐ ┌─────────────────┐
│ WebsiteMonitor│ │PerformanceTracker│
│ - Async checks│ │ - Statistics    │
│ - Retries     │ │ - Prometheus    │
└──────┬────────┘ └────────┬────────┘
       │                   │
       └───────┬───────────┘
               │
               ▼
       ┌──────────────┐
       │ AlertSystem  │
       │ - Telegram   │
       │ - Cooldown   │
       └──────────────┘
```

### Async Flow

```python
# Concurrent monitoring of multiple websites
async def run():
    tasks = [
        monitor_website("https://site1.com"),
        monitor_website("https://site2.com"),
        monitor_website("https://site3.com"),
    ]
    await asyncio.gather(*tasks)
```

---

## Production Deployment

### Using systemd

Create `/etc/systemd/system/website-monitor.service`:

```ini
[Unit]
Description=Website Monitoring Agent
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/opt/website-monitoring-agent
ExecStart=/usr/bin/python3 src/main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl enable website-monitor
sudo systemctl start website-monitor
sudo systemctl status website-monitor
```

### Using Docker

```dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/
CMD ["python", "src/main.py"]
```

Build and run:

```bash
docker build -t website-monitor .
docker run -d --name monitor \
  -v $(pwd)/src/config.yaml:/app/src/config.yaml \
  -p 8000:8000 \
  website-monitor
```

---

## Advanced Features

### Custom Error Handlers

```python
from utils.error_handler import async_error_handler

@async_error_handler(default_return=None, reraise=False)
async def my_function():
    # Your code here
    pass
```

### Colored Logging

```python
from utils.logging import setup_logging

logger = setup_logging(
    log_level="INFO",
    log_file="/var/log/monitor.log",
    enable_colors=True
)
```

### Retry Logic

```python
from utils.error_handler import RetryHandler

result = await RetryHandler.async_retry(
    my_async_function,
    max_attempts=3,
    backoff_factor=2.0,
    exceptions=(ConnectionError, TimeoutError)
)
```

---

## Troubleshooting

### Issue: Telegram alerts not sending

**Solution:**
1. Verify bot token is correct
2. Ensure bot has been started (send `/start` to your bot)
3. Check chat_id is correct
4. Review logs for Telegram API errors

### Issue: Prometheus metrics not available

**Solution:**
1. Check if port 8000 is already in use
2. Verify `enable_prometheus: true` in config
3. Check firewall rules
4. Try accessing `http://localhost:8000/metrics`

### Issue: High memory usage

**Solution:**
1. Reduce `window_size` in PerformanceTracker
2. Decrease check frequency
3. Limit number of monitored websites
4. Review and clear old metrics periodically

---

## Performance Considerations

### Recommended Limits

| Websites | Check Interval | Memory Usage | CPU Usage |
|----------|----------------|--------------|-----------|
| 1-10     | 60s           | ~50MB        | <5%       |
| 10-50    | 60s           | ~200MB       | <15%      |
| 50-100   | 120s          | ~500MB       | <25%      |
| 100+     | 300s          | ~1GB+        | <40%      |

### Optimization Tips

1. **Use longer check intervals** for stable sites
2. **Enable Prometheus** only if using Grafana
3. **Adjust window_size** based on your needs
4. **Use alert cooldowns** to prevent spam
5. **Monitor from multiple locations** for accuracy

---

## Contributing

### Running Tests Before Commit

```bash
# Run linting
flake8 src/ tests/

# Run tests
pytest tests/ -v --cov=src

# Type checking (if using mypy)
mypy src/
```

### Code Style

- Follow PEP 8
- Use type hints
- Write docstrings for all public functions
- Keep functions focused and small
- Add tests for new features

---

## Dependencies

- **aiohttp** - Async HTTP client
- **python-telegram-bot** - Telegram integration
- **prometheus-client** - Metrics export
- **pyyaml** - Configuration parsing
- **pytest** - Testing framework
- **pytest-asyncio** - Async test support

---

## License

MIT License - See LICENSE file for details

---

## Support

- **Issues:** GitHub Issues
- **Documentation:** This README
- **Examples:** See `tests/` directory

---

## Changelog

### v1.0.0 (2025-10-22)
- ✅ Initial release
- ✅ Async website monitoring
- ✅ Telegram alert integration
- ✅ Prometheus metrics
- ✅ Performance tracking
- ✅ Comprehensive test suite

---

▛▞ CURSOR ⫎▸
Built with precision for reliable website monitoring :: ∎
