import json


def save_json(path, data):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def load_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


# (1) ჩაწერა და წაკითხვა
save_json("student.json", {"name": "ნინო", "scores": [90, 85], "pair": (1, 2)})
student = load_json("student.json")
print(student)
print(type(student["pair"]))

# (2) არარსებული ფაილი
print(load_json("missing.json", default={}))

# (3) არასწორი JSON ფაილი
with open("broken.json", "w", encoding="utf-8") as file:
    file.write('{"name": "ნინო",}')

print(load_json("broken.json", default="არასწორი ფაილი"))
