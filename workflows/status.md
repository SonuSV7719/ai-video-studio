# /status Workflow

**Description**: Diagnostics and system overview command reporting installed skills, active MCP servers, license compliance tables, library asset counts, and any pending action items.

---

## Workflow Steps

1. **Inventory & Environment Scan**:
   - Check Node, Python, Git, and FFmpeg binaries.
   - List all installed skills across `.agents/skills/`.
   - List active MCP servers configured in `mcp_config.json`.
2. **Library Statistics**:
   - Count video clips, fonts, and graphics in `assets/`.
   - Count music tracks and SFX indexed in `assets/audio-index.json`.
   - Check `assets/audio-inbox/` for unindexed files.
3. **License Health Check**:
   - Verify every indexed asset has commercial rights confirmed.
   - Summarize tool licenses (Remotion, Whisper.cpp, Clipwright, FFmpeg).
4. **Director Report**:
   - Present clean markdown diagnostic dashboard.
   - Highlight any pending items requiring human input or approval.
