from typing import Sequence, Any, Union, Optional
"""
Duck-typed function that safely returns the first element of a list
"""


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of the list if it exists
    """
    if lst:
        return lst[0]
    else:
        return None
