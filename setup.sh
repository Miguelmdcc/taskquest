#!/bin/bash

# Verifica se o script está sendo "sourced" (essencial para o venv ficar ativo)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "⚠️  ATENÇÃO: Para que o ambiente virtual fique ativo no seu terminal,"
    echo "execute o script usando o comando 'source':"
    echo ""
    echo "      source setup.sh"
    echo ""
    exit 1
fi

echo "--- Verificando Python 3 ---"
if ! command -v python &> /dev/null; then
    echo "[ERRO] Python 3 não encontrado. Por favor, instale-o (sudo apt install python)."
    return 1 # Usamos return em vez de exit porque o script é 'sourced'
fi

python --version

echo "--- Criando ambiente virtual ---"
if [ ! -d "venv" ]; then
    python -m venv venv
fi

echo "--- Ativando ambiente virtual ---"

# Verifica se a pasta é Scripts (Windows) ou bin (Linux/Mac)
if [ -d "venv/Scripts" ]; then
    # Se existir Scripts, estamos no Windows
    source venv/Scripts/activate
elif [ -d "venv/bin" ]; then
    # Se existir bin, estamos no Linux/Mac
    source venv/bin/activate
else
    echo "[ERRO] Pasta de ativação do venv não encontrada!"
    return 1
fi

echo "--- Atualizando pip e dependências ---"
# Dentro do venv, 'python' já aponta para o python do venv
python.exe -m pip install --upgrade pip
if [ -f "requirements.txt" ]; then
    python.exe -m pip install -r requirements.txt
else
    echo "[AVISO] requirements.txt não encontrado."
fi

python seed.py

echo ""
echo "✨ Sua aventura está configurada e pronta para ser vivida!"
echo "🛡️  O ambiente virtual (venv) está ATIVO."
echo "🚀 Digite 'python run.py' para iniciar o TaskQuest."
echo ""