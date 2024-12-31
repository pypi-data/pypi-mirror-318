import asyncio
import json
import unittest

from sqlactive.conn import DBConnection

from ._logger import logger
from ._models import User, Post
from ._seed import Seed


class TestSerializationMixin(unittest.IsolatedAsyncioTestCase):
    """Tests for `sqlactive.serialization.SerializationMixin`."""

    DB_URL = 'sqlite+aiosqlite://'

    @classmethod
    def setUpClass(cls):
        logger.info('ActiveRecordBaseModel tests...')
        logger.info('Creating DB connection...')
        cls.conn = DBConnection(cls.DB_URL, echo=False)
        seed = Seed(cls.conn)
        asyncio.run(seed.run())

    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'conn'):
            logger.info('Closing DB connection...')
            asyncio.run(cls.conn.close())

    async def test_to_dict(self):
        """Test for `to_dict` function."""

        logger.info('Testing `to_dict` function...')
        user = await User.with_subquery(User.posts).filter(id=1).one()
        self.assertDictEqual(
            {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'age': user.age,
                'created_at': user.created_at,
                'updated_at': user.updated_at,
            },
            user.to_dict(),
        )
        self.assertDictEqual(
            {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'age': user.age,
                'created_at': user.created_at,
                'updated_at': user.updated_at,
                'is_adult': user.is_adult,
            },
            user.to_dict(hybrid_attributes=True),
        )
        self.assertDictEqual(
            {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'age': user.age,
                'is_adult': user.is_adult,
            },
            user.to_dict(hybrid_attributes=True, exclude=['created_at', 'updated_at']),
        )
        self.assertDictEqual(
            {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'age': user.age,
                'posts': [post.to_dict() for post in user.posts],
                'is_adult': user.is_adult,
            },
            user.to_dict(nested=True, hybrid_attributes=True, exclude=['created_at', 'updated_at']),
        )

    async def test_to_json(self):
        """Test for `to_json` function."""

        logger.info('Testing `to_json` function...')
        user = await User.with_subquery(User.posts).filter(id=1).one()
        self.assertEqual(json.dumps(user.to_dict(), ensure_ascii=False, default=str), user.to_json())
        self.assertEqual(
            json.dumps(user.to_dict(hybrid_attributes=True), ensure_ascii=False, default=str),
            user.to_json(hybrid_attributes=True),
        )
        self.assertEqual(
            json.dumps(
                user.to_dict(hybrid_attributes=True, exclude=['created_at', 'updated_at']),
                ensure_ascii=False,
                default=str,
            ),
            user.to_json(hybrid_attributes=True, exclude=['created_at', 'updated_at']),
        )
        self.assertEqual(
            json.dumps(
                user.to_dict(nested=True, hybrid_attributes=True, exclude=['created_at', 'updated_at']),
                ensure_ascii=False,
                default=str,
            ),
            user.to_json(nested=True, hybrid_attributes=True, exclude=['created_at', 'updated_at']),
        )

    def test_from_dict(self):
        """Test for `from_dict` function."""

        logger.info('Testing `from_dict` function...')
        user = User.from_dict({'id': 1, 'username': 'username', 'name': 'name', 'age': 0, 'is_adult': False})
        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.name, 'name')
        self.assertEqual(user.age, 0)
        self.assertEqual(user.is_adult, False)

        user = User.from_dict(
            {
                'id': 1,
                'username': 'username',
                'name': 'name',
                'age': 0,
                'is_adult': False,
                'posts': [
                    {'id': 1, 'title': 'title', 'body': 'body', 'rating': 0, 'user_id': 1},
                    {'id': 2, 'title': 'title', 'body': 'body', 'rating': 0, 'user_id': 1},
                ],
            }
        )
        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.name, 'name')
        self.assertEqual(user.age, 0)
        self.assertEqual(user.is_adult, False)
        EXPECTED_POSTS = Post.from_dict(
            [
                {'id': 1, 'title': 'title', 'body': 'body', 'rating': 0, 'user_id': 1},
                {'id': 2, 'title': 'title', 'body': 'body', 'rating': 0, 'user_id': 1},
            ]
        )
        for i in range(len(user.posts)):
            self.assertDictEqual(EXPECTED_POSTS[i].to_dict(), user.posts[i].to_dict())

    def test_from_json(self):
        """Test for `from_json` function."""

        logger.info('Testing `from_json` function...')
        user = User.from_json('{"id": 1, "username": "username", "name": "name", "age": 0, "is_adult": false}')
        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.name, 'name')
        self.assertEqual(user.age, 0)
        self.assertEqual(user.is_adult, False)

        user = User.from_json(
            '{"id": 1, "username": "username", "name": "name", "age": 0, "is_adult": false, "posts": [{"id": 1, "title": "title", "body": "body", "rating": 0, "user_id": 1}, {"id": 2, "title": "title", "body": "body", "rating": 0, "user_id": 1}]}'
        )
        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, 'username')
        self.assertEqual(user.name, 'name')
        self.assertEqual(user.age, 0)
        self.assertEqual(user.is_adult, False)
        EXPECTED_POSTS = Post.from_json(
            '[{"id": 1, "title": "title", "body": "body", "rating": 0, "user_id": 1}, {"id": 2, "title": "title", "body": "body", "rating": 0, "user_id": 1}]'
        )
        for i in range(len(user.posts)):
            self.assertDictEqual(EXPECTED_POSTS[i].to_dict(), user.posts[i].to_dict())
