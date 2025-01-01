import unittest
from pymongo import MongoClient
from Database import Database
from Schema import Schema
from DataObject import DataObject
from unittest.mock import patch, MagicMock
from uuid import uuid4
from datetime import datetime
import random


class TestDatabase(unittest.TestCase):

    @patch('Database.MongoClient')
    def setUp(self, MockMongoClient):
        self.mock_client = MockMongoClient.return_value
        self.mock_db = self.mock_client.__getitem__.return_value
        self.mock_collection = self.mock_db.__getitem__.return_value
        self.db = Database('mongodb://localhost:27017/', 'test_db', 'test_collection')

    def test_create(self):
        schema = Schema({
            'name': {
                'type': str,
                'default': 'John Doe',
                'apply': lambda x: x.upper()
            },
            'age': {
                'type': int,
                'default': 18,
                'apply': lambda x: random.randint(18, 60),
                'required': True
            },
            'email': {
                'type': str,
                'default': 'akshitshubhammas@gmail.com',
            },
            'posted_at': {
                'type': str,
                'default': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'apply': lambda x: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        })
        data = {}
        self.db.create(schema, data)
        self.mock_collection.insert_one.assert_called_once()
        inserted_data = self.mock_collection.insert_one.call_args[0][0]
        self.assertIn('_id', inserted_data)
        self.assertEqual(inserted_data['name'], 'JOHN DOE')
        self.assertEqual(inserted_data['email'], 'akshitshubhammas@gmail.com')

    def test_get(self):
        query = {'name': 'John Doe'}
        self.db.get(query)
        self.mock_collection.find.assert_called_once_with(query)

    def test_printAll(self):
        self.mock_collection.find.return_value = [
            {'name': 'John Doe', 'age': 30, 'email': 'john@example.com'},
            {'name': 'Jane Doe', 'age': 25, 'email': 'jane@example.com'}
        ]
        with patch('builtins.print') as mock_print:
            self.db.printAll()
            self.assertEqual(mock_print.call_count, 2)
            mock_print.assert_any_call({'name': 'John Doe', 'age': 30, 'email': 'john@example.com'})
            mock_print.assert_any_call({'name': 'Jane Doe', 'age': 25, 'email': 'jane@example.com'})


if __name__ == '__main__':
    unittest.main()
