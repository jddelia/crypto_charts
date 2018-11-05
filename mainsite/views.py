from django.shortcuts import render
import requests
import json

def index(request):
    return render(request, 'mainsite/index.html')

def btc(request):
    response_btc = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR')
    btc_data = json.loads(response_btc.text)

    context = {
        'btc_data': btc_data
    }
    return render(request, 'mainsite/btc.html', context)

def eth(request):
    response_eth = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR')
    eth_data = json.loads(response_eth.text)

    context = {
        'eth_data': eth_data
    }
    return render(request, 'mainsite/eth.html', context)

def ltc(request):
    response_ltc = requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,EUR')
    ltc_data = json.loads(response_ltc.text)

    context = {
        'ltc_data': ltc_data
    }
    return render(request, 'mainsite/ltc.html', context)

def contact(request):
    return render(request, 'mainsite/contact.html')
