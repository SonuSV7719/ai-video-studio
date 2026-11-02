import urllib.request
import json
import os

url = "https://api.github.com/repos/Vincentwei1021/mg-styles-15/contents/prompts"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
dest = r"C:\Users\sonup\.gemini\antigravity\scratch\video-studio\reference\repos\mg-styles-15\prompts"
os.makedirs(dest, exist_ok=True)

try:
    with urllib.request.urlopen(req) as resp:
        items = json.loads(resp.read().decode('utf-8'))
        for it in items:
            dl = it.get('download_url')
            name = it.get('name')
            if dl and name:
                dreq = urllib.request.Request(dl, headers={'User-Agent': 'Mozilla/5.0'})
                with urllib.request.urlopen(dreq) as dresp:
                    content = dresp.read()
                    with open(os.path.join(dest, name), 'wb') as f:
                        f.write(content)
                print(f"Downloaded: {name}", flush=True)
    print("ALL 15 PROMPTS DOWNLOADED SUCCESSFULLY!", flush=True)
except Exception as e:
    print(f"Error: {e}", flush=True)
