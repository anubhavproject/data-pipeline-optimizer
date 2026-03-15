# Data Pipeline Optimizer

This repository showcases the architecture and optimization of data warehousing pipelines that resulted in a **30% reduction in processing time** and enhanced downstream AI analytics.

## 🏗 Architecture
The pipeline follows a modern data stack (MDS) approach:
1.  **Orchestration:** Apache Airflow manages the end-to-end workflow, ensuring high availability and fault tolerance.
2.  **Transformation:** dbt (data build tool) handles the modular T in ELT, implementing incremental materialization for performance.
3.  **Storage:** Snowflake serves as the central data warehouse, optimized for concurrent analytical queries.
4.  **Visualization:** PowerBI consumes processed datasets via DirectQuery for real-time executive dashboards.

## 🚀 Optimization Highlights
- **Incremental Materialization:** Switched from full-refresh to incremental dbt models, reducing Snowflake credit consumption by 25%.
- **Parallel Task Execution:** Optimized Airflow DAG concurrency to handle multiple data streams in parallel.
- **Query Optimization:** Refactored complex SQL joins into optimized dbt models, cutting average dashboard load time by 40%.

## 🛠 File Structure
- dags/snowflake_pipeline.py: Airflow DAG orchestrating the ETL process.
- models/marts/fct_optimized_events.sql: dbt model demonstrating incremental transformation logic.
- i/powerbi_config.json: Conceptual configuration for PowerBI integration.

---
*Developed by Anubhav Ghildiyal.*