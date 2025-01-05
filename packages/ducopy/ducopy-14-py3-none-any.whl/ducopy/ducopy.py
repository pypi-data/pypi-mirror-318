from ducopy.rest.client import APIClient
from ducopy.rest.models import (
    NodesResponse,
    NodeInfo,
    ConfigNodeResponse,
    ActionsResponse,
    ConfigNodeRequest,
    NodesInfoResponse,
)
from pydantic import HttpUrl


class DucoPy:
    def __init__(self, base_url: HttpUrl, verify: bool = True) -> None:
        self.client = APIClient(base_url, verify)

    def raw_get(self, endpoint: str, params: dict = None) -> dict:
        return self.client.raw_get(endpoint=endpoint, params=params)

    def update_config_node(self, node_id: int, config: ConfigNodeRequest) -> ConfigNodeResponse:
        return self.client.patch_config_node(node_id=node_id, config=config)

    def get_api_info(self) -> dict:
        return self.client.get_api_info()

    def get_info(self, module: str | None = None, submodule: str | None = None, parameter: str | None = None) -> dict:
        return self.client.get_info(module=module, submodule=submodule, parameter=parameter)

    def get_nodes(self) -> NodesInfoResponse:
        return self.client.get_nodes()

    def get_node_info(self, node_id: int) -> NodeInfo:
        return self.client.get_node_info(node_id=node_id)

    def get_config_node(self, node_id: int) -> ConfigNodeResponse:
        return self.client.get_config_node(node_id=node_id)

    def get_config_nodes(self) -> NodesResponse:
        return self.client.get_config_nodes()

    def get_action(self, action: str | None = None) -> dict:
        return self.client.get_action(action=action)

    def get_actions_node(self, node_id: int, action: str | None = None) -> ActionsResponse:
        return self.client.get_actions_node(node_id=node_id, action=action)

    def get_logs(self) -> dict:
        return self.client.get_logs()

    def close(self) -> None:
        self.client.close()
