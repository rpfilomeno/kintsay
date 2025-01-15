from smolagents import CodeAgent, ToolCallingAgent, LiteLLMModel, DuckDuckGoSearchTool
from kintsay.config import logger, DEFAULT_CONFIG
from kintsay.tools import post_to_social_media_tool


class __KintsayAgent:
    def __init__(self, namespace=None):

        self.namespace = namespace or DEFAULT_CONFIG["namespace"]
        self.model = LiteLLMModel(
            model_id=DEFAULT_CONFIG["model"], api_key=DEFAULT_CONFIG["api_key"]
        )
        self.__agent = ToolCallingAgent(
            tools=[post_to_social_media_tool],
            model=self.model,
            max_steps=DEFAULT_CONFIG["max_steps"],
        )
        
        

    def ask(self, prompt):
        logger.info(f"Running with prompt: {prompt}")
        response = self.__agent.run(prompt=prompt)
        logger.info(f"Response: {response}")
        return {
            "model": self.model.name,
            "namespace": self.namespace,
            "prompt": prompt,
            "response": response,
        }


__agent: __KintsayAgent|None = None


def get_instance():
    if __agent is None:
        __agent = __KintsayAgent()
    return __agent
