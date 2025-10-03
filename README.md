# autoatendimento-lambda-identify

Lambda que recebe CPF e retorna um JWT de 5 minutos para identificação leve do cliente.

## Estrutura
- `src/handler.py` — handler principal (Lambda Proxy).
- `src/jwt_utils.py` — geração do JWT (HS256 para dev; trocar por KMS/Cognito em prod).
- `requirements.txt` — dependências (PyJWT).
- `.github/workflows/ci.yml` — pipeline que gera o ZIP como artifact.

## Teste local rápido (simulando evento API Gateway)
```bash
python - << 'PY'
import json
from src.handler import lambda_handler
print(lambda_handler({"body": json.dumps({"cpf": "12345678901"})}, None))
PY
```
test

