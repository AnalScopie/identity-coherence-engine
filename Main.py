import json
from datetime import datetime

def normalize_name(name):
    return name.strip().capitalize()

def normalize_email(email):
    return email.strip().lower()

def normalize_phone(phone):
    return phone.replace(" ", "")

def process_identity(data):
    log = []
    output = {}

    new_first = normalize_name(data.get("first_name", ""))
    log.append(f"first_name: '{data.get('first_name')}' → '{new_first}'")
    output["first_name"] = new_first

    new_last = normalize_name(data.get("last_name", ""))
    log.append(f"last_name: '{data.get('last_name')}' → '{new_last}'")
    output["last_name"] = new_last

    new_email = normalize_email(data.get("email", ""))
    log.append(f"email: '{data.get('email')}' → '{new_email}'")
    output["email"] = new_email

    new_phone = normalize_phone(data.get("phone", ""))
    log.append(f"phone: '{data.get('phone')}' → '{new_phone}'")
    output["phone"] = new_phone

    return output, log

def run():
    with open("input.json", "r") as f:
        data = json.load(f)

    result, log = process_identity(data)

    with open("output.json", "w") as f:
        json.dump(result, f, indent=2)

    with open("audit.log", "w") as f:
        f.write(f"Audit log - {datetime.now()}\n\n")
        for entry in log:
            f.write(entry + "\n")

if __name__ == "__main__":
    run()
