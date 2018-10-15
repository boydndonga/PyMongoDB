import unittest
import csv
import json
from pymongo import mongo_client



file = 'cleaned.csv'
json_file = 'output.json'
client = MongoClient('mongodb://localhost:27017')

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        db = client.pymongo_test

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()