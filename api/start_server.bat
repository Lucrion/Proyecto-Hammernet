@echo off
echo Iniciando servidor API de Hammernet...
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python no está instalado o no está en el PATH.
    echo Por favor, instale Python 3.8 o superior.
    pause
    exit /b 1
)

REM Verificar si las dependencias están instaladas
echo Verificando dependencias...
pip install -r requirements.txt

echo.
echo Iniciando servidor en http://localhost:8000
echo Presione Ctrl+C para detener el servidor
echo.

cd %~dp0
python run.py