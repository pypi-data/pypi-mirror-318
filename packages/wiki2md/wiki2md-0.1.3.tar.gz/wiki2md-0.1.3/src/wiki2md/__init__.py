from .html2md import get_wiki_mobile_html, WikipediaConverter
from httpx import AsyncClient


DEFAULT_USER_AGENT = (
    "wiki2md (https://gitlab.wikimedia.org/repos/future-audiences/wiki2md)"
)


async def wiki_to_markdown(
    title: str, lang: str = "en", client: AsyncClient | None = None
) -> str:
    """Converts a Wikipedia article to markdown."""

    # first get the HTML
    if not client:
        client = AsyncClient(headers={"User-Agent": DEFAULT_USER_AGENT})
    html = await get_wiki_mobile_html(client, title, lang)

    # then convert it to markdown
    converter = WikipediaConverter()
    return converter.convert(html)
