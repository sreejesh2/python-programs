'''dictionary comprehension'''

def doller_to_rupee():
    """create a new dictionary"""
    price = {'Laptop': 10, 'mobile': 5, 'watch': 3,'keybord':1}

    """multiplyed the price and convert_to rupee
       convert_to rupee = one doller covert to indian rupee
       """
    convert_to_ruppe = 81.38
    n_price = {i: j*convert_to_ruppe for (i, j) in price.items()}
    return n_price
rc=doller_to_rupee()
print(rc)
