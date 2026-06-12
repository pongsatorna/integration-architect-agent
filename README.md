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

### Option 1: Full Suite (Recommended via Antigravity CLI)
To install the entire suite of skills as an Antigravity plugin:
```bash
agy plugin install https://github.com/pongsatorna/integration-architect-agent
```

### Option 2: Individual Skills
Since `gemini skills install` is deprecated, you can manually clone the repository and symlink specific skills to your local workspace's `.agents/skills/` directory:
```bash
git clone https://github.com/pongsatorna/integration-architect-agent.git
mkdir -p .agents/skills
ln -s $(pwd)/integration-architect-agent/skills/integration-architect .agents/skills/
ln -s $(pwd)/integration-architect-agent/skills/discovery-expert .agents/skills/
# etc...
```

## ⚙️ Prerequisites

These skills are **Self-Healing**. The agent will automatically attempt to install the following if missing:
- **Python 3.12+**
- **Libraries:** `pandas`, `mammoth`, `python-docx`

### Figma MCP Setup
To enable high-fidelity UI analysis, you need to configure the **Figma MCP Server**. Since the Antigravity CLI (`agy`) scans the workspace root, this configuration **must** be placed in `.agents/mcp_config.json` at the root of your project (not inside `./discovery/`).

Create the file `.agents/mcp_config.json` in the root of your project:
```json
{
  "mcpServers": {
    "figma": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-figma"
      ],
      "env": {
        "FIGMA_ACCESS_TOKEN": "YOUR_FIGMA_PERSONAL_ACCESS_TOKEN"
      }
    }
  }
}
```
*Note: Replace `YOUR_FIGMA_PERSONAL_ACCESS_TOKEN` with your actual Figma Personal Access Token.*

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
