# Push Lunar Landing Navigator to GitHub (PowerShell)
param(
    [string]$RepoUrl = ""
)

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "        PUSH LUNAR LANDING SITE NAVIGATOR TO GITHUB" -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host ""

if ([string]::IsNullOrWhiteSpace($RepoUrl)) {
    $RepoUrl = Read-Host "Enter your GitHub Repository URL (e.g. https://github.com/USER/REPO.git)"
}

if ([string]::IsNullOrWhiteSpace($RepoUrl)) {
    Write-Host "[!] No URL entered. Aborting." -ForegroundColor Red
    return
}

try {
    git --version | Out-Null
} catch {
    Write-Host "[!] Git command line tool not found on PATH." -ForegroundColor Red
    Write-Host "    Download Git for Windows at: https://git-scm.com/download/win" -ForegroundColor Yellow
    Write-Host "    Or run: python push_to_github_api.py" -ForegroundColor Yellow
    return
}

Write-Host "[*] Initializing git..." -ForegroundColor Green
git init
git branch -M main

Write-Host "[*] Staging all files across frontend/, backend/, data/, docs/..." -ForegroundColor Green
git add -A

Write-Host "[*] Committing..." -ForegroundColor Green
git commit -m "feat: complete Lunar Landing Navigator with backend API, calculations engine, and 3D visualizer"

Write-Host "[*] Configuring remote origin..." -ForegroundColor Green
git remote remove origin 2>$null
git remote add origin $RepoUrl

Write-Host "[*] Pushing to main branch on GitHub..." -ForegroundColor Green
git push -u origin main

Write-Host ""
Write-Host "[+] All files successfully pushed to GitHub!" -ForegroundColor Cyan
