from typing import Any, List

def chunk(input_list: List[Any], chunk_size: int) -> List[List[Any]]:
    """Split a list into chunks of the specified size."""
    chunks = []
    for i in range(0, len(input_list), chunk_size):
        chunks.append(input_list[i : i + chunk_size])
    return chunks