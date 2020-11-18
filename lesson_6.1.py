coin = ('Bitcoin', 'Ether', 'Ripple', 'Litecoin')
code = ('BTC', 'ETH', 'XRP', 'LTC')

def coin_code(c1, c2):
    return dict(zip(c1, c2))
    

print(coin_code(coin, code))
