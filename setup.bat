@echo off
:: Configura o terminal para UTF-8
chcp 65001 >nul

echo Verificando se o Python esta instalado...
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado. 
    echo Por favor, instale-o em: https://www.python.org/downloads/
    pause
    exit /b 1
)

python --version

echo ------------------------------------------
echo Criando ambiente virtual...
if not exist venv (
    python -m venv venv
)

echo Atualizando o pip e instalando dependencias...
venv\Scripts\python.exe -m pip install --upgrade pip
if exist requirements.txt (
    venv\Scripts\pip install -r requirements.txt
)

:: DETECCAO DE SHELL
if not "%PSModulePath%"=="" (
    echo [PowerShell detectado] Ativando ambiente virtual...
    powershell -NoExit -ExecutionPolicy Bypass -Command "& {.\venv\Scripts\Activate.ps1; python seed.py; Write-Host 'Bem-vindo ao TaskQuest! Pronto para a aventura!' -ForegroundColor Green}"
) else (
    echo [CMD detectado] Ativando ambiente virtual...
    cmd /k "venv\Scripts\activate.bat && python seed.py && echo Bem-vindo ao TaskQuest! Pronto para a aventura!"
)