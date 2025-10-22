# Quick Start Guide 🚀

...loading.{quick-start} ▛▞//▮▮▮▮▮▮▮▮▹

## 5-Minute Setup

### Option 1: Automated Setup (Recommended)

```bash
# Run the setup script
chmod +x setup.sh
./setup.sh

# Edit configuration
nano src/config.yaml

# Run the monitor
./run.sh
```

### Option 2: Manual Setup

```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure
cp src/config.yaml src/config.yaml
# Edit src/config.yaml with your settings

# 4. Run
python src/main.py
```

### Option 3: Docker (Production)

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f website-monitor

# Stop
docker-compose down
```

---

## Get Telegram Credentials (2 minutes)

### Step 1: Create Bot
1. Open Telegram and message [@BotFather](https://t.me/botfather)
2. Send: `/newbot`
3. Follow prompts to name your bot
4. **Copy the token** (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### Step 2: Get Chat ID
1. Message [@userinfobot](https://t.me/userinfobot)
2. **Copy your ID** (looks like: `123456789`)

### Step 3: Start Your Bot
1. Find your bot in Telegram (search for the name you gave it)
2. Send `/start` to activate it

### Step 4: Update Config
```yaml
alert_settings:
  telegram_token: "123456789:ABCdefGHIjklMNOpqrsTUVwxyz"  # Your bot token
  chat_id: "123456789"  # Your chat ID
```

---

## Configure Websites to Monitor

Edit `src/config.yaml`:

```yaml
website_targets:
  - url: "https://yourwebsite.com"
    check_interval: 60      # Check every 60 seconds
    timeout: 10             # 10 second timeout
    critical_threshold: 500 # Alert if > 500ms
    
  - url: "https://api.yoursite.com"
    check_interval: 30      # More frequent checks
    timeout: 5
    critical_threshold: 300
```

---

## Test Installation

```bash
# Validate imports
python3 validate.py

# Run examples (no Telegram needed)
python3 example_usage.py

# Run tests
pytest tests/ -v
```

---

## What You'll Get

### Real-time Alerts

**Website Down:**
```
🚨 Website Down Alert

URL: https://example.com
Status Code: N/A
Error: Connection timeout
Time: 2025-10-22 10:30:45
```

**Performance Issue:**
```
⚠️ Performance Degradation

URL: https://example.com
Response Time: 1250ms
Threshold: 500ms
```

**Recovery:**
```
✅ Website Recovery

URL: https://example.com
Status Code: 200
Response Time: 180ms
```

### Prometheus Metrics

Access at: `http://localhost:8000/metrics`

```
website_response_time_ms{url="https://example.com"} 156.2
website_availability{url="https://example.com"} 1.0
website_status_code_total{url="https://example.com",status_code="200"} 1543
```

### Console Output

```
2025-10-22 10:30:45 | INFO     | Initializing Website Monitoring Agent...
2025-10-22 10:30:45 | INFO     | Configuration loaded from src/config.yaml
2025-10-22 10:30:45 | INFO     | Alert system initialized
2025-10-22 10:30:45 | INFO     | Monitoring 3 websites...
2025-10-22 10:30:46 | INFO     | ✓ https://example.com - Status: 200 - Time: 156ms
```

---

## Troubleshooting

### Dependencies Not Installing?

```bash
# Update pip first
pip install --upgrade pip

# Try with verbose output
pip install -r requirements.txt -v
```

### Port 8000 Already in Use?

Edit `src/config.yaml`:
```yaml
monitoring_config:
  prometheus_port: 8001  # Change to different port
```

### Telegram Not Working?

1. Verify bot token is correct (check for extra spaces)
2. Ensure you sent `/start` to your bot
3. Verify chat ID is correct
4. Check bot token hasn't expired
5. Review logs: `grep -i telegram logs/*.log`

### Import Errors?

```bash
# Ensure you're in the virtual environment
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

---

## Next Steps

### 1. Customize Alerts
Edit `src/integrations/alert_system.py` to customize alert messages and logic.

### 2. Add More Checks
Extend `WebsiteMonitor` to check:
- SSL certificate expiry
- Specific content on pages
- API response validation
- DNS resolution

### 3. Integrate with Grafana
```bash
# Using docker-compose
docker-compose up -d grafana

# Access Grafana at http://localhost:3000
# Username: admin
# Password: admin
```

### 4. Run as Service
See `WEBSITE_MONITORING_README.md` for systemd service setup.

---

## Common Configurations

### High-Frequency Monitoring
```yaml
website_targets:
  - url: "https://critical-api.com"
    check_interval: 10      # Every 10 seconds
    timeout: 3
    critical_threshold: 200
```

### Multiple Environments
```yaml
website_targets:
  - url: "https://prod.example.com"
    check_interval: 60
    
  - url: "https://staging.example.com"
    check_interval: 300     # Less frequent for staging
    
  - url: "https://dev.example.com"
    check_interval: 600     # Even less for dev
```

### API Endpoints
```yaml
website_targets:
  - url: "https://api.example.com/health"
    check_interval: 30
    timeout: 5
    critical_threshold: 500
    
  - url: "https://api.example.com/v2/status"
    check_interval: 30
    timeout: 5
    critical_threshold: 500
```

---

## Resources

- **Full Documentation:** `WEBSITE_MONITORING_README.md`
- **Example Code:** `example_usage.py`
- **Tests:** `tests/` directory
- **Configuration:** `src/config.yaml`

---

▛▞ CURSOR ⫎▸
You're now ready to monitor your websites! :: ∎
