import json

import structlog
from langgraph.graph import StateGraph
from mtmaisdk.clients.rest.models import AgentNodeRunRequest
from mtmaisdk.context.context import Context
from scrapegraphai.graphs import SmartScraperGraph

from mtmai.workflows.worker import wfapp

LOG = structlog.get_logger()


@wfapp.workflow(
    name="scrape", on_events=["scrape:run"], input_validator=AgentNodeRunRequest
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
