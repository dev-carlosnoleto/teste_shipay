#!/bin/bash
set -e

echo "🚀 Iniciando aplicação..."

# Função para aguardar o banco de dados estar pronto
wait_for_db() {
    echo "⏳ Aguardando banco de dados PostgreSQL estar pronto..."
    local max_attempts=30
    local attempt=1
    
    until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" > /dev/null 2>&1; do
        if [ $attempt -ge $max_attempts ]; then
            echo "❌ Erro: Banco de dados não ficou pronto após $max_attempts tentativas"
            exit 1
        fi
        echo "   Tentativa $attempt/$max_attempts - Banco de dados não está pronto ainda. Aguardando..."
        sleep 2
        attempt=$((attempt + 1))
    done
    echo "✅ Banco de dados está pronto!"
}

# Função para executar migrations
run_migrations() {
    echo "📦 Executando migrations automaticamente..."
    if alembic upgrade head; then
        echo "✅ Migrations aplicadas com sucesso!"
    else
        echo "❌ Erro ao executar migrations"
        exit 1
    fi
}

# Aguardar banco de dados estar pronto
wait_for_db

# Executar migrations automaticamente
run_migrations

# Iniciar aplicação
echo "🌐 Iniciando servidor FastAPI..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

