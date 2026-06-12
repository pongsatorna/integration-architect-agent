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

1. Clone this repository:
   ```bash
   git clone https://github.com/[your-org]/integration-architect-agent.git
   ```
2. Point your Gemini CLI to this directory as an extension.

## ⚙️ Prerequisites

These skills are **Self-Healing**. The agent will automatically attempt to install the following if missing:
- **Python 3.12+**
- **Libraries:** `pandas`, `mammoth`, `python-docx`

### Figma MCP Setup
To enable high-fidelity UI analysis, ensure you have the **Figma MCP Server** configured with your `FIGMA_ACCESS_TOKEN`.

## 📂 Workspace Structure
The skills expect and will create the following folders in your project:
- `./discovery/`: Legacy docs and DB exports.
- `./ui_analysis/`: Figma raw data and screenshots.
- `./contracts/`: Final OpenAPI specs and TypeScript types.
- `./database/`: SQL alignment scripts.
- `./testing/`: Postman collections and K6 scripts.

---
**Build with ❤️ for Integration Architects.**
