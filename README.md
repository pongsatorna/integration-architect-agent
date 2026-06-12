# Integration Architect Skill Suite 🚀

An autonomous, multi-skill suite for the **Integration Architect** lifecycle. It bridges the gap between legacy technical systems and modern mobile frontend requirements using a **Compute-First, Deterministic** approach.

## 🛠 Skills Included

1. **`integration-architect`**: The Master Orchestrator. Manages the 5-phase lifecycle.
2. **`discovery-expert`**: Technical Source understanding (Word/CSV to OpenAPI/Schema Map).
3. **`ui-analyzer`**: User Target understanding (Figma/Screenshot to UI Spec).
4. **`contract-designer`**: The Bridge (Optimized OpenAPI & TypeScript Types).
5. **`data-aligner`**: Persistence Layer (DB Gap Analysis & SQL Alignment).
6. **`quality-architect`**: Verification Layer (Postman, K6, and Mocks).

## 📦 Installation

### Option 1: Full Suite (Recommended)
To install the entire suite of 6 skills with one command:
```bash
gemini extensions install https://github.com/pongsatorna/integration-architect-agent
```

### Option 2: Individual Skills
To install specific skills using the `skills` command:
```bash
gemini skills install https://github.com/pongsatorna/integration-architect-agent --path skills/integration-architect
gemini skills install https://github.com/pongsatorna/integration-architect-agent --path skills/discovery-expert
# etc...
```

## ⚙️ Prerequisites

These skills are **Self-Healing**. The agent will automatically attempt to install the following if missing:
- **Python 3.12+**
- **Libraries:** `pandas`, `mammoth`, `python-docx`

### Figma MCP Setup
To enable high-fidelity UI analysis, ensure you have the **Figma MCP Server** configured with your `FIGMA_ACCESS_TOKEN`.

## 📂 Workspace Structure

### User-Created Input Folders (Must be set up before running):
- `./discovery/`: Place your legacy API docs (`.docx`) and database schema exports (`.csv`) here.
- `./ui_analysis/screenshots/`: Place UI mockups/screenshots here (if not using the Figma MCP server).

### Agent-Created Output Folders (Created automatically at runtime):
- `./contracts/`: Final OpenAPI specs, TypeScript types, and lineage maps.
- `./database/`: SQL alignment scripts and database migration plans.
- `./testing/`: Postman collections, K6 load test scripts, and mock response JSONs.

---
**Build with ❤️ for Integration Architects.**
