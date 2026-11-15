r"""
GitHub REST API Direct File Uploader (No git CLI required)
Module: push_to_github_api.py
NASA Space Apps Challenge 2026

Uploads or updates files in a GitHub repository using GitHub's REST API.
Useful when Git CLI is not installed or permissions prevent git installation.
"""

import os
import sys
import json
import base64
import urllib.request
import urllib.error

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_files_to_upload():
    upload_list = []
    # Directories to include
    include_dirs = ["frontend", "backend", "data", "docs"]
    include_files = ["README.md", ".gitignore", "start_navigator.bat", "push_to_github.bat", "push_to_github.ps1"]

    for d in include_dirs:
        dir_path = os.path.join(ROOT_DIR, d)
        if os.path.exists(dir_path):
            for root, _, files in os.walk(dir_path):
                for f in files:
                    if f.endswith(".pyc") or "__pycache__" in root:
                        continue
                    full_p = os.path.join(root, f)
                    rel_p = os.path.relpath(full_p, ROOT_DIR).replace("\\", "/")
                    upload_list.append((rel_p, full_p))

    for f in include_files:
        full_p = os.path.join(ROOT_DIR, f)
        if os.path.exists(full_p):
            upload_list.append((f, full_p))

    return upload_list

def upload_file_to_github(repo, file_path, local_path, token, branch="main"):
    url = f"https://api.github.com/repos/{repo}/contents/{file_path}"
    with open(local_path, "rb") as f:
        content_bytes = f.read()
    content_b64 = base64.b64encode(content_bytes).decode("utf-8")

    # Check if file exists to get SHA for update
    req = urllib.request.Request(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "LunarNavigatorUploader"
    })
    sha = None
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            sha = data.get("sha")
    except urllib.error.HTTPError as e:
        if e.code != 404:
            print(f"[!] Check error for {file_path}: {e}")

    payload = {
        "message": f"feat: sync {file_path}",
        "content": content_b64,
        "branch": branch
    }
    if sha:
        payload["sha"] = sha

    req_put = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "LunarNavigatorUploader"
    }, method="PUT")

    try:
        with urllib.request.urlopen(req_put) as resp:
            return True, resp.status
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        return False, err_msg

def main():
    print("=" * 65)
    print("      LUNAR LANDING NAVIGATOR: DIRECT GITHUB API UPLOADER")
    print("=" * 65)
    print("\nUploads your project files directly to GitHub without needing git installed.")
    print("Example Repo: 'username/lunar-landing-navigator'")

    repo = input("\nEnter GitHub Repo (owner/repo): ").strip()
    if not repo or "/" not in repo:
        print("[!] Invalid repo format. Must be 'owner/repo'.")
        return

    token = input("Enter GitHub Personal Access Token (classic or fine-grained with repo write): ").strip()
    if not token:
        print("[!] Token required for GitHub API upload.")
        return

    files = get_files_to_upload()
    print(f"\n[*] Found {len(files)} files to upload across frontend/, backend/, data/, docs/...\n")

    success_count = 0
    for rel_p, full_p in files:
        print(f" -> Uploading {rel_p} ...", end=" ", flush=True)
        ok, res = upload_file_to_github(repo, rel_p, full_p, token)
        if ok:
            print("[OK]")
            success_count += 1
        else:
            print(f"[FAIL] {res}")

    print(f"\n[+] Upload Complete: {success_count}/{len(files)} files uploaded to https://github.com/{repo}")

if __name__ == "__main__":
    main()
