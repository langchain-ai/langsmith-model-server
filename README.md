# LangSmith Model Server

This repository contains an example implementation of a LangSmith Model Server. This server leverages [LangServe](https://python.langchain.com/v0.2/docs/langserve/) to expose a REST API for interacting with a custom LangChain model implementation.
Once deployed, the server endpoint can be consumed by the LangSmith Playground to interact with your model.

## Setup
We recommend using poetry to manage dependencies. To install poetry, run the following command:

```bash
pip install poetry
```

Then, to install the dependencies, run the following command:

```bash
poetry install
```

## Adding a dependency

In some cases, your model implementation may require additional dependencies. To add a dependency, run the following command:

```bash
poetry add <package_name>
```

You will need to rebuild the Docker image after adding a dependency.

## Usage

After running through the setup, this server should work out of the box with the default configuration. To start the server, run the following command:

```bash
poetry run uvicorn app.server:app --host 0.0.0.0 --port <port>
```

The server should now be running
```
INFO:     Started server process [55114]
INFO:     Waiting for application startup.

 __          ___      .__   __.   _______      _______. _______ .______     ____    ____  _______
|  |        /   \     |  \ |  |  /  _____|    /       ||   ____||   _  \    \   \  /   / |   ____|
|  |       /  ^  \    |   \|  | |  |  __     |   (----`|  |__   |  |_)  |    \   \/   /  |  |__
|  |      /  /_\  \   |  . `  | |  | |_ |     \   \    |   __|  |      /      \      /   |   __|
|  `----./  _____  \  |  |\   | |  |__| | .----)   |   |  |____ |  |\  \----.  \    /    |  |____
|_______/__/     \__\ |__| \__|  \______| |_______/    |_______|| _| `._____|   \__/     |_______|

LANGSERVE: Playground for chain "/chat/" is live at:
LANGSERVE:  │
LANGSERVE:  └──> /chat/playground/
LANGSERVE:
LANGSERVE: Playground for chain "/" is live at:
LANGSERVE:  │
LANGSERVE:  └──> /playground/
LANGSERVE:
LANGSERVE: See all available routes at /docs/

INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

By default, we expose the chat model at `/chat` and the instruct model at `/`.

## Testing

To test that your server is running correctly, we have a helpful `test_server.py` script that leverages [RemoteRunnable](https://github.com/langchain-ai/langserve/blob/main/langserve/client.py#L259). To run the test, run the following command:

```bash
poetry run python test_server.py
```

You should see a response from the server indicating that the server is running correctly.

```bash
Pinging chat model: help
Pinging instruct model: help
```

## Running in Docker

This project folder includes a Dockerfile that allows you to easily build and host your model server. This will be needed 
to consume your model in the LangSmith Playground if not running LangSmith locally.

### Building the Image

To build the image, you simply:

```shell
docker build . -t my-model-server
```

If you tag your image with something other than `my-model-server`,
note it for use in the next step.

### Running the Image Locally

To run the image, you'll need to include any environment variables
necessary for your application. Our example implementation does not require any environment variables.

We also expose port 8080 with the `-p 8080:8080` option.

```shell
docker run -e ENV_VARIABLE=FOO -p 8080:8080 my-model-server
```

## Using in the LangSmith Playground

Refer to the LangSmith documentation for more information on how to use your model in the LangSmith Playground.

You can find the documentation [here](https://docs.smith.langchain.com/how_to_guides/playground/custom_endpoint).
