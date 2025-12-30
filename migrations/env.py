from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
import sys

# Adiciona o diretório raiz ao path para importar os módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Importa as configurações e modelos
from app.config.database import Base
from app.config.settings import settings
from app.models.models import Role, User, Claim, UserClaim


config = context.config


if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata






def get_url():
# Obtém a URL do banco de dados das configurações
    return settings.DATABASE_URL




