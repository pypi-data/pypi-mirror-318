from w3lib.url import url_query_cleaner

from .base import UrlProcessorBase


class QueryRemovalProcessor(UrlProcessorBase):
    def validate_args(self) -> None:
        for arg in self.args:
            if not isinstance(arg, str):
                raise TypeError(
                    f"queryRemoval args must be strings, not {type(arg)}: {arg}"
                )

    def process(self, input_url: str) -> str:
        return url_query_cleaner(
            input_url, self.args, remove=True, unique=False, keep_fragments=True
        )
