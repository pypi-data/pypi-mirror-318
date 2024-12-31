import requests
import typer
from typing_extensions import Annotated

from .errors import InvalidCoinError, InvalidCurrencyError, ERROR_MESSAGES


app = typer.Typer()


CG_BASE_URL = "https://api.coingecko.com/api/v3/"


@app.command()
def get_price(
    ids: Annotated[str, typer.Argument(help="Valid token name in full e.g Bitcoin")],
    vs_currencies: str = typer.Option(
        "USD", "-f", "--fiat", help="Valid fiat currency e.g EUR", show_default=True
    )
  ):
    """
    cpfeed (short for Crypto Price Feed) is a Python package for fetching cryptocurrency prices from the CoinGecko API.
    """
    token_name, fiat_currency = ids.lower().strip(), vs_currencies.lower().strip()
    price_url = f'{CG_BASE_URL}/simple/price?ids={token_name}&vs_currencies={fiat_currency}'

    try:
        response = requests.get(price_url)
        response.raise_for_status()

        data = response.json()

        if token_name not in data:
            raise InvalidCoinError(f'Invalid coin ID: {token_name}')
        if fiat_currency not in data[token_name]:
            raise InvalidCurrencyError(f'Invalid fiat_currency: {fiat_currency}')

        price = data[token_name][fiat_currency]
        typer.echo(f'The price of {token_name.title()} in {fiat_currency.upper()} is {price:,}')

    except requests.exceptions.HTTPError as http_err:
        status_code = http_err.response.status_code
        if status_code in ERROR_MESSAGES:
            typer.echo(ERROR_MESSAGES[status_code])
            raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(e)
        raise typer.Exit(code=1)


def main():
    app()
