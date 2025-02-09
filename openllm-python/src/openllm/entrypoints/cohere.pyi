from http import HTTPStatus
from typing import Optional, Union

from attr import AttrsInstance
from starlette.requests import Request
from starlette.responses import JSONResponse, Response

from bentoml import Service
from openllm_core._typing_compat import M, T

from .._llm import LLM
from ..protocol.cohere import CohereChatRequest, CohereGenerateRequest

def mount_to_svc(svc: Service, llm: LLM[M, T]) -> Service: ...
def jsonify_attr(obj: AttrsInstance) -> str: ...
def error_response(status_code: HTTPStatus, message: str) -> JSONResponse: ...
async def check_model(
  request: Union[CohereGenerateRequest, CohereChatRequest], model: str
) -> Optional[JSONResponse]: ...
async def cohere_generate(req: Request, llm: LLM[M, T]) -> Response: ...
async def cohere_chat(req: Request, llm: LLM[M, T]) -> Response: ...
