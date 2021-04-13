from .base import Base
from .modification import Modification
from .. import chronicler, database


class Item(Base):
    """Represents an single item, such as a bat or armor"""
    @classmethod
    def _get_fields(cls):
        p = cls.load_one("aab9ce81-6fd4-439b-867c-a9da07b3e011")
        return [cls._from_api_conversion(x) for x in p.fields]

    @classmethod
    def load(cls, *ids):
        return [cls(item) for item in database.get_items(list(ids))]

    @classmethod
    def load_one(cls, id_):
        return cls.load(id_)[0]

    @classmethod
    def load_discipline(cls, *ids):
        """Load Pre-S15 Era Items (Bat & Armor slots)"""
        return [cls(item) for item in chronicler.get_old_items(list(ids))]

    @classmethod
    def load_one_discipline(cls, id_):
        if id_ is None:
            return cls({"id": id_, "name": "None?", "attr": "NONE"})
        if id_ == "":
            return cls({"id": id_, "name": "None", "attr": "NONE"})
        return cls.load_discipline(id_)[0]

    @Base.lazy_load("_attr_id", cache_name="_attr", use_default=False)
    def attr(self):
        """Pre-S15 Era Item Modifications (depreciated)"""
        return Modification.load_one(self._attr_id)

    @property
    def adjustments(self):
        if getattr(self, "root", None) is None:
            return []
        return self.root["adjustments"]