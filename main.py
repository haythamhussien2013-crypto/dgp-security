from fastapi import FastAPI
from security.verification import generate_code, verify_code

app = FastAPI()


@app.get("/")
def home():
    return {"status": "DGP Security Engine Running"}


@app.get("/generate/{user_id}")
def generate(user_id: str):
    code = generate_code(user_id)

    return {
        "user": user_id,
        "verification_code": code
    }


@app.get("/verify/{user_id}/{code}")
def verify(user_id: str, code: int):
    result = verify_code(user_id, code)

    return {
        "user": user_id,
        "code": code,
        "verified": result
    }
from security.token import generate_token, verify_token
