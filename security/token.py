import random

codes = {}

def generate_code(user_id: str):
    code = random.randint(100000, 999999)
    codes[user_id] = code
    return code

def verify_code(user_id: str, code: int):
    if user_id in codes and codes[user_id] == code:
        return True
    return False