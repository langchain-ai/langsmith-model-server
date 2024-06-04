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

## Testing

To test that your server is running correctly, we have a helpful `test_server.py` script that leverages [RemoteRunnable](https://github.com/langchain-ai/langserve/blob/main/langserve/client.py#L259). To run the test, run the following command:

```bash
poetry run python test_server.py
```

You should see a response from the server indicating that the server is running correctly.

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

TODO: Add instructions for using your model server in the LangSmith Playground.
