import json
import os


def add_to_json(filename, dictionary):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            json.dump([], file)

    try:
        with open(filename, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(dictionary)

    with open(filename, 'w') as file:
        json.dump(data, file)


filename = "data.json"
dictionary = {"name": "Hari", "age": 30}
add_to_json(filename, dictionary)
