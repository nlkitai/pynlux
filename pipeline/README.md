## Dependencies

The project dependencies and versions are listed in the `pyproject.toml` files, at the root level and at each package
directory.

The key dependencies include:

* `langchain-community` and `langchain-core` ― Used in packages to build LLM chains and logic
* `langserve` ― Used to create RESET APIs built on top LangChain modules and `FastAPI`
* `openai` ― Used by several packages to build demo endpoints consumed by NLUX
* `FastAPI` and `uvicorn` ― Used for the REST endpoints and HTTP server

## Package Management + Build System

* This project was developed using `Anaconda Python` distribution.
* The commands in this document describe how to
install and configure packages in the context of Anaconda Python and `Conda` package manager, but you still
can do the same thing using PIP or any other package manager or distribution.
* This project uses `Python Poetry` for **dependency management** and packaging ― 
You can read more Poetry [here](https://python-poetry.org/docs/).

* This project was developed using Python  `version 3.12.1`

## Environment Variables

In order to run the project (in development or in production), the following environment variables should be set:

* `OPENAI_API_KEY` ― The API key to use for calls to OpenAI services

## Development

To run the development server:

1. Install `Python 3.12` and `Poetry` on your dev machine ― if they are not already installed.
2. Install `langchain-cli` on your dev machine. It's currently available via PIP. You can install it via PIP
and access it from a conda environment by running:

```shell
conda config --set pip_interop_enabled True
pip install langchain-cli
```

Set environment variables:
2. Add your [OpenAI API Key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-api-key) in `OPENAI_API_KEY` environment variable.
3. Install dependencies by running:

```shell
poetry install
```

4. Start the dev server by running:

```shell
poetry run dev
```

## Deployment

The project is configured for deployment on [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python).<br />
To deploy to Heroku:

1. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login to hero using `heroku login`
3. Set your application's **Heroku Git Remote** using command:<br />

```shell
heroku git:remote --app {YOUR_APP_ID_FROM_HEROKU}
```

4. Set the Heroku Build Packs for `poetry` and `python`

```shell
heroku buildpacks:clear
heroku buildpacks:add https://github.com/moneymeets/python-poetry-buildpack.git
heroku buildpacks:add heroku/python
heroku config:set POETRY_EXPORT_DEV_REQUIREMENTS=1
```

5. Push your code to the Heroku remote:

```shell
git push heroku main
```

## Poetry + Dev Env Config

Since deploying to Heoku depends on having a `poetry.lock` properly set, and matching the Python version used
on the Heroku server, it's important to make sure that you're using a compatible Python version (ideally `3.12.1`)
and matching Poetry version (ideally `1.7.1`).

The following [Conda](https://conda.io/projects/conda/en/latest/user-guide/index.html) instructions can help in 
setting up the right Python and Poetry versions.

* Have a Conda channel with the latest packages configure ― [Conda Forge](https://conda-forge.org/docs/user/introduction.html) is a great one.
* Make sure that your Conda packages are all update to date ― You can do that via `conda update --all` or via Anaconda-Navigator. 
* Configure your Conda environment with the right Python version, and activate it before running Poetry.
