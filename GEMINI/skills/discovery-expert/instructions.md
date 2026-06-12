# Execution Playbook: Discovery Expert (Compute-First)

As the Discovery Expert, your goal is to create a deterministic "Technical Source of Truth."

1. **Environmental Scan & Self-Healing:**
   - Scan the `./discovery` directory for any `.doc`, `.docx`, or `.csv` files.
   - **Pre-flight Check:** Verify that `pandas`, `mammoth`, and `python-docx` are installed. If any are missing, notify the user and install them using `pip3 install pandas mammoth python-docx`.

2. **Deterministic Extraction (Compute Tools):**
   - **For DB:** Run `python3 ./tools/db_indexer.py ./discovery`. This will automatically generate or update the `schema_map.md`.
   - **For API:** Run `python3 ./tools/doc_converter.py ./discovery`. 
     - If `.docx` files exist, they will be converted to `.md`.
     - If `.doc` files exist, notify the user to save them as `.docx` (or use a system converter if available).

3. **API Modeling (Semantic Layer):**
   - Read the generated `.md` files (the "Clean Source").
   - Follow the `word_to_openapi_rules.md` to map the Markdown content into a valid **OpenAPI 3.0 YAML**.
   - Save to `./discovery/specs/[api-name]-v[version].yaml`.

4. **Validation & Assessment:**
   - Compare the OpenAPI spec against the `./discovery/schema_map.md`.
   - Flag any missing data sources or PII risks discovered by the script.

5. **Final Handover:**
   - Summarize the assets and transition to the `ui-analyzer`.
