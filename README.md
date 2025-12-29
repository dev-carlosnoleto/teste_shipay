# Shipay Backend Challenge - UserAPI

API REST para gerenciamento de usuários desenvolvida com FastAPI, PostgreSQL e SQLAlchemy.

**Repositório:** [https://github.com/dev-carlosnoleto/teste_shipay](https://github.com/dev-carlosnoleto/teste_shipay)

> **📝 Nota**: Esta aplicação requer inicialização **manual** com Uvicorn. Não há automação de inicialização.

## 🎯 Sobre o Projeto

API REST para consulta e criação de usuários e permissões, gereniciando recursos em um banco de dados relacional.
### Funcionalidades

- ✅ Criação de usuários com geração automática de senha
- ✅ Consulta de usuários por ID
- ✅ Consulta de roles por ID
- ✅ Migrations com Alembic (execução manual)
- ✅ Validação de dados com Pydantic
- ✅ Banco de dados com Identity columns (PostgreSQL)

## 🛠 Tecnologias

- **FastAPI** 0.127.1 - Framework web moderno e rápido
- **PostgreSQL** 15 - Banco de dados relacional
- **SQLAlchemy** 2.0.45 - ORM Python
- **Alembic** 1.13.2 - Gerenciamento de migrations
- **Pydantic** 2.12.5 - Validação de dados
- **Uvicorn** 0.40.0 - Servidor ASGI
- **Docker** & **Docker Compose** - Containerização
- **Nginx** - Proxy reverso 

## 🔧 Requisitos

### Para Docker Compose (Recomendado)

- **Docker** 20.10+
- **Docker Compose** 2.0+
- [Instalar Docker](https://docs.docker.com/get-docker/)

### Para Instalação Local

- **Python** 3.8+ (recomendado 3.11)
- **PostgreSQL** 12+
- **pip** (gerenciador de pacotes Python)

## 🚀 Instalação e Execução Local

### Método 1: Docker Compose (Apenas Banco de Dados)

O Docker Compose apenas inicia o banco de dados PostgreSQL. A instalação de dependências, execução de migrations e inicialização da API são **manuais**.

#### 1. Clonar o Repositório

```bash
git clone https://github.com/dev-carlosnoleto/teste_shipay.git
cd teste_shipay
```

#### 2. Iniciar Banco de Dados

```bash
# Iniciar apenas o banco de dados PostgreSQL
docker-compose up -d db

# Verificar se está rodando
docker-compose ps

# Parar o banco
docker-compose down
```

#### 3. Criar Ambiente Virtual e Instalar Dependências

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

#### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DB_USER=postgres
DB_PASSWORD=postgres123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
```

#### 5. Executar Migrations (Manual)

```bash
# Executar migrations
alembic upgrade head

# Verificar status
alembic current
```

#### 6. Iniciar API Manualmente com Uvicorn

```bash
# Com ambiente virtual ativado
uvicorn app.main:app 
```

A API estará disponível em:

- **API**: http://localhost:8000
- **Documentação Swagger**: http://localhost:8000/docs
- **Documentação ReDoc**: http://localhost:8000/redoc


## 🔐 Variáveis de Ambiente

### Arquivo `.env` (Local)

Crie um arquivo `.env` na raiz do projeto:

```env
DB_USER=postgres
DB_PASSWORD=postgres123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
```

### Docker Compose

As variáveis de ambiente são configuradas diretamente no `docker-compose.yml`. Para produção, use um arquivo `.env` separado ou variáveis de ambiente do sistema.


## 🌐 Deploy em Produção - AWS EC2 com Nginx

### Pré-requisitos

- Conta AWS ativa
- Instância EC2 criada (Ubuntu 22.04 LTS recomendado)
- Acesso SSH à instância EC2
- Domínio configurado

### Passo 1: Configurar Instância EC2

#### 1.1. Conectar via SSH

```bash
ssh -i sua-chave.pem ubuntu@seu-ip-ec2
```

#### 1.2. Atualizar Sistema

```bash
sudo apt update && sudo apt upgrade -y
```

#### 1.3. Instalar Dependências

```bash
# Instalar Docker e Docker Compose
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu

# Instalar Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Instalar Git
sudo apt install git -y

# Instalar Nginx
sudo apt install nginx -y

# Instalar PostgreSQL (se não usar Docker)
sudo apt install postgresql postgresql-contrib -y
```

#### 1.4. Reiniciar Sessão

```bash
# Sair e reconectar para aplicar mudanças do grupo docker
exit
# Reconectar via SSH
```

### Passo 2: Configurar Banco de Dados PostgreSQL



O `docker-compose.yml` já está configurado para usar PostgreSQL em container. Não é necessário instalação adicional.


### Passo 3: Deploy da Aplicação

#### 3.1. Clonar Repositório

```bash
cd /opt
sudo git clone https://github.com/dev-carlosnoleto/teste_shipay.git
sudo chown -R ubuntu:ubuntu teste_shipay
cd teste_shipay
```

#### 3.2. Configurar Variáveis de Ambiente

```bash
# Criar arquivo .env para produção
nano .env.production
```

Conteúdo do `.env.production`:

```env
DB_USER=postgres
DB_PASSWORD=senha_segura_producao
DB_HOST=db
DB_PORT=5432
DB_NAME=postgres
```

#### 3.3. Atualizar docker-compose.yml para Produção

Crie um arquivo `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  db:
    image: postgres:15-alpine
    container_name: user_api_db_prod
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: postgres
    volumes:
      - postgres_data_prod:/var/lib/postgresql/data
    restart: unless-stopped
    networks:
      - app_network

  app:
    build: .
    container_name: user_api_app_prod
    ports:
      - "127.0.0.1:8000:8000"  # Apenas localhost (Nginx fará proxy)
    env_file:
      - .env.production
    depends_on:
      db:
        condition: service_healthy
    volumes:
      - .:/app
    restart: unless-stopped
    networks:
      - app_network

volumes:
  postgres_data_prod:

networks:
  app_network:
    driver: bridge
```

#### 3.4. Build e Iniciar Aplicação

```bash
# Build da imagem
docker-compose -f docker-compose.prod.yml build

# Iniciar serviços
docker-compose -f docker-compose.prod.yml up -d

# Verificar logs
docker-compose -f docker-compose.prod.yml logs -f app
```

### Passo 4: Configurar Nginx

#### 4.1. Criar Configuração do Nginx

```bash
sudo nano /etc/nginx/sites-available/user-api
```

Conteúdo da configuração:

```nginx
server {
    listen 80;
    server_name seu-dominio.com www.seu-dominio.com;  # Substitua pelo seu domínio ou IP

    # Logs
    access_log /var/log/nginx/user-api-access.log;
    error_log /var/log/nginx/user-api-error.log;

    # Tamanho máximo de upload
    client_max_body_size 10M;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    # Health check endpoint (opcional)
    location /health {
        proxy_pass http://127.0.0.1:8000/docs;
        access_log off;
    }
}
```

#### 4.2. Ativar Configuração

```bash
# Criar link simbólico
sudo ln -s /etc/nginx/sites-available/user-api /etc/nginx/sites-enabled/

# Remover configuração padrão (opcional)
sudo rm /etc/nginx/sites-enabled/default

# Reiniciar Nginx
sudo systemctl restart nginx
```

