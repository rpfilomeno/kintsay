import pytest
from kintsay.config import logger, DEFAULT_CONFIG
from smolagents import CodeAgent, LiteLLMModel, DuckDuckGoSearchTool
from celery import Celery


def test_smolagents():
    agent = CodeAgent(
        tools=[DuckDuckGoSearchTool()],
        model=LiteLLMModel(
            model_id=DEFAULT_CONFIG["model"],
            api_key=DEFAULT_CONFIG["api_key"],
        ),
        additional_authorized_imports=["math", "requests"],
        verbose=True,
    )

    result = agent.run(
        "Could you give me the 5th number in the Fibonacci sequence?",
    )

    logger.info(f"Result: {result}")

    assert result == 5


def test_celery():
    app = Celery(
        DEFAULT_CONFIG["namespace"],
        broker=DEFAULT_CONFIG["broker"],
        backend=DEFAULT_CONFIG["backend"],
    )

    @app.task
    def task():
        return "hello world"

    result = task.delay()
    assert result.get() == "hello world"


if __name__ == "__main__":
    test_celery()
