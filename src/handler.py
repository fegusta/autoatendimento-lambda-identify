import json, time, re
from jwt_utils import mint_jwt

CPF_RE = re.compile(r"^\d{11}$")

def lambda_handler(event, context):
    body = json.loads(event.get("body") or "{}")
    cpf = (body.get("cpf") or "").strip()

    if not CPF_RE.match(cpf):
        return {"statusCode": 400, "body": json.dumps({"error":"CPF inválido"})}

    now = int(time.time())
    claims = {
        "sub": cpf,
        "cpf": cpf,
        "iat": now,
        "exp": now + 300,   # 5 minutos
        "iss": "lambda-identify"
    }

    token = mint_jwt(claims)
    return {"statusCode": 200, "body": json.dumps({"token": token})}
