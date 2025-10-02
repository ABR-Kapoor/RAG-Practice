from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from middlewares.exception_handlers import catch_exceptions_middleware
from routers.upload_pdfs import router as upload_router
from routers.ask_question import router as ask_router

app = FastAPI()

# cors setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# middleware exception handlers
app.middleware("http")(catch_exceptions_middleware)


# router
# 1. upload pdfs
app.include_router(upload_router)
# 2. asking queries
app.include_router(ask_router)