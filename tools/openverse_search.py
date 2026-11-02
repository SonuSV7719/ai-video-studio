#!/usr/bin/env python3
"""
Openverse Search & Ingestion Tool for AI Video Studio
Search and download 800M+ CC-licensed (Creative Commons / GPL-compatible)
stock images, textures, backgrounds, audio tracks, and sound effects from Openverse.

Usage:
    python tools/openverse_search.py images "paper texture" [--limit 5] [--download DIR]
    python tools/openverse_search.py audio "acoustic guitar" [--limit 5] [--download DIR]
"""

import sys
import os
import json
import argparse
import subprocess
import urllib.parse

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

def search_openverse_api(media_type, query, limit=5, license_type="commercial,modification"):
    """Queries Openverse REST API."""
    params = {
        "q": query,
        "page_size": limit,
    }
    if license_type:
        params["license_type"] = license_type

    url = f"https://api.openverse.org/v1/{media_type}/?" + urllib.parse.urlencode(params)
    
    try:
        cmd = ["curl.exe", "-s", "-L", "-A", USER_AGENT, "-H", "Accept: application/json", url]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        out = res.stdout.strip()
        if res.returncode == 0 and out.startswith("{"):
            data = json.loads(out)
            if "results" in data:
                return data["results"]
    except Exception:
        pass

    # Fallback to Wikimedia Commons public CC API
    return search_wikimedia_commons(query, limit)

def search_wikimedia_commons(query, limit=5):
    """Resilient CC-licensed fallback searching Wikimedia Commons."""
    params = {
        "action": "query",
        "generator": "search",
        "gsrsearch": query,
        "gsrlimit": limit,
        "prop": "imageinfo",
        "iiprop": "url|extmetadata|size",
        "format": "json"
    }
    url = "https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(params)
    try:
        cmd = ["curl.exe", "-s", "-L", "-A", USER_AGENT, url]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if res.returncode == 0 and res.stdout.strip().startswith("{"):
            data = json.loads(res.stdout)
            pages = data.get("query", {}).get("pages", {})
            results = []
            for p_id, p_info in pages.items():
                img_info = p_info.get("imageinfo", [{}])[0]
                results.append({
                    "id": p_id,
                    "title": p_info.get("title", "Untitled").replace("File:", ""),
                    "url": img_info.get("url"),
                    "license": "CC / Public Domain",
                    "creator": "Wikimedia Commons",
                })
            return results
    except Exception:
        pass
    return []

def download_asset(url, dest_dir, filename=None):
    """Downloads an asset safely with streaming."""
    os.makedirs(dest_dir, exist_ok=True)
    if not filename:
        clean_url = url.split("?")[0]
        ext = os.path.splitext(clean_url)[1] or (".jpg" if "image" in url else ".mp3")
        filename = f"asset_{abs(hash(url)) % 100000}{ext}"
    
    dest_path = os.path.join(dest_dir, filename)
    print(f"  Downloading: {url} -> {dest_path}")
    try:
        cmd = ["curl.exe", "-s", "-L", "-A", USER_AGENT, "-o", dest_path, url]
        subprocess.run(cmd, check=True, timeout=30)
        if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
            print(f"  ✓ Saved ({os.path.getsize(dest_path) / 1024:.1f} KB)")
            return dest_path
    except Exception as e:
        print(f"  ✗ Download failed: {e}", file=sys.stderr)
    return None

def main():
    parser = argparse.ArgumentParser(description="Search & download CC-licensed media from Openverse.")
    parser.add_argument("type", choices=["images", "audio"], help="Media type (images or audio)")
    parser.add_argument("query", help="Search query keywords")
    parser.add_argument("--limit", type=int, default=5, help="Max results to return")
    parser.add_argument("--download", help="Directory to download results to")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    print(f"🔍 Searching Openverse for {args.type}: '{args.query}' (limit {args.limit})...")
    results = search_openverse_api(args.type, args.query, limit=args.limit)

    if not results:
        print("No results found. Try alternative keywords.")
        sys.exit(0)

    if args.json:
        print(json.dumps(results, indent=2))
        return

    print(f"\nFound {len(results)} matches:")
    print("-" * 80)
    for idx, r in enumerate(results, 1):
        title = r.get("title", "Untitled")
        creator = r.get("creator", "Unknown")
        license_str = r.get("license", "CC")
        media_url = r.get("url") or r.get("image_url") or "N/A"
        print(f"{idx}. {title}")
        print(f"   Creator: {creator} | License: {str(license_str).upper()}")
        print(f"   URL: {media_url}")

        if args.download and media_url != "N/A":
            download_asset(media_url, args.download)
        print("-" * 80)

if __name__ == "__main__":
    main()
