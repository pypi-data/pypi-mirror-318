import re
from typing import Any

from bs4 import BeautifulSoup
from urllib.parse import quote, unquote, urlparse, urlunparse
import markdownify
import httpx


BANNED_CLASSES = set(
    [
        "flagicon",
        "metadata",
        "reference",
        "pcs-collapse-table-icon",
        "reflist",
        "pcs-collapse-table-collapsed-container",
        "pcs-collapse-table-collapsed-bottom",
    ]
)
BANNED_LINK_TEXT = set(["Edit this at Wikidata"])

"""
Adapted from: https://github.com/microsoft/markitdown/blob/main/src/markitdown/_markitdown.py
Which is MIT licensed.
"""


class _CustomMarkdownify(markdownify.MarkdownConverter):
    """
    A custom version of markdownify's MarkdownConverter. Changes include:

    - Altering the default heading style to use '#', '##', etc.
    - Removing javascript hyperlinks.
    - Truncating images with large data:uri sources.
    - Ensuring URIs are properly escaped, and do not conflict with Markdown syntax
    """

    def __init__(self, **options: Any):
        options["heading_style"] = options.get("heading_style", markdownify.ATX)
        options["strip_links"] = options.get("strip_links", True)
        options["keep_inline_images_in"] = options.get(
            "keep_inline_images_in", ["div", "span"]
        )
        # Explicitly cast options to the expected type if necessary
        super().__init__(**options)

    def _convert_hn(self, n: int, el: Any, text: str, convert_as_inline: bool) -> str:
        """Same as usual, but be sure to start with a new line"""
        if not convert_as_inline:
            if not re.search(r"^\n", text):
                return "\n" + super()._convert_hn(n, el, text, convert_as_inline)  # type: ignore

        return super()._convert_hn(n, el, text, convert_as_inline)  # type: ignore

    def convert_a(self, el: Any, text: str, convert_as_inline: bool):
        """Same as usual converter, but removes Javascript links and escapes URIs."""
        prefix, suffix, text = markdownify.chomp(text)  # type: ignore
        if not text:
            return ""
        href = el.get("href")
        title = el.get("title")

        if text in BANNED_LINK_TEXT or title in BANNED_LINK_TEXT:
            return ""

        # Escape URIs and skip non-http or file schemes
        if href:
            try:
                parsed_url = urlparse(href)  # type: ignore
                if parsed_url.scheme and parsed_url.scheme.lower() not in [
                    "http",
                    "https",
                    "file",
                ]:  # type: ignore
                    return "%s%s%s" % (prefix, text, suffix)
                href = urlunparse(
                    parsed_url._replace(path=quote(unquote(parsed_url.path)))
                )  # type: ignore
            except ValueError:  # It's not clear if this ever gets thrown
                return "%s%s%s" % (prefix, text, suffix)

        if self.options["strip_links"]:
            return "%s%s%s" % (prefix, text, suffix)

        # For the replacement see #29: text nodes underscores are escaped
        if (
            self.options["autolinks"]
            and text.replace(r"\_", "_") == href
            and not title
            and not self.options["default_title"]
        ):
            # Shortcut syntax
            return "<%s>" % href
        if self.options["default_title"] and not title:
            title = href
        title_part = ' "%s"' % title.replace('"', r"\"") if title else ""
        return (
            "%s[%s](%s%s)%s" % (prefix, text, href, title_part, suffix)
            if href
            else text
        )

    def convert_img(self, el: Any, text: str, convert_as_inline: bool) -> str:
        """Same as usual converter, but removes data URIs"""

        alt = el.attrs.get("alt", None) or ""
        src = el.attrs.get("src", None) or ""
        title = el.attrs.get("title", None) or ""
        title_part = ' "%s"' % title.replace('"', r"\"") if title else ""

        if (
            convert_as_inline
            and el.parent.name not in self.options["keep_inline_images_in"]
        ):
            return alt

        # Remove dataURIs
        if src.startswith("data:"):
            src = src.split(",")[0] + "..."

        return "![%s](%s%s)" % (alt, src, title_part)

    def _banned_element(self, el: Any) -> bool:
        return "class" in el.attrs and any(
            cls in BANNED_CLASSES for cls in el.attrs["class"]
        )

    def convert_div(self, el: Any, text: str, convert_as_inline: bool) -> str:
        if self._banned_element(el):
            return ""

        return text

    def convert_figure(self, el: Any, text: str, convert_as_inline: bool) -> str:
        # we want to extract the image and caption
        # per the spec in https://www.mediawiki.org/wiki/Specs/HTML/2.8.0

        img_link = el.find("a")

        figcaption = el.find("figcaption")
        if img_link and figcaption:
            caption_text = self.convert_soup(figcaption)
            return f"![{caption_text}]({img_link.attrs.get('href', '')})"
        return ""

    def convert_sup(self, el: Any, text: str, convert_as_inline: bool) -> str:
        if self._banned_element(el):
            return ""

        return super().convert_sup(el, text, convert_as_inline)

    def convert_span(self, el: Any, text: str, convert_as_inline: bool) -> str:
        if self._banned_element(el):
            return ""

        return text

    def convert_soup(self, soup: Any) -> str:
        return super().convert_soup(soup)  # type: ignore


class WikipediaConverter:
    """Handle Wikipedia pages separately, focusing only on the main document content."""

    def convert(self, html: str, **kwargs: Any) -> str:
        soup = BeautifulSoup(html, "html.parser")

        body_elm = soup.find("div", {"id": "mw-content-text"})
        if body_elm is None:
            body_elm = soup.find("body", {"class": "mw-body-content"})
            if body_elm is None:
                body_elm = soup

        webpage_text = _CustomMarkdownify(**kwargs).convert_soup(body_elm)

        return webpage_text


BASE_URL = "https://{}.wikipedia.org/api/rest_v1/page/mobile-html"


async def get_wiki_mobile_html(client: httpx.AsyncClient, title: str, lang: str) -> str:
    # url encode title
    title = quote(title, safe="")

    # use the REST API to get the mobile version of the page
    LANG_BASE_URL = BASE_URL.format(lang)
    url = f"{LANG_BASE_URL}/{title}"
    try:
        response = await client.get(url)
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        # check for 301
        if e.response.status_code == 301 or e.response.status_code == 302:
            # get the new location
            new_title = unquote(e.response.headers["Location"])
            return await get_wiki_mobile_html(client, new_title, lang)
        else:
            raise
    return response.text
