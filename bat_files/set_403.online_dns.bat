
@echo off
:: Check for admin privileges
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo Requesting admin privileges...
    powershell start-process '%0' -verb runas
    exit /b
)
py "%~dp0..\dns_scripts\dns_switcher_403.online.py"
pause
    