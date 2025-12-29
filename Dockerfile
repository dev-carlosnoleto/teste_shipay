FROM python:3.11-slim

WORKDIR /app

# Instalar dependências do sistema necessárias para PostgreSQL
RUN apt-get update && apt-get install -y \
    postgresql-client \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar código da aplicação
COPY . .

# Expor porta
EXPOSE 8000

# Comando padrão (pode ser sobrescrito)
# A instalação de requirements e inicialização da app são manuais
CMD ["sleep", "infinity"]

