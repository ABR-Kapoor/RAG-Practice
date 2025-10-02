from fastapi import Request
from fastapi.responses import JSONResponse
from logger import logger

async def catch_exceptions_middleware(request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        logger.error(f"Unhandled exception: {e}")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)},
        )