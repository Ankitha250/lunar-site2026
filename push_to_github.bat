@echo off
title Push Lunar Landing Navigator to GitHub
echo =================================================================
echo         PUSH LUNAR LANDING SITE NAVIGATOR TO GITHUB
echo =================================================================
echo.

set /p REPO_URL="Enter your GitHub Repository URL (e.g. https://github.com/USER/REPO.git): "

if "%REPO_URL%"=="" (
    echo [!] No URL entered. Aborting.
    pause
    exit /b
)

echo.
echo [*] Initializing Git repository...
git init
git branch -M main

echo [*] Staging all project folders (frontend, backend, data, docs)...
git add frontend backend data docs README.md .gitignore start_navigator.bat push_to_github.bat push_to_github.ps1

echo [*] Committing files...
git commit -m "feat: complete Lunar Landing Navigator platform with backend calculations, frontend 3D UI, and verified NASA datasets"

echo [*] Setting remote origin to %REPO_URL%...
git remote remove origin 2>nul
git remote add origin %REPO_URL%

echo [*] Pushing to main branch...
git push -u origin main

echo.
if %errorlevel% equ 0 (
    echo =================================================================
    echo [+] SUCCESS! All files have been pushed to your GitHub repo!
    echo =================================================================
) else (
    echo [!] Push encountered an issue. If git is not installed, install Git for Windows:
    echo     https://git-scm.com/download/win
    echo     or use the Python API uploader (push_to_github_api.py).
)

pause
