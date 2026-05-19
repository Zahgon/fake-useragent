"""Fake User Agent retriever."""

import random
from collections.abc import Iterable
from typing import Any, Optional, Union

from fake_useragent.log import logger
from fake_useragent.utils import BrowserUserAgentData, load


def _ensure_iterable(
    *, default: Iterable[str], **kwarg: Optional[Iterable[str]]
) -> list[str]:
    """Ensure the given value is an Iterable and convert it to a list.

    Args:
        default (Iterable[str]): Default iterable to use if value is `None`.
        **kwarg (Optional[Iterable[str]]): A single keyword argument containing the value to check
            and convert.

    Raises:
        ValueError: If more than one keyword argument is provided.
        TypeError: If the value is not None, not a str, and not iterable.

    Returns:
        list[str]: A list containing the items from the iterable.
    """
    pass


def _ensure_float(value: Any) -> float:
    """Ensure the given value is a float.

    Args:
        value (Any): The value to check and convert.

    Raises:
        ValueError: If the value is not a float.

    Returns:
        float: The float value.
    """
    pass


def _is_magic_name(attribute_name: str) -> bool:
    """Judge whether the given attribute name is the name of a magic method(e.g. __iter__).

    Args:
        attribute_name (str): The attribute name to check.

    Returns:
        bool: Whether the given attribute name is magic.
    """
    pass


class FakeUserAgent:
    """Fake User Agent retriever.

    Args:
        browsers (Optional[Iterable[str]], optional): If given, will only ever return user agents
            from these browsers. If None, set to:
            `["Google", "Chrome", "Firefox", "Edge", "Opera"," Safari", "Android", "Yandex Browser", "Samsung Internet", "Opera Mobile",
              "Mobile Safari", "Firefox Mobile", "Firefox iOS", "Chrome Mobile", "Chrome Mobile iOS", "Mobile Safari UI/WKWebView",
              "Edge Mobile", "DuckDuckGo Mobile", "MiuiBrowser", "Whale", "Twitter", "Facebook", "Amazon Silk"]`.
            Defaults to None.
        os (Optional[Iterable[str]], optional): If given, will only ever return user agents from
            these operating systems. If None, set to `["Windows", "Linux", "Ubuntu", "Chrome OS", "Mac OS X", "Android","iOS"]`. Defaults to
            None.
        min_version (float, optional): Will only ever return user agents with versions greater than
            this one. Defaults to 0.0.
        min_percentage (float, optional): Filter user agents based on usage.
            Defaults to 0.0.
        platforms (Optional[Iterable[str]], optional): If given, will only return the user-agents with
            the provided platform type. If None, set to `["desktop", "mobile", "tablet"]`. Defaults to None.
        fallback (str, optional): User agent to use if there are any issues retrieving a user agent.
            Defaults to `"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like
            Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"`.
        safe_attrs (Optional[Iterable[str]], optional): `FakeUserAgent` uses a custom `__getattr__`
            to facilitate retrieval of user agents by browser. If you need to prevent some
            attributes from being treated as browsers, pass them here. If None, all attributes will
            be treated as browsers. Defaults to ["shape"] to prevent unintended calls in IDEs like PyCharm.

    Raises:
        TypeError: If `fallback` isn't a `str` or `safe_attrs` contains non-`str` values.
    """

    def __init__(
        self,
        browsers: Optional[Iterable[str]] = None,
        os: Optional[Iterable[str]] = None,
        min_version: float = 0.0,
        min_percentage: float = 0.0,
        platforms: Optional[Iterable[str]] = None,
        fallback: str = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0"
        ),
        safe_attrs: Optional[Iterable[str]] = None,
    ):
        self.browsers = _ensure_iterable(
            browsers=browsers,
            default=[
                "Google",
                "Chrome",
                "Firefox",
                "Edge",
                "Opera",
                "Safari",
                "Android",
                "Yandex Browser",
                "Samsung Internet",
                "Opera Mobile",
                "Mobile Safari",
                "Firefox Mobile",
                "Firefox iOS",
                "Chrome Mobile",
                "Chrome Mobile iOS",
                "Mobile Safari UI/WKWebView",
                "Edge Mobile",
                "DuckDuckGo Mobile",
                "MiuiBrowser",
                "Whale",
                "Twitter",
                "Facebook",
                "Amazon Silk",
            ],
        )

        self.os = _ensure_iterable(
            os=os,
            default=[
                "Windows",
                "Linux",
                "Ubuntu",
                "Chrome OS",
                "Mac OS X",
                "Android",
                "iOS",
            ],
        )
        self.min_percentage = _ensure_float(min_percentage)
        self.min_version = _ensure_float(min_version)

        self.platforms = _ensure_iterable(
            platforms=platforms, default=["desktop", "mobile", "tablet"]
        )

        if not isinstance(fallback, str):
            msg = f"fallback must be a str but got {type(fallback).__name__}."
            raise TypeError(msg)
        self.fallback = fallback

        if safe_attrs is None:
            safe_attrs = ["shape"]
        safe_attrs = _ensure_iterable(safe_attrs=safe_attrs, default=set())
        str_safe_attrs = [isinstance(attr, str) for attr in safe_attrs]
        if not all(str_safe_attrs):
            bad_indices = [
                idx for idx, is_str in enumerate(str_safe_attrs) if not is_str
            ]
            msg = f"safe_attrs must be an iterable of str but indices {bad_indices} are not."
            raise TypeError(msg)
        self.safe_attrs = set(safe_attrs)

        # Next, load our local data file into memory (browsers.jsonl)
        self.data_browsers = load()

    def getBrowser(self, browsers: Union[str, list[str]]) -> BrowserUserAgentData:
        """Get a browser user agent based on the filters.

        Args:
            browsers (str): The browser name(s) to get. Special keyword "random" will return a random user-agent string.

        Returns:
            BrowserUserAgentData: The user agent with additional data.
        """
        pass

    def _filter_useragents(
        self, browsers_to_filter: Optional[Union[str, list[str]]] = None
    ) -> list[BrowserUserAgentData]:
        """Filter the user agents based on filters set in the instance, and an optional browser name.

        User agents from the data file are filtered based on the attributes passed upon
        instantiation.

        Args:
            browsers_to_filter (Union[str, None], optional): A specific browser name you want results for in
                this particular call. If None, don't apply extra filters. Defaults to None.

        Returns:
            list[BrowserUserAgentData]: A filtered list of user agents.
        """
        pass

    def __getitem__(self, attr: str) -> Union[str, Any]:
        """Get a user agent by key lookup, as if it were a dictionary (i.e., `ua['random']`).

        Args:
            attr (str): Browser name to get.

        Returns:
            Union[str, Any]: The user agent string if not a `self.safe_attr`, otherwise the
                attribute value.
        """
        return self.__getattr__(attr)

    def __getattr__(self, attr: Union[str, list[str]]) -> Union[str, Any]:
        """Get a user agent string by attribute lookup.

        Args:
            attr (str): Browser name to get. Special keyword "random" will return a user agent from
                any browser allowed by the instance's `self.browsers` filter.

        Returns:
            Union[str, Any]: The user agent string if not a `self.safe_attr`, otherwise the
                attribute value.
        """
        if isinstance(attr, str):
            if _is_magic_name(attr) or attr in self.safe_attrs:
                return super(UserAgent, self).__getattribute__(attr)
        elif isinstance(attr, list):
            for a in attr:
                if a in self.safe_attrs:
                    return super(UserAgent, self).__getattribute__(a)

        return self.getBrowser(attr)["useragent"]

    @property
    def chrome(self) -> str:
        """Get a random Chrome user agent."""
        pass

    @property
    def googlechrome(self) -> str:
        """Get a random Chrome user agent."""
        pass

    @property
    def ff(self) -> str:
        """Get a random Firefox user agent."""
        pass

    @property
    def firefox(self) -> str:
        """Get a random Firefox user agent."""
        pass

    @property
    def safari(self) -> str:
        """Get a random Safari user agent."""
        pass

    @property
    def opera(self) -> str:
        """Get a random Opera user agent."""
        pass

    @property
    def google(self) -> str:
        """Get a random Google user agent."""
        pass

    @property
    def edge(self) -> str:
        """Get a random Edge user agent."""
        pass

    @property
    def random(self) -> str:
        """Get a random user agent."""
        pass

    @property
    def getChrome(self) -> BrowserUserAgentData:
        """Get a random Chrome user agent, with additional data."""
        pass

    @property
    def getFirefox(self) -> BrowserUserAgentData:
        """Get a random Firefox user agent, with additional data."""
        pass

    @property
    def getSafari(self) -> BrowserUserAgentData:
        """Get a random Safari user agent, with additional data."""
        pass

    @property
    def getOpera(self) -> BrowserUserAgentData:
        """Get a random Safari user agent, with additional data."""
        pass

    @property
    def getGoogle(self) -> BrowserUserAgentData:
        """Get a random Google user agent, with additional data."""
        pass

    @property
    def getEdge(self) -> BrowserUserAgentData:
        """Get a random Edge user agent, with additional data."""
        pass

    @property
    def getRandom(self) -> BrowserUserAgentData:
        """Get a random user agent, with additional data."""
        pass


# common alias
UserAgent = FakeUserAgent
