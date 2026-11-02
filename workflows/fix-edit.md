# /fix-edit Workflow

**Description**: Targeted iteration workflow for refining an existing render based on director feedback without re-building the entire composition.

---

## Workflow Steps

1. **Intake Director Notes**:
   - Parse specific feedback items (e.g., *"captions too small"*, *"cut earlier at 0:14"*, *"music ducking too quiet"*, *"change accent color to amber"*).
2. **Surgical Parameter Updates**:
   - Avoid rebuilding unrelated scenes.
   - Adjust target Remotion components, CSS values, font sizes, or timeline slice points in `src/Composition.tsx`.
   - Update audio cue sheet or ducking parameters in `src/Composition.tsx` or audio mix scripts.
3. **Targeted Re-render & Verification**:
   - Re-render the composition.
   - Run `/quality-check` on modified frames.
   - Log changes in `out/CHANGELOG.md`.
   - Present side-by-side comparison or updated frame stills to director.
