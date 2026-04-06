"""ANDREW CHURCH - ALLEN KRUEGER - CIS AM"""

def discount(cart=None):
    
    #taking input
    if type(cart) is not list:
        cart = input(
            "Enter a list of prices in your cart, divided by comma:"
            ).split(",")

        
    #converting numbers to int and splitting cart into sets
    split_cart = [ ]
    
    for i in range(len(cart)):
        
        if len(split_cart) < ((i//3)+1):
            split_cart.append([])
            
        split_cart[(i//3)].append(float(cart[i]))

    
    #figuring out total discount
    total_discounted = 0
    
    for chunk in split_cart:
        if len(chunk) == 3:
            total_discounted += min(chunk)   


    #figuring out a percent of the list
    total_discounted = (100-(100*(total_discounted/sum(cart))))/100
    print(total_discounted)


    #applying random list percent
    for i in range(len(cart)):
        cart[i] = round(cart[i]*total_discounted,2)
        

    #deleting values just in case
    del split_cart, total_discounted

    #output
    return cart
    
print(discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]))

"""OUTPUTS:
discount([2.99, 5.75, 3.35, 4.99]) -> [2.47, 4.74, 2.76, 4.12]
discount([10.75, 11.68]) -> [10.75, 11.68]
discount([68.74, 17.85, 55.99]) -> [60.13, 15.62, 48.98]
discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]) -> [5.16,
13.45, 33.06, 10.91, 22.71, 5.16, 5.16, 5.16]


"""
