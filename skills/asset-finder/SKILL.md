---
name: asset-finder
description: Asset vetting, commercial licensing verification, and attribution manifest logger.
---

# asset-finder

Use this skill whenever verifying, searching for, or approving stock footage, audio tracks, sound effects, fonts, and graphics for production.

## 1. Source Restrictions
- Consult ONLY approved directories in `assets/SOURCES.md` and `assets/AUDIO_SOURCES.md`.
- Never scrape, auto-download, or accept files from unknown repositories, pirated packs, or ambiguous licenses.

## 2. Rejection Criteria
Immediately REJECT and quarantine any asset carrying:
- `NonCommercial` (`NC`) tags.
- `NoDerivatives` (`ND`) tags.
- Editorial-Only clauses.
- Paid subscriptions, accounts, or trial-only terms.
- Vague or missing license documentation.

## 3. Manifest Logging Workflow
For every accepted asset:
1. Ensure the user places the file in `assets/audio-inbox/` or relevant asset folder.
2. Verify licensing terms allow commercial monetization on YouTube/Instagram.
3. Record full metadata in `assets/ASSETS.md` and `assets/AUDIO_LICENSES.csv`.
4. If attribution is mandatory, formulate the exact credit string for on-screen display or video description inclusion.
