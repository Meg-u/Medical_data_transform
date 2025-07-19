

SELECT
  message_id,
  channel_id,
  channel_name,
  message_date,
  message_text,
  has_photo,
  LENGTH(message_text) AS message_length
FROM
  raw.telegram_messages