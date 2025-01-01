import csv
import time
from typing import List, Optional

from . import log
from . import plugins
from .plugins.Anime import Anime


class AniSearch:
    def __init__(self, plugin_name: str = 'dmhy', parser: str = None, verify: bool = None, timefmt: str = None):
        """
        Initialize AniSearch object.

        Args:
        - plugin_name: Name of the plugin, default is 'dmhy'
        - parser: Name of the parser
        - verify: Whether to verify
        - timefmt: Time format
        """
        self.reset()
        self._timefmt = None
        self.plugin = self._load_plugin(plugin_name, parser, verify, timefmt)
        log.debug("New search object created.")

    def _load_plugin(self, plugin_name, parser, verify, timefmt):
        kwargs = {}
        if parser is not None:
            kwargs['parser'] = parser
        if verify is not None:
            kwargs['verify'] = verify
        if timefmt is not None:
            self.set_timefmt(timefmt)
            kwargs['timefmt'] = self._timefmt

        try:
            plugin = plugins.get_plugin(plugin_name)(**kwargs)
            log.debug(f"Successfully loaded plugin: {plugin_name}")
            return plugin
        except (ImportError, AttributeError) as e:
            log.error(f"Failed to load plugin {plugin_name}: {str(e)}")
            raise

    def set_timefmt(self, timefmt: str) -> None:
        """
        Set and validate the time format.

        Args:
        - timefmt: Time format string
        """
        time.strftime(timefmt, time.localtime())
        self._timefmt = timefmt

    def reset(self) -> None:
        """Reset the search object."""
        self.animes: List[Anime] = []
        self.anime: Optional[Anime] = None
        self.if_selected: Optional[bool] = False

    def search(self, keyword: str, collected: Optional[bool] = None, proxies: Optional[dict] = None,
           system_proxy: Optional[bool] = None, **extra_options) -> bool:
        """
        Search for anime using the given keyword.

        Args:
        - keyword: Search keyword
        - collected: Whether to collect results
        - proxies: Proxy settings
        - system_proxy: Whether to use system proxy

        Returns:
        - True if search is successful, False otherwise.
        """
        self.reset()

        # 使用过滤条件减少不必要的计算
        kwargs = {'keyword': keyword}
        if collected is not None:
            kwargs['collected'] = collected
        if proxies:
            kwargs['proxies'] = proxies
        if system_proxy:
            kwargs['system_proxy'] = system_proxy
        kwargs.update(extra_options)

        try:
            self.animes = self.plugin.search(**kwargs)

            log.info(f"This search is complete: {keyword}")
            return True

        except Exception as e:
            log.error(f"Search failed: {str(e)}")
            return False


    def select(self, index: int) -> None:
        """
        Select an anime from the search results.

        Args:
        - index: Index of the anime in the results list
        """
        if not (0 <= index < len(self.animes)):
            raise IndexError("Invalid selection index")
        self.anime = self.animes[index]
        self.if_selected = True

    def size_format(self, unit: str = 'MB') -> None:
        """
        Convert the size of the selected anime to the specified unit.

        Args:
        - unit: Target size unit, default is 'MB'
        """
        if not self.if_selected:
            raise ValueError("No item selected. Please use select() method first.")

        self.anime.size_format(unit)

    def save_csv(self, filename: str) -> None:
        """
        Save the selected anime details to a CSV file.

        Args:
        - filename: Name of the CSV file
        """
        fieldnames = ["time", "title", "size", "magnet"]

        try:
            with open(filename, mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()

                for anime in self.animes:
                    writer.writerow({
                        "time": anime.time,
                        "title": anime.title,
                        "size": anime.size,
                        "magnet": anime.magnet
                    })

        except Exception as e:
            log.error(f"Failed to save CSV: {str(e)}")
            raise


if __name__ == "__main__":
    import doctest

    doctest.testmod()
