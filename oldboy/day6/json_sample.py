import json

name = {
    'alex': [22, "M"],
    'rain': [21, "F"]
}

name_after_transfer = json.dumps(name)

print name_after_transfer