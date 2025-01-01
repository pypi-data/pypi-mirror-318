import unittest
from DataObject import DataObject
from Schema import Schema
from datetime import datetime
import random


class TestDataObject(unittest.TestCase):

    def setUp(self):
        self.schema = Schema({
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

    def test_applySchema(self):
        data = {
            'name': 'Jane Doe',
            'age': 25,
            'email': 'jane@example.com',
            'posted_at': '2023-01-01 00:00:00'
        }
        data_object = DataObject(data, self.schema)
        data_object.applySchema()
        self.assertEqual(data_object.getData()['name'], 'JANE DOE')
        self.assertNotEqual(data_object.getData()['age'], 25)
        self.assertEqual(data_object.getData()['email'], 'jane@example.com')
        self.assertNotEqual(data_object.getData()['posted_at'], '2023-01-01 00:00:00')

    def test_getData(self):
        data = {
            'name': 'Jane Doe',
            'age': 25,
            'email': 'jane@example.com',
            'posted_at': '2023-01-01 00:00:00'
        }
        data_object = DataObject(data, self.schema)
        self.assertEqual(data_object.getData(), data)


if __name__ == '__main__':
    unittest.main()
