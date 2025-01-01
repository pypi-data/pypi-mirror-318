# -*- coding: UTF-8 -*-
"""
Model definitions based on Flask SQLAlchemy
===========================================
@ Flask SQLAlchemy Compat - Examples

Author
------
Yuchen Jin (cainmagi)
cainmagi@gmail.com

License
-------
MIT License

Description
-----------
The example of using the Flask SQLAlchemy interface. When `Flask-SQLAlchemy` is not
installed but `Flask-SQLAlchemy-Lite` is installed, will use the lite version to
mimic the behaviors of it.
"""

from hashlib import blake2b

from typing import Optional

try:
    from typing import List
except ImportError:
    from builtins import list as List

import sqlalchemy as sa
import sqlalchemy.orm as sa_orm
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property

from flask_login import UserMixin

import flask_sqlalchemy_compat as fsc


class Base(sa_orm.MappedAsDataclass, sa_orm.DeclarativeBase):
    """The base class of all models."""

    # Add the following line to correct the typehint. It is not necessary for run
    # time.
    query = fsc.QueryGetter()


# Get the Flask-SQLAlchemy extension.
db = fsc.get_flask_sqlalchemy(model_class=Base)

PASSWORD_SALT: bytes = (
    "Something random, used for customizing the password hashing.".encode("utf-8")
)


user_roles = db.Table(
    "user_roles",
    sa.Column(
        "user_id", sa.ForeignKey("user.id", ondelete="cascade"), primary_key=True
    ),
    sa.Column(
        "role_id", sa.ForeignKey("role.id", ondelete="cascade"), primary_key=True
    ),
)


class User(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(255))
    password: Mapped[Optional[str]] = mapped_column(
        sa.String(32), default=None, server_default=None
    )

    # Test many-to-many mapping.
    # We have to add a pyright-ignore here because the current Flask-SQLAlchemy 3.1.x
    # version still does not solve the following issue:
    # https://github.com/pallets-eco/flask-sqlalchemy/issues/1318
    roles: sa_orm.Mapped[List["Role"]] = (
        db.relationship(  # pyright: ignore [reportAssignmentType]
            secondary=user_roles, back_populates="users", default_factory=list
        )
    )

    # Test one-to-many mapping.
    entries: Mapped[List["Entry"]] = (
        db.relationship(  # pyright: ignore [reportAssignmentType]
            back_populates="user",
            default_factory=list,
            cascade="all, delete, delete-orphan",
        )
    )

    # Test queriable property.
    @hybrid_property
    def is_admin(self) -> bool:
        """The level of an admin is < 10"""
        return bool(
            db.session.query(sa.literal(True))
            .filter(
                Role.query.join(User, Role.users)
                .where(User.id == self.id, Role.level < 10)
                .exists()
            )
            .scalar()
        )

    @is_admin.inplace.expression
    @classmethod
    def _is_admin(cls) -> sa.ColumnElement[bool]:
        """The level of an admin is < 10"""
        return cls.id.in_(
            db.session.query(cls.id)
            .join(Role, cls.roles)
            .where(Role.level < 10)
            .group_by(cls.id)
        )

    # Test method
    def set_password(self, password: str) -> None:
        """Set the password by the hashed value of the given string."""
        h_blake2b = blake2b(key=PASSWORD_SALT, digest_size=16)
        h_blake2b.update(password.encode("utf-8"))
        self.password = h_blake2b.hexdigest()

    def validate_passowrd(self, password: str) -> bool:
        """Check whether the password is valdiated for this user."""
        h_blake2b = blake2b(key=PASSWORD_SALT, digest_size=16)
        h_blake2b.update(password.encode("utf-8"))
        return self.password == h_blake2b.hexdigest()


class Role(db.Model):
    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    name: Mapped[str] = mapped_column()
    level: Mapped[int] = mapped_column(default=100, server_default="100")

    # Test many-to-many mapping.
    users: Mapped[List["User"]] = (
        db.relationship(  # pyright: ignore [reportAssignmentType]
            secondary=user_roles, back_populates="roles", default_factory=list
        )
    )

    # Test queriable property.
    @hybrid_property
    def is_admin(self) -> bool:
        """The level of an admin is < 10"""
        return self.level < 10

    @is_admin.inplace.expression
    @classmethod
    def _is_admin(cls) -> sa.ColumnElement[bool]:
        """The level of an admin is < 10"""
        return Role.level < 10


class Entry(db.Model):
    id: Mapped[int] = mapped_column(init=False, primary_key=True)

    # Test one-to-many mapping.
    user_id: Mapped[int] = mapped_column(
        sa.ForeignKey("user.id", ondelete="cascade"), nullable=False
    )
    user: Mapped[User] = db.relationship(  # pyright: ignore [reportAssignmentType]
        back_populates="entries"
    )

    data: Mapped[str] = mapped_column(sa.Text, default="", deferred=True)
