import sqlalchemy as db
from extension_db import Base, ModelMixin


class Account(Base, ModelMixin):
    __tablename__ = "accounts"
    __table_args__ = (db.PrimaryKeyConstraint("id", name="account_pkey"), db.Index("account_email_idx", "email"))

    id = db.Column(db.UUID, server_default=db.text("uuid_generate_v4()"))
    name = db.Column(db.String(255), nullable=False)
    nickname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    real_email = db.Column(db.String(255), nullable=True)  # 新增real_email
    password = db.Column(db.String(255), nullable=True)
    password_salt = db.Column(db.String(255), nullable=True)
    avatar = db.Column(db.String(255))
    interface_language = db.Column(db.String(255))
    interface_theme = db.Column(db.String(255))
    timezone = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(255))
    last_active_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))
    status = db.Column(db.String(16), nullable=False, server_default=db.text("'active'::character varying"))
    initialized_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))
    updated_at = db.Column(db.DateTime, nullable=False, server_default=db.text("CURRENT_TIMESTAMP(0)"))