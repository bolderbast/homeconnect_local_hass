"""Helper functions."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import HCData
    from .entity import HCEntity


def create_entities(
    entities_classes: dict[str, type[HCEntity]], runtime_data: HCData
) -> set[HCEntity]:
    """Create entities from entity_descriptions."""
    entities = set()
    for entity_key, entity_class in entities_classes.items():
        if entity_key in runtime_data.available_entity_descriptions:
            for entity_description in runtime_data.available_entity_descriptions[entity_key]:
                entities.add(
                    entity_class(
                        entity_description=entity_description,
                        appliance=runtime_data.appliance,
                        device_info=runtime_data.device_info,
                    )
                )
    return entities
