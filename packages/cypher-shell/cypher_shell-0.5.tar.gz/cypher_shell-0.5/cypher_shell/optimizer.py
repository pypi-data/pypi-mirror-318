from typing import Any

from rich.markdown import Markdown
from swarm import Swarm

from .agent import Agent
from .prompts.optim import OPTIMIZATION_PROMPT_GENERAL


class Optimizer:
    def __init__(self, cfg: dict):
        self.optimizer_agent = Agent(
            name="Cypher Query Optimizer",
            model="gpt-4o-mini",
            temperature=0.0,
            instructions=OPTIMIZATION_PROMPT_GENERAL,
        )
        self.client = Swarm()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def optimize_query(self, query: dict[str, Any]) -> str:
        msg = self.client.run(
            agent=self.optimizer_agent,
            messages=[
                {
                    "role": "user",
                    "content": f"Query: {query}. Reread the query carefully: {query}",
                }
            ],
        )
        return Markdown(msg.messages[-1]["content"])
