from pipewine.item import CachedItem
from pipewine.mappers.base import Mapper
from pipewine.sample import Sample


class CacheMapper[T: Sample](Mapper[T, T]):
    def __call__(self, idx: int, x: T) -> T:
        return x.with_items(
            **{
                k: v if isinstance(v, CachedItem) else CachedItem(v)
                for k, v in x.items()
            }
        )
