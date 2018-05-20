import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import UniqueConstraint

import versionalchemy as va
from versionalchemy.models import VAModelMixin, VALogMixin


engine = create_engine('postgresql+psycopg2://postgres:walkiria@localhost:5432/orm3')
Base = declarative_base(bind=engine)

class Example(Base, VAModelMixin):
    __tablename__ = 'example'
    va_version_columns = ['id']
    id = sa.Column(sa.Integer, primary_key=True)
    value = sa.Column(sa.String(128))


class ExampleArchive(Base, VALogMixin):
    __tablename__ = 'example_archive'
    __table_args__ = (
        UniqueConstraint('id', 'va_version'),
    )
    id = sa.Column(sa.Integer)
    user_id = sa.Column(sa.Integer)

va.init()  # Only call this once
Example.register(ExampleArchive, engine)  # Call this once per engine, AFTER va.init