import os
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from pirate_speak.chain import chain as pirate_speak_chain
from einbot.chain import chain as einbot_chain
from mia.chain import chain as mia_chain
from langchain.schema.runnable import Runnable
from langserve import add_routes

ON_HEROKU = os.environ.get('ON_HEROKU')

origins = [
    "https://nlux.ai",
    "https://docs.nlux.ai"
]

if ON_HEROKU:
    # Additional origins that may be added/configured via HEROKU
    HEROKU_ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS")
    if HEROKU_ALLOWED_ORIGINS:
        origins_to_add = HEROKU_ALLOWED_ORIGINS.split(",")
        for origin in origins_to_add:
            origins.append(origin)
else:
    # Below are used for dev purposes on localhost
    # Do not deploy to a public remove server
    origins.append("http://localhost:9090")

app = FastAPI(debug=False, docs_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


def add_route(path: str, chain: Runnable):
    add_routes(
        app,
        runnable=chain,
        path=path,
        enabled_endpoints=["invoke", "stream", "input_schema", "output_schema"],
    )


add_route("/pirate-speak", pirate_speak_chain)
add_route("/einbot", einbot_chain)
add_route("/mia", mia_chain)

if __name__ == "__main__":
    import uvicorn

    if ON_HEROKU:
        port = int(os.environ.get("PORT", 17995))
    else:
        port = 8000

    uvicorn.run(app, host="0.0.0.0", port=port)
