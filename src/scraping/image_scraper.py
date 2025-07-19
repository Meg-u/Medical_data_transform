import asyncio
import os
import logging
from datetime import datetime

from telethon import TelegramClient #type: ignore
from telethon.tl.types import MessageMediaPhoto #type: ignore
from telethon.errors import FloodWaitError #type: ignore

from src.config import config

logging.basicConfig(
    filename="image_scraping.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

client = TelegramClient(
    'session_name',
    config.TELEGRAM_API_ID,
    config.TELEGRAM_API_HASH
)

CHANNELS = [
    "https://t.me/lobelia4cosmetics",
    "https://t.me/tikvahpharma"
]

MESSAGE_LIMIT = 100  # Use a limit for safety

RAW_IMAGE_DIR = "data/raw/telegram_images"

async def scrape_images(channel_url):
    try:
        await client.start()
        logging.info(f"Image scraping started for: {channel_url}")

        entity = await client.get_entity(channel_url)
        today = datetime.now().strftime("%Y-%m-%d")
        channel_name = entity.username or entity.title.replace(" ", "_")
        output_dir = os.path.join(RAW_IMAGE_DIR, today, channel_name)
        os.makedirs(output_dir, exist_ok=True)

        count = 0
        async for message in client.iter_messages(entity, limit=MESSAGE_LIMIT):
            if isinstance(message.media, MessageMediaPhoto):
                file_name = f"{message.id}.jpg"
                await message.download_media(file=os.path.join(output_dir, file_name))
                logging.info(f"Downloaded image {file_name}")
                count += 1

        print(f"✅ Downloaded {count} images from {channel_url}")
        logging.info(f"Downloaded {count} images from {channel_url}")

    except FloodWaitError as e:
        logging.error(f"Flood wait: Sleeping for {e.seconds} seconds")
    except Exception as e:
        logging.error(f"Error scraping images for {channel_url}: {e}")

async def main():
    for channel in CHANNELS:
        await scrape_images(channel)

if __name__ == "__main__":
    logging.info("Starting image scraping...")
    asyncio.run(main())
