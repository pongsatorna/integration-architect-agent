---
name: ui-analyzer
description: Analyzes mobile UI designs (Figma/Screenshots) to define Target requirements. Extracts data fields, types, and states.
version: 1.0.0
---

# Execution Playbook: UI Analyzer (Compute-First & Gate-Driven)

As the UI Analyzer, your goal is to extract "Data Requirements" from the frontend design and align them with upstream data sources with zero guesswork.

---

## 📋 Phase 2A: Pre-Extraction (The Screen/Source Mapping Gate)

1.  **Connectivity & Ingestion:**
    *   **Pre-flight Check:** Ensure the environment is ready.
    *   Scan the `./ui_analysis/raw_mcp` folder for JSON data or attempt to connect to the **Figma MCP Server** using the provided URL.
    *   If MCP is used, save the raw Node JSON to `./ui_analysis/raw_mcp/figma_raw.json`.
    *   **FALLBACK:** If MCP fails or is unavailable, scan the `./ui_analysis/screenshots` folder for images. Proceed with Vision-based analysis on any files found there.

2.  **Deterministic Hierarchy Extraction:**
    *   Run `python3 ./tools/figma_screen_extractor.py ./ui_analysis/raw_mcp/figma_raw.json ./ui_analysis/screen_sections_map.json`.
    *   This extracts a structured hierarchy of screens, their constituent sections, and UI fields.

3.  **🛑 STOP & GATE (User Alignment):**
    *   **Action**: Report to the user that the screen hierarchy template has been successfully generated at `./ui_analysis/screen_sections_map.json`.
    *   **Requirement**: Ask the user to open `./ui_analysis/screen_sections_map.json` and fill in the `"upstream_source": ""` key for each section.
    *   **Gate Condition**: Do **NOT** proceed to Phase 2B until the user confirms they have mapped the upstream sources and approves resuming the workflow.

---

## 📋 Phase 2B: Full Analysis (Specification Generation)

4.  **Parse Field Metadata:**
    *   Run `python3 ./tools/figma_node_parser.py ./ui_analysis/raw_mcp/figma_raw.json ./ui_analysis/ui_data_map.json`.
    *   Compare the output `./ui_analysis/ui_data_map.json` against the user-populated `./ui_analysis/screen_sections_map.json` to verify component names, text data types, and layouts.

5.  **Semantic & Vision Analysis (Fallback Path):**
    *   If using screenshot mockups instead of Figma MCP, analyze each screen from top-to-bottom.
    *   Identify dynamic fields vs static text, data types, and API trigger buttons.

6.  **State Mapping:**
    *   Consult [ui_state_matrix.md](file:///Users/superneung/Documents/code/agent-creation/integration-architect-agent/skills/ui-analyzer/tools/ui_state_matrix.md) to define:
        *   Error states, empty states, and loading states for each section.

7.  **Output Generation:**
    *   Compile all data into a consolidated `./ui_analysis/ui_requirements_spec.md`.
    *   **CRITICAL REQUIREMENT**: Ensure every UI section and field in the spec is linked back to the declared **upstream data source** defined by the user in Phase 2A.
    *   This specification serves as the formal "Target" input for Phase 3 (Contract Design).
