# type: ignore

import inspect
from typing import Any

from ..generator import display_none
from ..ui import INTERACTION_TYPE, ComponentReturn
from .find_component import FindComponent
from .validate import validate_static_layout
from .diff import diff_static_layouts
from .manage_submit_button import manage_layout_form_submit_button


class _StaticTree:
    """
    _StaticTree is a class that provides methods for working with static layouts.
    """

    @property
    def find_component(self):
        return FindComponent

    @property
    def diff(self):
        return diff_static_layouts

    @property
    def validate(self):
        return validate_static_layout

    @staticmethod
    def generate(layout: Any, resolver: Any) -> ComponentReturn:
        """
        Generates a static layout from a layout.
        """
        executed = None

        if callable(layout):
            layout_params = inspect.signature(layout).parameters
            kwargs = {}
            if "resolve" in layout_params:
                kwargs["resolve"] = resolver
            executed = layout(**kwargs)
        else:
            executed = layout

        if executed is None:
            return display_none()

        processed = manage_layout_form_submit_button(executed)

        return processed

    @staticmethod
    def without_ids(static_layout):
        """
        Removes the IDs from a static layout.
        """
        new_layout = static_layout.copy()

        new_layout["model"] = new_layout["model"].copy()
        new_layout["model"]["id"] = None

        if new_layout["interactionType"] == INTERACTION_TYPE.LAYOUT:
            new_layout["model"]["children"] = [
                _StaticTree.without_ids(child)
                for child in new_layout["model"]["children"]
            ]

        return new_layout


StaticTree = _StaticTree()
