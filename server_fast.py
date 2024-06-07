# coding: utf-8
# @author: outlaws-bai
# @date: 2024/05/31 16:57:21
# @description: fastapi pycryptodome
import base64
import json
from fastapi import FastAPI, HTTPException, Request, Response
from pydantic import BaseModel
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

app = FastAPI()

# 密钥和IV（初始向量），AES-256需要32字节的密钥和16字节的IV
KEY = b"32byteslongsecretkeyforaes256!aa"
IV = b"16byteslongiv456"

# 模拟用户数据库
users_db = {
    "user1": {"id": 1, "name": "Alice", "email": "alice@example.com"},
    "user2": {"id": 2, "name": "Bob", "email": "bob@example.com"},
}


# AES加密函数
def aes_encrypt(data: bytes) -> bytes:
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return base64.b64encode(ct_bytes)


lambda x: json.loads(x.decode())["data"]


# AES解密函数
def aes_decrypt(data: bytes) -> bytes:
    data1 = base64.b64decode(data)
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    pt = unpad(cipher.decrypt(data1), AES.block_size)
    return pt


# 请求模型
class EncryptedRequest(BaseModel):
    data: str


# 响应模型
class EncryptedResponse(BaseModel):
    data: str


@app.post("/getUserInfo", response_model=EncryptedResponse)
async def get_user_info(request: EncryptedRequest):
    # 解密请求数据
    decrypted_data = aes_decrypt(request.data.encode())
    request_data = json.loads(decrypted_data)
    username = request_data.get("username")

    # 查询用户信息
    user_info = users_db.get(username)
    if not user_info:
        raise HTTPException(status_code=404, detail="User not found")

    # 加密响应数据
    response_data = json.dumps(user_info)
    encrypted_response = aes_encrypt(response_data.encode())

    return EncryptedResponse(data=encrypted_response.decode())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
