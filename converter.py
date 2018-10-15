import csv
import json
from pymongo import MongoClient



file = 'cleaned.csv'
json_file = 'output.json'

#database settings
client = MongoClient('mongodb://localhost:27017')
db = client.pymongo_dev
infos = db.infos

#Read CSV File
def read_CSV(file, json_file):
    csv_rows = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        field = reader.fieldnames
        for row in reader:
            csv_rows.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        convert_write_json(csv_rows, json_file)

#Convert csv data into json
def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': '))) #for pretty
        save_json_data()

#read from json
def read_json():
    with open(json_file) as f:
        data = json.load(f)
        return data


#save to database
def save_json_data():
    output = read_json()
    new_result = infos.insert_many(output)
    print('Multiple data: {0}'.format(new_result.inserted_ids))


read_CSV(file,json_file)
