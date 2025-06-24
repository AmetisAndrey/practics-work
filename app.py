import math
import sys
import re
from tinydb import TinyDB
import os

args = sys.argv
if len(args) < 2 or args[1] != "get_tpl":
    sys.exit(1)

db = TinyDB(os.path.join("database", "database.json"))
query_fields = {}
i = 2
while i < len(args):
    arg = args[i]
    if arg.startswith("--"):
        if "=" in arg:
            key, val = arg[2:].split("=", 1)
            query_fields[key] = val
            i += 1
        else:
            key = arg[2:]
            if i + 1 < len(args):
                query_fields[key] = args[i + 1]
            i += 2
    else:
        i += 1

def detect_type(value):
    if re.match(r'^\d{2}\.\d{2}\.\d{4}$', value) or re.match(r'^\d{4}-\d{2}-\d{2}$', value):
        return "date"
    if re.match(r'^\+7 \d{3} \d{3} \d{2} \d{2}$', value):
        return "phone"
    if re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', value):
        return "email"
    return "text"



query_types = {k: detect_type(v) for k, v in query_fields.items()}

for form in db.all():
    template = {k: v for k, v in form.items() if k != "name"}
    if all(k in query_types and template[k] == query_types[k] for k in template):
        print(form["name"])
        break
else:
    print("{")
    items = list(query_types.items())
    for idx, (k, v) in enumerate(items):
        comma = "," if idx < len(items) - 1 else ""
        print(f'  "{k}": "{v}"{comma}')
    print("}")