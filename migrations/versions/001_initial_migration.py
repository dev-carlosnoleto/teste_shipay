"""initial migration

Revision ID: 001_initial
Revises: 
Create Date: 2025-12-29 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '001_initial'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Criar tabela roles
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), sa.Identity(always=True), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id', name='roles_pk')
    )
    
    # Criar tabela claims
    op.create_table(
        'claims',
        sa.Column('id', sa.BigInteger(), sa.Identity(always=True), nullable=False),
        sa.Column('description', sa.String(), nullable=False),
        sa.Column('active', sa.Boolean(), nullable=False, server_default='true'),
        sa.PrimaryKeyConstraint('id', name='claims_pk')
    )
    
    # Criar tabela users
    op.create_table(
        'users',
        sa.Column('id', sa.BigInteger(), sa.Identity(always=True), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.Date(), nullable=False),
        sa.Column('updated_at', sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint('id', name='users_pk')
    )
    
    # Adicionar foreign key de users para roles
    op.create_foreign_key('users_fk', 'users', 'roles', ['role_id'], ['id'])
    
    # Criar índice único no email
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    
    # Criar tabela user_claims (tabela de relacionamento)
    # Nota: O SQL original tem apenas UNIQUE, mas adicionamos PK composta para SQLAlchemy funcionar
    op.create_table(
        'user_claims',
        sa.Column('user_id', sa.BigInteger(), nullable=False),
        sa.Column('claim_id', sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'claim_id')
    )
    
    # Adicionar foreign keys de user_claims
    op.create_foreign_key('user_claims_fk', 'user_claims', 'users', ['user_id'], ['id'])
    op.create_foreign_key('user_claims_fk_1', 'user_claims', 'claims', ['claim_id'], ['id'])
    
    # Adicionar constraint UNIQUE conforme SQL original
    # (PK composta já garante unicidade, mas mantemos para compatibilidade com SQL)
    op.create_unique_constraint('user_claims_un', 'user_claims', ['user_id', 'claim_id'])


def downgrade() -> None:
    # Remover tabelas na ordem inversa (respeitando foreign keys)
    op.drop_table('user_claims')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('claims')
    op.drop_table('roles')

