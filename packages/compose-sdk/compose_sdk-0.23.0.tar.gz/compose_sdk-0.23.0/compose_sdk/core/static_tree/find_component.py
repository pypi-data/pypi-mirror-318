# type: ignore

from typing import Union

from ..ui import INTERACTION_TYPE, TYPE, ComponentReturn


class FindComponent:
    @staticmethod
    def by_id(
        static_layout: ComponentReturn, component_id: str
    ) -> Union[ComponentReturn, None]:
        if static_layout["model"]["id"] == component_id:
            return static_layout

        if static_layout["interactionType"] == INTERACTION_TYPE.LAYOUT:
            children = (
                static_layout["model"]["children"]
                if isinstance(static_layout["model"]["children"], list)
                else [static_layout["model"]["children"]]
            )

            for child in children:
                found = FindComponent.by_id(child, component_id)
                if found is not None:
                    return found

        return None

    @staticmethod
    def by_type(
        static_layout: ComponentReturn, component_type: TYPE
    ) -> Union[ComponentReturn, None]:
        if static_layout["type"] == component_type:
            return static_layout

        if static_layout["interactionType"] == INTERACTION_TYPE.LAYOUT:
            children = (
                static_layout["model"]["children"]
                if isinstance(static_layout["model"]["children"], list)
                else [static_layout["model"]["children"]]
            )

            for child in children:
                found = FindComponent.by_type(child, component_type)
                if found is not None:
                    return found

        return None

    @staticmethod
    def by_interaction_type(
        static_layout: ComponentReturn, interaction_type: INTERACTION_TYPE
    ) -> Union[ComponentReturn, None]:
        if static_layout["interactionType"] == interaction_type:
            return static_layout

        if static_layout["interactionType"] == INTERACTION_TYPE.LAYOUT:
            children = (
                static_layout["model"]["children"]
                if isinstance(static_layout["model"]["children"], list)
                else [static_layout["model"]["children"]]
            )

            for child in children:
                found = FindComponent.by_interaction_type(child, interaction_type)
                if found is not None:
                    return found

        return None

    @staticmethod
    def count_by_type(static_layout: ComponentReturn, component_type: TYPE) -> int:
        count = 0

        if static_layout["type"] == component_type:
            count += 1

        if static_layout["interactionType"] == INTERACTION_TYPE.LAYOUT:
            children = (
                static_layout["model"]["children"]
                if isinstance(static_layout["model"]["children"], list)
                else [static_layout["model"]["children"]]
            )

            for child in children:
                count += FindComponent.count_by_type(child, component_type)

        return count
