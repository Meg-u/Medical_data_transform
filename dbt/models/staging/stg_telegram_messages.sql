WITH raw AS (
  SELECT
    id,
    message_json ->> 'id' AS message_id,
    message_json ->> 'message' AS message_text,
    message_json ->> 'date' AS message_date,
    (message_json ->> 'media') IS NOT NULL AS has_image,
    source_channel,
    scraped_date
  FROM {{ source('raw', 'telegram_messages') }}
)

SELECT * FROM raw;
