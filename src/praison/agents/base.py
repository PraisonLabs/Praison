# cleanup imports and fix typing
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from praison.memory import AgentMemory
    from praison.tools import ToolRegistry
