import unittest
from Schema import Schema

class TestSchema(unittest.TestCase):

    def setUp(self):
        self.schema = Schema({
            'name': {'type': str, 'required': True},
            'age': {'type': int, 'required': True, 'default': 18},
            'email': {'type': str, 'required': False, 'default': 'test@example.com'}
        })

    def test_listToDict(self):
        values = ['John Doe', 30, 'john@example.com']
        expected = {'name': 'John Doe', 'age': 30, 'email': 'john@example.com'}
        result = self.schema.listToDict(values)
        self.assertEqual(result, expected)

    def test_validate(self):
        data = {'name': 'John Doe', 'age': 30}
        self.assertTrue(self.schema.validate(data))

        data = {'name': 'John Doe'}
        self.assertTrue(self.schema.validate(data))
        self.assertEqual(data['age'], 18)

        data = {'name': 'John Doe', 'age': 'thirty'}
        with self.assertRaises(ValueError):
            self.schema.validate(data)

    def test_listOfKeysToApply(self):
        schema_with_apply = Schema({
            'name': {'type': str, 'required': True, 'apply': lambda x: x.upper()},
            'age': {'type': int, 'required': True, 'default': 18},
            'email': {'type': str, 'required': False, 'default': 'test@example.com'}
        })
        data = {'name': 'John Doe', 'age': 30, 'email': 'john@example.com'}
        expected = ['name']
        result = schema_with_apply.listOfKeysToApply(data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
