from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pirate_speak.chain import chain as pirate_speak_chain
from einbot.chain import chain as einbot_chain
from langchain.schema.runnable import Runnable
from langserve import add_routes

app = FastAPI(debug=False, docs_url=None)
defaultEndpoints = ["invoke", "stream", "input_schema", "output_schema"]


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

if __name__ == "__main__":
    import uvicorn
    import os

    ON_HEROKU = os.environ.get('ON_HEROKU')
    if ON_HEROKU:
        port = int(os.environ.get("PORT", 17995))
    else:
        port = 8000

    uvicorn.run(app, host="0.0.0.0", port=port)
