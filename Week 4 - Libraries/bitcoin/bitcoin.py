# Jesus Carlos Martinez Gonzalez
# 13/05/2023
# Bitcoin Price Index

import sys
import requests


def main():

    # Validate command-line argument
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        amount = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

    # Get data from coindesk's API
    try:
        price = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()['bpi']['USD']['rate_float']
    except requests.RequestException:
        sys.exit("Something went wrong")

    # Print total price of requested info
    total = price * amount
    print(f'${total:,.4f}')


if __name__ == '__main__':
    main()