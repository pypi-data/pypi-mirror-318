import modal.client
import typing
import typing_extensions

class ClusterInfo:
    rank: int
    container_ips: list[str]

    def __init__(self, rank: int, container_ips: list[str]) -> None: ...
    def __repr__(self): ...
    def __eq__(self, other): ...

def get_cluster_info() -> ClusterInfo: ...
async def _initialize_clustered_function(client: modal.client._Client, task_id: str, world_size: int): ...

class __initialize_clustered_function_spec(typing_extensions.Protocol):
    def __call__(self, client: modal.client.Client, task_id: str, world_size: int): ...
    async def aio(self, client: modal.client.Client, task_id: str, world_size: int): ...

initialize_clustered_function: __initialize_clustered_function_spec

cluster_info: typing.Optional[ClusterInfo]
