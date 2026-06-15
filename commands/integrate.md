---
description: Start the Integration Architect lifecycle. Runs the 5-phase deterministic workflow (Discovery → UI Analysis → Contract Design → DB Alignment → Quality).
argument-hint: "[phase] - Optional: start from a specific phase (discovery, ui, contract, db, quality)"
---

Run the **Integration Architect** orchestrator to execute the full integration lifecycle.

## Instructions

1. Check the workspace for inputs:
   - `./discovery/` for legacy API docs (.docx, .pptx, .xlsx) and DB schemas (.csv)
   - `./ui_analysis/` for Figma data or screenshots

2. If a specific phase is requested via argument, skip to that phase (only if prerequisites exist).

3. Otherwise, delegate to the `integration-architect` agent to run the full 5-phase lifecycle with gate-based progression.

## Phases

| # | Phase | Agent | Input | Output |
|---|-------|-------|-------|--------|
| 1 | Discovery | discovery-expert | ./discovery/ docs | OpenAPI specs, schema_map |
| 2 | UI Analysis | ui-analyzer | Figma/screenshots | ui_requirements_spec.md |
| 3 | Contract | contract-designer | Phase 1+2 outputs | BFF OpenAPI, TS types, lineage |
| 4 | DB Align | data-aligner | Lineage gaps | SQL DDL, migration plans |
| 5 | Quality | quality-architect | Final contract | Postman, K6, mocks |
