from xbrain import xbrain_tool
from gevent.pywsgi import WSGIServer
from flask import jsonify
from xbrain.chat import run
from pydantic import BaseModel, Field
from typing import List
from flask_openapi3 import OpenAPI, Info
from flask import jsonify
from pydantic import BaseModel, Field, ValidationError

from xbrain.context import Type


class ChatMessage(BaseModel):
    role: str = Field(..., description="Role, can only be 'assistant' or 'user'", examples=["user", "assistant"], json_schema_extra={"enum": ["assistant", "user"]})
    content: str = Field(..., description="Content", examples=["Please help me write a function", "Hello, I am the assistant"])

class ChatRequestBody(BaseModel):
    messages: List[ChatMessage] = Field(..., description="List of messages")

class ChatResponseChoiceMessage(BaseModel):
    role: str = Field(..., description="Role", examples=["assistant"])
    content: str = Field(..., description="Response content")

class ChatResponseChoice(BaseModel):
    message: ChatResponseChoiceMessage = Field(..., description="Message")

class ChatResponse(BaseModel):
    status: str = Field(default="success", description="Status")
    choices: List[ChatResponseChoice] = Field(..., description="List of choices")


class ValidationErrorModel(BaseModel):
    status: str = Field(..., json_schema_extra={"enum": ["error", "success"]})
    content: str = Field(...)


def validation_error_callback(e: ValidationError):
    validation_error_object = ValidationErrorModel(status="error", content=str(e))
    response = jsonify(validation_error_object.dict())
    return response

info = Info(title="XBrain API", version="1.0.0")

app = OpenAPI(__name__,
              validation_error_status=200,
              validation_error_model=ValidationErrorModel,
              validation_error_callback=validation_error_callback
              )
app.json.sort_keys = False

@app.post("/chat", summary="Chat Interface", responses={200: ChatResponse})
def chat(body: ChatRequestBody):
    """
    Chat Interface
    """
    res = run(body.messages, chat_model=True)
    return jsonify({"status": "success", "choices": [{"message": {"role": "assistant", "content": res}}]})

class XBrainDeploy(BaseModel):
    """Deploy capabilities as a service"""
    pass

@xbrain_tool.Tool(model=XBrainDeploy, hit_condition={Type.IS_XBRAIN_PROJECT: True})
def deploy():
    port = 8001
    print(f"Service started, chat at: http://127.0.0.1:{port}/chat")
    http_server = WSGIServer(("0.0.0.0", port), app)
    http_server.serve_forever()