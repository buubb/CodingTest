import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hmac
import os

# HS512에 적합한 키 생성
def generate_hs512_key():
    # 랜덤 512비트 키 생성 (64 바이트)
    key = os.urandom(64)
    # Base64로 인코딩
    base64_key = base64.b64encode(key).decode('utf-8')
    return base64_key

if __name__ == "__main__":
    key = generate_hs512_key()
    print(f"Generated Key: {key}")
