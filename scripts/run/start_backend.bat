@echo off
echo ===============================
echo   AI Launcher - Backend
echo ===============================

cd /d %~dp0\..\..\backend

python -m uvicorn app.main:app ^
    --host 127.0.0.1 ^
    --port 11451 ^
    --reload

pause
