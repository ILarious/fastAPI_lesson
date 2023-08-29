from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, MetaData, Table, JSON, Boolean

metadata = MetaData()

role = Table(
    "role",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user", String(50), nullable=False),
    Column("permissions", JSON),
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(50), nullable=False, unique=True),
    Column("email", String(320), unique=True, nullable=False),
    Column("role_id", ForeignKey(role.c.id)),
    Column("created_at", TIMESTAMP, default=datetime.utcnow),
    Column('hashed_password', String(length=1024), nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)