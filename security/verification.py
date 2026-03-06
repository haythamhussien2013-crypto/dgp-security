import random
import time

codes = {}

def generate_code(user_id):
    code = random.randint(100000, 999999)
    codes[user_id] = {
        "code": code,
        "time": time.time()
    }
    return code


def verify_code(user_id, code):
    if user_id not in codes:
        return False

    stored_code = codes[user_id]["code"]

    if stored_code == code:
        return True

    return False