from xbrain import xbrain_tool
from gevent.pywsgi import WSGIServer
from flask import jsonify
from xbrain.main import run
from pydantic import BaseModel, Field
from typing import List
from flask_openapi3 import OpenAPI, Info
from flask import jsonify
from pydantic import BaseModel, Field, ValidationError


class ChatMessage(BaseModel):
    role: str = Field(..., description="角色, 只能是 assistant 或 user", examples=["user", "assistant"], json_schema_extra={"enum": ["assistant", "user"]})
    content: str = Field(..., description="内容", examples=["请你帮我写一个函数", "你好，我是assistant"])

class ChatRequestBody(BaseModel):
    botId: str = Field(..., description="botId")
    messages: List[ChatMessage] = Field(..., description="消息列表")

class ChatResponseChoiceMessage(BaseModel):
    role: str = Field(..., description="角色", examples=["assistant"])
    content: str = Field(..., description="响应内容")

class ChatResponseChoice(BaseModel):
    message: ChatResponseChoiceMessage = Field(..., description="消息")

class ChatResponse(BaseModel):
    status: str = Field(default="success", description="状态")
    choices: List[ChatResponseChoice] = Field(..., description="选择列表")


class ValidationErrorModel(BaseModel):
    status: str = Field(..., json_schema_extra={"enum": ["error", "success"]})
    content: str = Field(...)


def validation_error_callback(e: ValidationError):
    validation_error_object = ValidationErrorModel(status="error", content=e.__str__())
    response = jsonify(validation_error_object.model_dump())
    return response

info = Info(title="XBrain API", version="1.0.0")

app = OpenAPI(__name__,
              validation_error_status=200,
              validation_error_model=ValidationErrorModel,
              validation_error_callback=validation_error_callback
              )
app.json.sort_keys = False

@app.post("/chat", summary="聊天接口", responses={200: ChatResponse})
def chat(body: ChatRequestBody):
    """
    聊天接口
    """
    run(body.messages)
    return jsonify({"status": "success", "choices": [{"message": {"role": "assistant", "content": res}}]})

class Deploy(BaseModel):
    """部署服务器"""
    pass

@xbrain_tool.Tool(model=Deploy)
def deploy():
    port = input("请输入服务器监听的端口，默认为8000\n>>> ")
    if not port or not port.isdigit():
        port = 8000
    else:
        port = int(port)    
    print(f"Starting server, listen port: {port}")
    http_server = WSGIServer(("0.0.0.0", port), app)
    http_server.serve_forever()