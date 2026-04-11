e@echo off
:: Configura o terminal para aceitar acentos (UTF-8)
chcp 65001 >nul

echo "Verificando se o Python esta instalado..."
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado. 
    echo Por favor, instale-o em: https://www.python.org/downloads/ e tente novamente.
    pause
    exit /b 1
)

python --version

echo "------------------------------------------"
echo "Criando ambiente virtual..."
if not exist venv (
    python -m venv venv
)

echo "Atualizando o pip e instalando dependencias..."
:: Usamos o caminho direto do python do venv para não depender de ativação agora
venv\Scripts\python.exe -m pip install --upgrade pip
if exist requirements.txt (
    venv\Scripts\pip install -r requirements.txt
)

:: DETECÇÃO DE SHELL: O venv vai ficar ativo agora
:: Se a variável %PSModulePath% existir, você provavelmente está no PowerShell
if not "%PSModulePath%"=="" (
    echo [PowerShell detectado] Ativando ambiente virtual...
    powershell -NoExit -ExecutionPolicy Bypass -Command "& {.\venv\Scripts\Activate.ps1; Write-Host 'Bem-vindo ao TaskQuest! Sua aventura esta configurada e pronta para ser vivida! Vá e comece suas tasks no mundo de TaskQuest!' -ForegroundColor Green}"
) else (
    echo [CMD detectado] Ativando ambiente virtual...
    cmd /k "venv\Scripts\activate.bat && echo Bem-vindo ao TaskQuest! Sua aventura esta configurada e pronta para ser vivida! Vá e comece suas tasks no mundo de TaskQuest!"
)