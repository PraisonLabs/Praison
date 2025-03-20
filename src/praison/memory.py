"""
Shared memory module for multi-agent collaboration.
Provides both short-term working memory and long-term persistent storage.
"""

from typing import Any, Dict, List, Optional

class AgentMemory:
    def __init__(self):
        self._short_term: Dict[str, Any] = {}
        self._long_term: List[Dict] = []
    
    def store(self, key: str, value: Any, persist: bool = False):
        self._short_term[key] = value
        if persist:
            self._long_term.append({'key': key, 'value': value})
    
    def recall(self, key: str) -> Optional[Any]:
        return self._short_term.get(key)
    
    def search_history(self, query: str) -> List[Dict]:
        return [m for m in self._long_term if query.lower() in str(m).lower()]
