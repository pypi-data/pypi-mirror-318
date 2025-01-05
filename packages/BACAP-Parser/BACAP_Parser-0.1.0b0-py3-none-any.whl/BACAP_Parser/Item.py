from typing import Literal

from autoslot import Slots

from .ExtendedDict import ExtendedDict
from .Color import Color



class Item(Slots):
    def __init__(self, /, item_data: ExtendedDict[str, str | dict | list] = None,
                 *, item_id: str = None, components: ExtendedDict[str, str | ExtendedDict | list] = None) -> None:
        if item_data is None and item_id is None:
            raise ValueError("Either 'item_data' must be provided or both 'item_id' and 'components' must be specified.")

        if item_data:
            item_id = item_data["id"]
            components = item_data.get("components")

        self._id = item_id
        self._components = components or ExtendedDict()

    @property
    def id(self) -> str:
        return self._id

    @property
    def components(self) -> dict | None:
        return self._components

    @property
    def enchantments(self) -> dict | None:
        return self.components.get("enchantments")

    @property
    def has_enchantment_glint(self) -> bool:
        enchantment_glint_override = self._components.get_with_multiple_values("minecraft:enchantment_glint_override", "enchantment_glint_override")
        if enchantment_glint_override is not None:
            return True
        else:
            return bool(self._components.get("enchantments", False))

    def __repr__(self):
        return f"{self.__class__.__name__}({self._id})"

    def __str__(self):
        return self.__repr__()


class RewardItem(Item):
    def __init__(self, item_id: str, components: ExtendedDict[str, str | dict | list] | None, item_type: Literal['item', 'block'], amount: str | int | None = 1) -> None:
        super().__init__(item_id=item_id, components=components)

        if item_type not in ["item", "block"]:
            raise ValueError("item_type must be either item or block")

        self._type = item_type
        self._amount = int(amount)

    @property
    def type(self) -> str:
        return self._type

    @property
    def amount(self) -> int:
        return self._amount

    def __repr__(self):
        return f"{self.__class__.__name__}(item:{self._id}, amount:{self._amount}, type:{self.type})"

    def __str__(self):
        return self.__repr__()


class TrophyItem(Item):
    def __init__(self, item_id: str, components: ExtendedDict[str, str | dict | list], name: str, color: Color, description: str) -> None:
        super().__init__(item_id=item_id, components=components)
        self._name = name
        self._color = color
        self._description = description

    @property
    def name(self) -> str:
        return self._name

    @property
    def color(self) -> Color:
        return self._color

    @property
    def description(self) -> str:
        return self._description

    def __repr__(self):
        return f"{self.__class__.__name__}(item:{self._id}, name:{self._name})"

    def __str__(self):
        return self.__repr__()