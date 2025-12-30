from sqlalchemy import create_engine, Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session


DATABASE_URL = "postgresql://postgres:postgres123@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)

Base = declarative_base()


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    users = relationship("User", back_populates="role")

class Claim(Base):
    __tablename__ = "claims"
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    active = Column(Boolean, nullable=False, default=True)
    user_claims = relationship("UserClaim", back_populates="claim")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    created_at = Column(Date, nullable=False)
    updated_at = Column(Date)

    role = relationship("Role", back_populates="users")
    claims = relationship("UserClaim", back_populates="user")

class UserClaim(Base):
    __tablename__ = "user_claims"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    claim_id = Column(Integer, ForeignKey("claims.id"), primary_key=True)

    user = relationship("User", back_populates="claims")
    claim = relationship("Claim", back_populates="user_claims")


def fetch_users_with_roles_and_claims():
    session = Session(engine)

    users = session.query(User).order_by(User.name).all()

    
    result_json = []
    for u in users:
        user_dict = {
            "name": u.name,
            "email": u.email,
            "role": u.role.description if u.role else None,
            "claims": [uc.claim.description for uc in u.claims]
        }
        result_json.append(user_dict)

    session.close()
    return result_json


if __name__ == "__main__":
    users_json = fetch_users_with_roles_and_claims()
    print(users_json)
