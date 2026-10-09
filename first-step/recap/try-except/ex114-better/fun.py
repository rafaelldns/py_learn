import requests

def test(url):
    try:
        res = requests.get(url)
    except requests.ConnectionError:
        print('\033[0;31mThe site is offline or doesnt exist!\033[m')
    else:
        print('\033[0;32mThe site is opened and working in this PC!\033[m')

        