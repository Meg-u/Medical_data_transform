{{ config(materialized='table') }}

SELECT
  message_id,
  channel_id,
  message_date::DATE AS date_day,
  message_length,
  has_photo
FROM
  {{ ref('stg_telegram_messages') }}
