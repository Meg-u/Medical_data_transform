import os
import sys
import json
import logging
from datetime import datetimee
from telethon.tl.types import MessageMediaPhoto #type: ignore

from telethon import TelegramClient  # type: ignore
from telethon.tl.types import MessageMediaPhoto  # type: ignore
from telethon.errors import FloodWaitError  # type: ignore

from src.config import config

logging.basicConfig(
    filename="scraping.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

client = TelegramClient(
    'session_name',
    config.TELEGRAM_API_ID,
    config.TELEGRAM_API_HASH
)

CHANNELS = ["durov","tikvahpharma","lobelia4cosmetics",]
MESSAGE_LIMIT = 100
RAW_DATA_DIR = "data/raw/telegram_messages"
IMAGE_DIR = "data/raw/telegram_images"
async def scrape_channel(channel_url):
    await client.start()
    logging.info(f"Scraping started for: {channel_url}")

    entity = await client.get_entity(channel_url)

    today = datetime.now().strftime("%Y-%m-%d")
    channel_name = entity.username or entity.title.replace(" ", "_")
    output_dir = os.path.join(RAW_DATA_DIR, today)
    os.makedirs(output_dir, exist_ok=True)

    out_file = os.path.join(output_dir, f"{channel_name}.json")
    temp_file = out_file + ".tmp"

    print(f"Writing to: {temp_file}")

    with open(temp_file, "w", encoding="utf-8") as f:
        f.write("[\n")

        count = 0
        async for message in client.iter_messages(entity, limit=MESSAGE_LIMIT):
            try:
                msg_dict = message.to_dict()
                msg_dict['has_photo'] = isinstance(message.media, MessageMediaPhoto)

                json.dump(msg_dict, f, ensure_ascii=False)
                count += 1

                # Add comma only if we expect more
                if count < MESSAGE_LIMIT:
                    f.write(",\n")
                else:
                    f.write("\n")

                f.flush()
                os.fsync(f.fileno())

                print(f"Fetched ID: {message.id}")

            except Exception as e:
                logging.error(f"Error processing message: {e}")

        # Always close with ]
        f.write("]\n")
        f.flush()
        os.fsync(f.fileno())

        # Inside your loop:
        if isinstance(message.media, MessageMediaPhoto):
            today = datetime.now().strftime("%Y-%m-%d")
            channel_name = entity.username or entity.title.replace(" ", "_")
            image_dir = os.path.join(IMAGE_DIR, today, channel_name)
            os.makedirs(image_dir, exist_ok=True)

            file_path = os.path.join(image_dir, f"photo_{message.id}.jpg")

            # Download the photo
            await client.download_media(message, file=file_path)

            msg_dict['photo_file'] = file_path  # add to your JSON
            print(f"Downloaded photo for message ID {message.id} → {file_path}")

    # Atomic rename
    os.replace(temp_file, out_file)

    with open(out_file, "r", encoding="utf-8") as f:
        content = f.read()
        print(f"File starts with: {content[:10]!r}")
        print(f"File ends with: {content[-10:]!r}")

    logging.info(f"Finished writing: {out_file}")

async def main():
    for channel in CHANNELS:
        await scrape_channel(channel)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
