import argparse
import re
from tinydb import TinyDB
import sys

def validate_type(name, value):
    if name == "email":
        return bool(re.match(r"[^@]+@[^@]+\.[^@]+", value))
    if name == "phone":
        return bool(re.match(r"\+7 \d{3} \d{3} \d{2} \d{2}", value))
    if name == "date":
        return bool(re.match(r"\d{2}\.\d{2}\.\d{4}", value) or re.match(r"\d{4}-\d{2}-\d{2}", value))
    return True

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd')
    parser.add_argument('-f', '--fields', nargs='*')
    args, unknown = parser.parse_known_args()
    fields = {}
    for arg in unknown:
        if arg.startswith('--'):
            k, v = arg[2:].split('=', 1)
            fields[k] = v
    return args.cmd, fields

def main():
    cmd, fields = parse_args()
    db = TinyDB('forms_db.json')
    templates = db.all()
    request_fields = []
    for k, v in fields.items():

        if validate_type("email", v):
            ftype = "email"
        elif validate_type("phone", v):
            ftype = "phone"
        elif validate_type("date", v):
            ftype = "date"
        else:
            ftype = "text"
        request_fields.append({"name": k, "type": ftype})


    for tpl in templates:
        tpl_fields = tpl['fields']
        found = True
        for f in tpl_fields:
            if not any(rf['name'] == f['name'] and rf['type'] == f['type'] for rf in request_fields):
                found = False
                break
        if found:
            print(tpl['name'])
            sys.exit(0)
    for rf in request_fields:
        print(f"{rf['name']}: {rf['type']}")


if __name__ == "__main__":
    main()

