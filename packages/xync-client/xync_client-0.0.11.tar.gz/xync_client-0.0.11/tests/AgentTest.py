import pytest
from xync_schema.enums import ExStatus
from xync_schema.models import Ex

from xync_client.Abc.BaseTest import BaseTest
from xync_client.Abc.Agent import BaseAgentClient
from xync_client.Abc.Base import BaseClient


class AgentTest(BaseTest):
    @pytest.fixture(scope="class", autouse=True)
    async def clients(self) -> list[BaseClient]:
        exs = await Ex.filter(status__gt=ExStatus.plan).prefetch_related("agents")
        clients: list[BaseAgentClient] = [[ag for ag in ex.agents if ag.auth].pop().client() for ex in exs]
        yield clients
        [await cl.close() for cl in clients]
