"""
Telegram Webhook Integration
Handles Telegram bot communication for alerts and notifications
"""

import asyncio
from typing import Optional
from telegram import Bot
from telegram.error import TelegramError
import logging


class TelegramWebhook:
    """
    Manages Telegram webhook integration for notifications
    """
    
    def __init__(self, token: str, chat_id: str):
        """
        Initialize Telegram webhook
        
        Args:
            token: Telegram bot token
            chat_id: Target chat ID for messages
        """
        self.token = token
        self.chat_id = chat_id
        self.bot: Optional[Bot] = None
        self.logger = logging.getLogger(__name__)
    
    async def initialize(self):
        """Initialize the Telegram bot"""
        try:
            self.bot = Bot(token=self.token)
            # Test the connection
            await self.bot.get_me()
            self.logger.info("Telegram bot initialized successfully")
        except TelegramError as e:
            self.logger.error(f"Failed to initialize Telegram bot: {e}")
            raise
    
    async def send_message(
        self, 
        message: str, 
        parse_mode: str = 'HTML',
        disable_notification: bool = False
    ) -> bool:
        """
        Send a message via Telegram
        
        Args:
            message: Message text to send
            parse_mode: Message parse mode (HTML, Markdown)
            disable_notification: Disable notification sound
        
        Returns:
            True if message sent successfully
        """
        if not self.bot:
            await self.initialize()
        
        try:
            await self.bot.send_message(
                chat_id=self.chat_id,
                text=message,
                parse_mode=parse_mode,
                disable_notification=disable_notification
            )
            self.logger.debug(f"Message sent to Telegram: {message[:50]}...")
            return True
        
        except TelegramError as e:
            self.logger.error(f"Failed to send Telegram message: {e}")
            return False
    
    async def send_formatted_alert(
        self,
        title: str,
        details: dict,
        severity: str = "info"
    ) -> bool:
        """
        Send a formatted alert message
        
        Args:
            title: Alert title
            details: Dictionary of alert details
            severity: Alert severity (info, warning, critical)
        
        Returns:
            True if message sent successfully
        """
        # Emoji mapping for severity
        severity_emoji = {
            "info": "ℹ️",
            "warning": "⚠️",
            "critical": "🚨"
        }
        
        emoji = severity_emoji.get(severity, "📢")
        
        # Format message
        message = f"{emoji} <b>{title}</b>\n\n"
        
        for key, value in details.items():
            formatted_key = key.replace('_', ' ').title()
            message += f"<b>{formatted_key}:</b> {value}\n"
        
        return await self.send_message(
            message,
            disable_notification=(severity == "info")
        )
    
    async def send_status_report(self, statistics: list) -> bool:
        """
        Send a status report with statistics
        
        Args:
            statistics: List of statistics dictionaries
        
        Returns:
            True if message sent successfully
        """
        message = "📊 <b>Website Monitoring Report</b>\n\n"
        
        for stat in statistics:
            url = stat.get('url', 'Unknown')
            availability = stat.get('availability_percent', 0)
            avg_time = stat.get('avg_response_time', 'N/A')
            
            # Status indicator
            if availability >= 99:
                status = "✅"
            elif availability >= 95:
                status = "⚠️"
            else:
                status = "❌"
            
            message += f"{status} <b>{url}</b>\n"
            message += f"   Availability: {availability}%\n"
            message += f"   Avg Response: {avg_time}ms\n"
            message += f"   Checks: {stat.get('total_checks', 0)}\n\n"
        
        return await self.send_message(message)
    
    async def close(self):
        """Close the Telegram bot connection"""
        if self.bot:
            # The python-telegram-bot v20+ handles cleanup automatically
            self.bot = None
