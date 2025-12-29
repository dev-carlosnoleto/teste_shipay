from sqlalchemy import Column, Integer, BigInteger, String, Boolean, Date, ForeignKey, Identity
from sqlalchemy.orm import relationship
from app.config.database import Base

class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, Identity(always=True), primary_key=True)
    description = Column(String, nullable=False)

    users = relationship("User", back_populates="role")


class Claim(Base):
    __tablename__ = "claims"

    id = Column(BigInteger, Identity(always=True), primary_key=True)
    description = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)

    user_claims = relationship("UserClaim", back_populates="claim")


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, Identity(always=True), primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date)

    role = relationship("Role", back_populates="users")
    claims = relationship("UserClaim", back_populates="user")


class UserClaim(Base):
    __tablename__ = "user_claims"
    __table_args__ = (
        {'comment': 'Tabela de relacionamento entre users e claims com constraint UNIQUE'}
    )

    user_id = Column(BigInteger, ForeignKey("users.id"), primary_key=True)
    claim_id = Column(BigInteger, ForeignKey("claims.id"), primary_key=True)

    user = relationship("User", back_populates="claims")
    claim = relationship("Claim", back_populates="user_claims")
