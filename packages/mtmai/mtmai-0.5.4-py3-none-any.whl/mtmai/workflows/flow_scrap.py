import json
import uuid
from typing import cast

import structlog
from langchain_core.runnables import RunnableConfig
from langgraph.graph import StateGraph
from langgraph.graph.graph import CompiledGraph
from mtmai.agents.ctx import init_mtmai_context, mtmai_context
from mtmai.agents.graphutils import is_internal_node, is_skip_kind
from mtmai.agents.joke_graph import joke_graph
from mtmai.core.coreutils import is_in_dev
from mtmai.workflows.worker import wfapp
from mtmaisdk.clients.rest.models import AgentNodeRunRequest
from mtmaisdk.context.context import Context
from scrapegraphai.graphs import SmartScraperGraph

LOG = structlog.get_logger()


@wfapp.workflow(
    name="RunGraph", on_events=["graph:run"], input_validator=AgentNodeRunRequest
)
class ScrapFlow:
    counter: int = 0
    graph: StateGraph | None

    @wfapp.step(timeout="20m", retries=2)
    async def graph_entry(self, hatctx: Context):
        # Define the configuration for the scraping pipeline
        graph_config = {
            "llm": {
                "api_key": "YOUR_OPENAI_APIKEY",
                "model": "openai/gpt-4o-mini",
            },
            "verbose": True,
            "headless": False,
        }

        # Create the SmartScraperGraph instance
        smart_scraper_graph = SmartScraperGraph(
            prompt="Extract me all the news from the website",
            source="https://www.wired.com",
            config=graph_config,
        )

        # Run the pipeline
        result = smart_scraper_graph.run()
        print(json.dumps(result, indent=4))
