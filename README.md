# Shipay Backend Challenge - UserAPI

## Sobre

A **Shipay Backend Challenge** é uma API RESTful desenvolvida para gerenciar operações de CRUD para usuários, roles e claims. Esta aplicação demonstra o uso de FastAPI e tecnologias associadas para criar e gerenciar recursos em um banco de dados relacional PostgreSQL.

## 📋 Tecnologias

- **Python 3.11**
- **FastAPI**
- **SQLAlchemy**
- **Alembic**
- **PostgreSQL**
- **Docker** & **Docker Compose**

## 🚀 Instalação Normal

**Clone o repositório**:

```bash
git clone https://github.com/dev-carlosnoleto/teste_shipay.git
cd teste_shipay
```

**Criar ambiente virtual**:

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

**Instalar as dependências do projeto**:

```bash
pip install -r requirements.txt
```

**Configurar o arquivo `.env`**:

Crie um arquivo `.env` na raiz do projeto com as configurações do banco de dados:

```env
DB_USER=postgres
DB_PASSWORD=postgres123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
```

> 💡 Use o arquivo `.env.example` como base (se existir)

**Iniciar o banco de dados PostgreSQL**:

Você pode usar Docker Compose para iniciar apenas o banco de dados:

```bash
docker-compose up -d db
```

Ou instalar PostgreSQL localmente e criar o banco de dados manualmente.

**Depois de configurado seu banco de dados, execute as migrations**:

```bash
# Executar migrations
alembic upgrade head

# Verificar status
alembic current
```

**Rodar o projeto**:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

A API estará disponível em `http://localhost:8000`

## 🐳 Instalação via Docker

**Clone o repositório**:

```bash
git clone https://github.com/dev-carlosnoleto/teste_shipay.git
cd teste_shipay
```

**Iniciar apenas o banco de dados PostgreSQL**:

```bash
docker-compose up -d db
```

**Construir a imagem Docker da aplicação**:

```bash
docker-compose build app
```

**Executar migrations**:

```bash
# Linux/Mac
./run-migrations.sh

# Windows
run-migrations.bat

# Ou manualmente
docker-compose run --rm app alembic upgrade head
```

**Instalar dependências e iniciar aplicação**:

```bash
# Criar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Iniciar aplicação
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

> ⚠️ **Nota**: O Docker Compose apenas inicia o banco de dados. A instalação de dependências e inicialização da aplicação são manuais.

## 🌐 Rotas da API

A documentação interativa da API (Swagger) está disponível em:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Endpoints Disponíveis

#### Usuários

- `POST /users/create` - Criar um novo usuário
- `GET /users/{user_id}` - Buscar usuário por ID

#### Roles

- `GET /role/{role_id}` - Buscar role por ID

### Exemplo de Uso

**Criar usuário**:

```bash
curl -X POST "http://localhost:8000/users/create" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "João Silva",
       "email": "joao@example.com",
       "role_id": 1
     }'
```

**Buscar usuário**:

```bash
curl "http://localhost:8000/users/1"
```

**Buscar role**:

```bash
curl "http://localhost:8000/role/1"
```

## 📁 Estrutura do Projeto

```
teste_shipay/
├── app/
│   ├── controllers/          # Endpoints da API
│   ├── models/               # Modelos do banco de dados
│   ├── schema/               # Schemas Pydantic
│   ├── services/             # Lógica de negócio
│   ├── config/               # Configurações
│   └── main.py              # Ponto de entrada
├── migrations/               # Migrations do Alembic
├── docker-compose.yml        # Configuração Docker
├── Dockerfile               # Imagem Docker
├── requirements.txt         # Dependências
└── README.md               # Este arquivo
```

## 🔧 Comandos Úteis

### Migrations

```bash
# Executar migrations
alembic upgrade head

# Criar nova migration
alembic revision --autogenerate -m "descrição"

# Ver histórico
alembic history

# Reverter migration
alembic downgrade -1
```

### Docker

```bash
# Iniciar banco de dados
docker-compose up -d db

# Parar banco de dados
docker-compose down

# Ver logs do banco
docker-compose logs -f db

# Executar migrations via Docker
docker-compose run --rm app alembic upgrade head
```

## 🗄️ Banco de Dados

O projeto utiliza PostgreSQL com as seguintes tabelas:

- **roles** - Roles de usuários
- **users** - Usuários do sistema
- **claims** - Permissões/claims
- **user_claims** - Relacionamento entre users e claims

As migrations criam o banco de dados de acordo com o SQL fornecido, incluindo Identity columns (GENERATED ALWAYS AS IDENTITY).

## 📝 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DB_USER=postgres
DB_PASSWORD=postgres123
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
```

Para Docker Compose, use `DB_HOST=db` (nome do serviço).

## 🚀 Deploy em Produção

Para instruções detalhadas de deploy em AWS EC2 com Nginx, consulte a seção "Deploy em Produção - AWS EC2 com Nginx" no README completo.

## 📚 Documentação Adicional

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

## 📞 Suporte

Para dúvidas ou problemas, abra uma issue no [repositório GitHub](https://github.com/dev-carlosnoleto/teste_shipay/issues).

## 📄 Licença

Este projeto é um teste técnico desenvolvido para Shipay.
