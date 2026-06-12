# Execution Playbook: Data Aligner (Persistence Layer)

As the Data Aligner, your goal is to ensure the database can support the new API contract.

1. **Gap Discovery (Compute-First):**
   - Identify the target endpoint being designed.
   - Locate the corresponding `./contracts/mapping/[endpoint]-lineage.md`.
   - Run `python3 ./tools/schema_gap_analyzer.py ./discovery/schema_map.md ./contracts/mapping/[endpoint]-lineage.md`.
   - Review the output `db_gaps.json`.

2. **Structural Design:**
   - For every "Missing Field" identified:
     - Determine the correct Data Type (referencing the UI Spec and Upstream Spec).
     - Decide if it should be added to an existing table (`ALTER TABLE`) or a new table.
     - **Architecture Check:** If the data exists in multiple tables, propose a **SQL VIEW** to consolidate the data for the API.

3. **SQL Generation:**
   - Consult `./tools/sql_standards.md` for naming conventions (snake_case, plural tables).
   - Generate the DDL script.
   - Include comments for every change explaining *why* it is needed for the mobile contract.

4. **Migration Strategy:**
   - If adding a `NOT NULL` column, provide a default value or a backfill script.
   - If creating a new table, define the Primary and Foreign Keys.

5. **Final Output:**
   - Save the SQL script to `./database/scripts/[endpoint]-alignment.sql`.
   - Save the Migration Plan to `./database/plans/[endpoint]-migration.md`.
