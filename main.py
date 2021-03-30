import urllib.request
from termcolor import colored

stores = {
    181: 'Denver, CO',
    191: 'Overland Park, KS',
}

cards_to_search = {
    3080: 'Nvidia RTX 3080',
    3090: 'Nvidia RTX 3090',
}


def fetch_cards(store_id, rtx_number):
    url = f'https://www.microcenter.com/search/search_results.aspx?Ntt=rtx+{rtx_number}&searchButton=search&storeid={store_id}'
    with urllib.request.urlopen(url) as response:
        content = str(response.read())
        if content.find('limitNoSale') > 0:
            print(colored(f'{stores[store_id]} might have {cards_to_search[rtx_number]} in stock! =D', 'green'))
            print(colored(f'{url}', 'blue'))
        else:
            print(
                colored(f'{stores[store_id]} does not appear to have {cards_to_search[rtx_number]} in stock :(', 'red'))


if __name__ == '__main__':
    for store in stores:
        for card in cards_to_search:
            fetch_cards(store, card)
