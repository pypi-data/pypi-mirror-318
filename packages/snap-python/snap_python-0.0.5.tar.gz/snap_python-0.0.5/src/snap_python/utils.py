from abc import ABC, abstractmethod

import httpx

from snap_python.schemas.changes import ChangesResponse


class AbstractSnapsClient(ABC):  # pragma: no cover
    @abstractmethod
    async def request(self) -> httpx.Response:
        pass

    @abstractmethod
    async def request_raw(self) -> httpx.Response:
        pass

    @abstractmethod
    async def get_changes_by_id(self, change_id: str) -> ChangesResponse:
        pass


def going_to_reload_daemon(changes: ChangesResponse | None) -> bool:
    if changes is None or not isinstance(changes, ChangesResponse):
        return False

    if changes.maintenance and changes.maintenance.kind in [
        "daemon-reload",
        "daemon-restart",
    ]:
        return True

    return False
