@echo off
title XONIBOT 2026 - Bot de WhatsApp con DeepSeek
color 0A

:: ============================================================
:: IR AL DIRECTORIO DONDE ESTA EL SCRIPT .BAT
:: ============================================================
cd /d "%~dp0"

:: ============================================================
:: SOLICITAR PERMISOS DE ADMINISTRADOR
:: ============================================================
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Solicitando permisos de administrador...
    echo.
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B
)

:: ============================================================
:: VERIFICAR QUE start.py EXISTE
:: ============================================================
if not exist "%~dp0start.py" (
    echo [ERROR] No se encuentra start.py en esta carpeta
    echo.
    echo Ruta actual: %~dp0
    echo.
    echo Asegurate de que start.py esta en la misma carpeta que este .bat
    echo.
    pause
    exit /B
)

:: ============================================================
:: EJECUTAR start.py CON PERMISOS DE ADMINISTRADOR
:: ============================================================
cls
echo ============================================================
echo           XONIBOT 2026 - Bot de WhatsApp
echo              (Modo Administrador)
echo ============================================================
echo.
echo [OK] Permisos de administrador obtenidos
echo.
echo [INFO] Directorio de trabajo: %~dp0
echo.
echo Iniciando XONIBOT...
echo.
echo [INFO] Bot de WhatsApp con DeepSeek
echo [INFO] Automatiza respuestas con IA
echo [INFO] Contexto de ultimos 3 mensajes
echo [INFO] No responde a sus propios mensajes
echo.
echo REQUISITOS PREVIOS:
echo   1. WhatsApp Web abierto (pestaña 1)
echo   2. DeepSeek abierto (pestaña 2)
echo   3. Terminal (pestaña 3)
echo.
echo CONTROLES:
echo   Ctrl+C  - Detener el bot
echo.
echo Presiona Ctrl+C para detener
echo ============================================================
echo.

python start.py

pause
