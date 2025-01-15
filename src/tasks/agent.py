import kintsay
from kintsay.config import DEFAULT_CONFIG
from celery import Celery

app = Celery(
    broker="redis://redis:6379",
    backend="redis://redis:6379",
)


@app.task()
def ask(*args, **kwargs):
    agent = kintsay.get_instance()
    response = agent.ask(prompt=kwargs["prompt"])
    return response


if __name__ == "__main__":
    args = ["worker", "--loglevel=INFO"]
    app.worker_main(argv=args)
