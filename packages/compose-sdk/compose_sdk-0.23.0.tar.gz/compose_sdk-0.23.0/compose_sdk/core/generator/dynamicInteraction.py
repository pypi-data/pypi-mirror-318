from typing import Union, Any
from .displayInteraction import display_none
from ..ui import ComponentReturn


def dynamic_cond(
    condition: Any,
    *,
    true: Union[ComponentReturn, None] = None,
    false: Union[ComponentReturn, None] = None
) -> ComponentReturn:
    """
    Conditionally displays a component based on a condition. Conditions are evaluated for truthiness.

    ## Documentation
    https://docs.composehq.com/components/dynamic/if-else

    ## Parameters
    #### condition
        - `Any`
        - Required
        - The condition to evaluate. The condition will be evaluated for truthiness.
    #### true
        - `Component`
        - Optional
        - The component to display if the condition is truthy. Will display nothing if not provided.
    #### false
        - `Component`
        - Optional
        - The component to display if the condition is falsey. Will display nothing if not provided.

    ## Returns
    The configured component.

    ## Example
    >>> page.add(lambda: ui.cond(
    ...     3 > 2,
    ...     true=ui.text("This is true"),
    ...     false=ui.text("This is false"),
    ... ))
    """
    if condition:
        if true is None:
            return display_none()
        return true
    else:
        if false is None:
            return display_none()
        return false
