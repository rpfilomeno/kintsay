import time
from tasks import agent

print("starting..")
result = agent.ask.delay(prompt="what is the top news about AI today")

while not result.ready():
    print("waiting for results...")
    time.sleep(1)
print(result.result)
