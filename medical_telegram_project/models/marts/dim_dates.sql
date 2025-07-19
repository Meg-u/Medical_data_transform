{{ config(materialized='table') }}

SELECT DISTINCT
  message_date::DATE AS date_day
FROM
  {{ ref('stg_telegram_messages') }}
