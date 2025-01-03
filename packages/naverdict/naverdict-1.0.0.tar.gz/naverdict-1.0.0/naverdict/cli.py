import click
from naverdict.search import search


@click.command()
@click.argument("search_word", nargs=1, default="하다")
def main(search_word):
    """Quick CLI for scraping Naver's English-Korean dictionary.

    Usage:
        python cli_naver_dict.py [SEARCH_WORD]

    Example:
        python cli_naver_dict.py 하다
    """
    results = search(search_word)
    for item in results:
        click.echo(item)


if __name__ == "__main__":
    main()
