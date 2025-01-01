from .strategy_implementation import AdvancedChunkingStrategy, BasicChunkingStrategy
from .strategy_abs import ChunkingStrategy

class ChunkingStrategyFactory:
    def get_strategy(self, version: str) -> ChunkingStrategy:
        if version == "V1":
            return AdvancedChunkingStrategy()
        return BasicChunkingStrategy()
