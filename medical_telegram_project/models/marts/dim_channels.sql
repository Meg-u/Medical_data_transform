{{ config(materialized='table') }}

SELECT DISTINCT
  channel_id,
  channel_name
FROM
  {{ ref('stg_telegram_messages') }}
