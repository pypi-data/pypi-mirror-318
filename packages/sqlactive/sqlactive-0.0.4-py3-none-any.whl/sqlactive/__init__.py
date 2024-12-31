"""
# SQLActive

A sleek, powerful and asynchronous ActiveRecord-style wrapper for SQLAlchemy.
Bring Django-like queries, automatic timestamps, nested eager loading,
and dictionary serialization for SQLAlchemy models.

Heavily inspired by [sqlalchemy-mixins](https://github.com/absent1706/sqlalchemy-mixins/).

Documentation: https://daireto.github.io/sqlactive/

This package provides a set of mixins for SQLAlchemy models
and a base class for all models.

The CRUD methods are defined in the `ActiveRecordMixin` class which
provides ActiveRecord-like behavior. It also inherits from
`SessionMixin` and `SmartQueryMixin` classes:

- `SessionMixin` class provides a session handler.
- `SmartQueryMixin` class adds smart query capabilities. It also inherits
from `InspectionMixin` class which provides helper methods for inspecting
the model.

The `ActiveRecordBaseModel` class is a base class for all models
that inherits from `ActiveRecordMixin` class which provides the set
of ActiveRecord-like helper methods for interacting with the database,
`TimestampMixin` class which adds the `created_at` and `updated_at`
timestamp columns, and `SerializationMixin` class which provides
serialization and deserialization methods.

It is recommended to define a `BaseModel` class that inherits from
`ActiveRecordBaseModel` and use it as the base class for all models
as shown in the following example:

```python
    from sqlalchemy import Mapped, mapped_column
    from sqlactive import ActiveRecordBaseModel

    class BaseModel(ActiveRecordBaseModel):
        __abstract__ = True

    class User(BaseModel):
        __tablename__ = 'users'
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(100))

    # Create engine
    DATABASE_URL = 'sqlite+aiosqlite://'
    engine = create_async_engine(DATABASE_URL, echo=True)
    async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)

    # Create session
    session = async_scoped_session(async_session_factory, scopefunc=asyncio.current_task)
    BaseModel.set_session(session)

    # Create tables
    BaseModel.metadata.create_all(engine)
```

`TimestampMixin` class defines the `created_at` and `updated_at` columns
with default values and onupdate behavior. To know how to customize the
timestamps behavior, check the `TimestampMixin` class documentation in
`sqlactive.timestamp.TimestampMixin` or in the following link:
https://daireto.github.io/sqlactive/latest/pages/timestamp_mixin/

Your `BaseModel` class can also inherit directly from the mixins. For
example, if you don't want to implement automatic timestamps don't inherit
from `ActiveRecordBaseModel` class. Instead, inherit from `ActiveRecordMixin`
and/or `SerializationMixin` as shown in the following example:

```python
    from sqlalchemy import Mapped, mapped_column
    from sqlactive import ActiveRecordMixin, SerializationMixin

    class BaseModel(ActiveRecordMixin, SerializationMixin):
        __abstract__ = True

    class User(BaseModel):
        __tablename__ = 'users'
        id: Mapped[int] = mapped_column(primary_key=True)
        name: Mapped[str] = mapped_column(String(100))
```

NOTE: When defining a `BaseModel` class, don't forget to set `__abstract__` to `True`
in the base class to avoid creating tables for the base class.

### ActiveRecord-like methods
>>> bob = User.create(name='Bob')
>>> bob
# <User #1>
>>> bob.name
# Bob
>>> User.where(name='Bob').all()
# [<User #1>]
>>> User.get(1)
# <User #1>
>>> bob.update(name='Bob2')
>>> bob.name
# Bob2
>>> bob.to_dict()
# {'id': 2, 'name': 'Bob2'}
>>> bob.delete()
>>> User.all()
# []

### DBConnection helper
To create a DB connection, create a instance of the `DBConnection` class and call the `init_db` method
as shown in the following example:
```python
    from sqlactive import ActiveRecordBaseModel, DBConnection

    class BaseModel(ActiveRecordBaseModel):
        __abstract__ = True

    DATABASE_URL = 'sqlite+aiosqlite://'
    conn = DBConnection(DATABASE_URL, echo=True)
    asyncio.run(conn.init_db(BaseModel))
```

If no base model is provided, the `ActiveRecordBaseModel` class will be used as the base model:
```python
    from sqlactive import DBConnection

    DATABASE_URL = 'sqlite+aiosqlite://'
    conn = DBConnection(DATABASE_URL, echo=True)
    asyncio.run(conn.init_db())
```
"""

from .base_model import ActiveRecordBaseModel
from .active_record import ActiveRecordMixin
from .serialization import SerializationMixin
from .timestamp import TimestampMixin
from .definitions import JOINED, SUBQUERY, SELECT_IN
from .conn import DBConnection


__all__ = [
    'ActiveRecordBaseModel',
    'ActiveRecordMixin',
    'SerializationMixin',
    'TimestampMixin',
    'JOINED',
    'SUBQUERY',
    'SELECT_IN',
    'DBConnection'
]


__version__ = '0.0.4'
