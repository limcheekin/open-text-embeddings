# Created with the help of the ChatGPT (GPT-3.5)
# REF: https://chat.openai.com/share/4ab741e7-8059-4be1-b3da-46b8e78d98cc
# REF: https://gealber.com/gzip-middleware-fastapi
import gzip
from starlette.types import Message
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class GZipRequestMiddleware(BaseHTTPMiddleware):
    async def set_body(self, request: Request):
        receive_ = await request._receive()
        content_encoding = request.headers.get('Content-Encoding', '').lower()
        print("content_encoding", content_encoding)
        if 'gzip' in content_encoding:
            # print("receive_", receive_)

            try:
                content_length = int(
                    request.headers.get('Content-Length', '0'))
                body = receive_.get('body')
                if len(body) != content_length:
                    return JSONResponse(
                        content={"error": "Invalid Content-Length header"},
                        status_code=400,
                    )
                json_byte_string = gzip.decompress(body)
                receive_['body'] = json_byte_string
                print("content_length", content_length)
                # print("body", body)
                print("gzip decompressed body:", receive_['body'])
            except ValueError:
                return JSONResponse(
                    content={"error": "Invalid Content-Length header"},
                    status_code=400,
                )
            except Exception as e:
                print(e)
                return JSONResponse(
                    content={"error": "Failed to decompress gzip content"},
                    status_code=400,
                )

        async def receive() -> Message:
            return receive_

        request._receive = receive

    async def dispatch(self, request, call_next):
        await self.set_body(request)
        response = await call_next(request)
        return response
