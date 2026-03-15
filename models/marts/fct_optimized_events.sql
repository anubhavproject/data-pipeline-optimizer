{{ config(materialized='incremental', unique_key='event_id') }}

WITH raw_events AS (
    SELECT * FROM {{ source('telemetry', 'raw_logs') }}
    {% if is_incremental() %}
    WHERE event_timestamp > (SELECT MAX(event_timestamp) FROM {{ this }})
    {% endif %}
),
optimized_features AS (
    SELECT
        event_id,
        user_id,
        event_type,
        event_timestamp,
        -- High-performance feature engineering for AI models
        PARSE_JSON(metadata):latency::float as processing_latency,
        DATEDIFF('second', event_timestamp, CURRENT_TIMESTAMP()) as ingestion_lag
    FROM raw_events
)
SELECT * FROM optimized_features