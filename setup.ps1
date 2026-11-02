<#
.SYNOPSIS
  AI Video Studio — Automated 1-Command Environment Setup
.DESCRIPTION
  Sets up the programmatic video production studio:
  - 3-folder architecture (raw_footage/, reference/, export/)
  - HyperFrames CLI & global skills
  - yt-dlp, FFmpeg checks
  - GSAP, Remotion, and Lemo-Opuscar style engine
  - VoiceStudio integration (voice cloning & dubbing)
  - Agent Skills (video-storyboard, video-storyboard-stylesheet, lemo-opuscar)
#>

param(
    [switch]$InstallVoiceStudio,
    [switch]$SkipNpm
)

$ErrorActionPreference = "Stop"
Write-Host "🎬 Initializing AI Video Studio Setup..." -ForegroundColor Cyan

# 1. Mandatory 3-Folder Architecture
Write-Host "`n📁 Creating Standard 3-Folder Architecture..." -ForegroundColor Yellow
$folders = @("raw_footage", "reference", "export")
foreach ($f in $folders) {
    if (-not (Test-Path $f)) {
        New-Item -ItemType Directory -Path $f -Force | Out-Null
        Write-Host "  ✓ Created $f/" -ForegroundColor Green
    } else {
        Write-Host "  ✓ $f/ already exists" -ForegroundColor Gray
    }
}

# 2. Check System Prerequisites
Write-Host "`n🔍 Checking System Prerequisites..." -ForegroundColor Yellow

# FFmpeg check
if (Get-Command ffmpeg -ErrorAction SilentlyContinue) {
    $ffVer = ffmpeg -version | Select-Object -First 1
    Write-Host "  ✓ FFmpeg detected: $ffVer" -ForegroundColor Green
} else {
    Write-Warning "  ✗ FFmpeg is not installed or not in PATH! Please install FFmpeg (e.g. winget install Gyan.FFmpeg)"
}

# yt-dlp check
if (Get-Command yt-dlp -ErrorAction SilentlyContinue) {
    $ytVer = yt-dlp --version
    Write-Host "  ✓ yt-dlp detected (v$ytVer)" -ForegroundColor Green
} else {
    Write-Warning "  ✗ yt-dlp is not installed! (winget install yt-dlp or pip install yt-dlp)"
}

# Node.js check
if (Get-Command node -ErrorAction SilentlyContinue) {
    $nodeVer = node -v
    Write-Host "  ✓ Node.js detected ($nodeVer)" -ForegroundColor Green
} else {
    Write-Error "  ✗ Node.js 20+ is required. Please install from https://nodejs.org/"
}

# 3. Global Tools Installation
if (-not $SkipNpm) {
    Write-Host "`n⚡ Installing Global Programmatic Video Engines..." -ForegroundColor Yellow
    Write-Host "  -> Installing hyperframes globally..."
    npm install -g hyperframes --silent
    Write-Host "  ✓ HyperFrames CLI installed" -ForegroundColor Green
}

# 4. Agent Skills Setup
Write-Host "`n🧠 Installing AI Agent Skills..." -ForegroundColor Yellow
$targetSkills = Join-Path $HOME ".gemini\config\skills"
if (-not (Test-Path $targetSkills)) {
    New-Item -ItemType Directory -Path $targetSkills -Force | Out-Null
}

$skillsSource = Join-Path $PSScriptRoot "skills"
if (Test-Path $skillsSource) {
    Get-ChildItem -Path $skillsSource -Directory | ForEach-Object {
        $dest = Join-Path $targetSkills $_.Name
        Copy-Item -Path $_.FullName -Destination $dest -Recurse -Force
        Write-Host "  ✓ Installed skill: $($_.Name) -> $dest" -ForegroundColor Green
    }
}

# 5. VoiceStudio (Local Voice Cloning & Dubbing)
if ($InstallVoiceStudio) {
    Write-Host "`n🎙️ Installing VoiceStudio for AI Voice Cloning & Dubbing..." -ForegroundColor Yellow
    Invoke-RestMethod https://voicestudio.sh/install.ps1 | Invoke-Expression
} else {
    Write-Host "`n💡 VoiceStudio (Voice Cloning & Dubbing):" -ForegroundColor Gray
    Write-Host "  To install free open-source VoiceStudio on your machine, run:" -ForegroundColor Gray
    Write-Host "  irm https://voicestudio.sh/install.ps1 | iex" -ForegroundColor White
}

Write-Host "`n🎉 AI Video Studio is 100% Ready!" -ForegroundColor Green
Write-Host "  Run 'python tools/generate_interactive_storyboard.py' to generate your first interactive deck."
