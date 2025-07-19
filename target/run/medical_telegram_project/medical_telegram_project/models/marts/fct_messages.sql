
  
    

  create  table "medical_project"."staging_marts"."fct_messages__dbt_tmp"
  
  
    as
  
  (
    

SELECT
  message_id,
  channel_id,
  message_date::DATE AS date_day,
  message_length,
  has_photo
FROM
  "medical_project"."staging_staging"."stg_telegram_messages"
  );
  