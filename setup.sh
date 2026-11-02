#!/bin/sh
set -e

echo "🎬 Initializing AI Video Studio Setup (Linux/macOS)..."

# 1. 3-Folder Architecture
mkdir -p raw_footage reference export
echo "✓ Created standard 3-folder architecture (raw_footage/, reference/, export/)"

# 2. Check System Tools
command -v ffmpeg >/dev/null 2>&1 || echo "⚠️  FFmpeg not found. Install via: brew install ffmpeg / sudo apt install ffmpeg"
command -v yt-dlp >/dev/null 2>&1 || echo "⚠️  yt-dlp not found. Install via: pip install yt-dlp / brew install yt-dlp"
command -v node >/dev/null 2>&1 || { echo "✗ Node.js 20+ is required."; exit 1; }

# 3. Global Engines
echo "⚡ Installing HyperFrames..."
npm install -g hyperframes --silent || true

# 4. Agent Skills
SKILLS_DIR="$HOME/.gemini/config/skills"
mkdir -p "$SKILLS_DIR"
if [ -d "skills" ]; then
    cp -r skills/* "$SKILLS_DIR/"
    echo "✓ Copied skills to $SKILLS_DIR"
fi

echo "💡 To install VoiceStudio for local voice cloning & dubbing, run:"
echo "   curl -fsSL https://voicestudio.sh/install | sh"

echo "🎉 AI Video Studio is ready!"
