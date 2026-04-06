"""
SHOPPING LIST
>creatable list
>pre-made pantry
>ability to add to list
"""
class Shop():
    def __init__(self):
        """INITIALIZATION"""
        self.list=[]
        self.pantry=['spaghetti','jelly','peanut butter','bread','eggs']
    def makelist(self):
        """TAKING INPUT"""
        choice=''
        while choice != 'done':
            choice=input('what do you need? (enter "done" when complete):')
            if choice=='done':pass
            else:self.list.append(str(choice).lower())
        """DISPLAYING WHAT YOU WANT, HAVE, AND NEED"""
        print("YOU WANT: ", end='')
        for item in self.list: print(str(item),end=', ')
        print("\nYOU HAVE: ", end='');
        for item in self.list:
            if item in self.pantry: print(item,end=', ')
        print("\nYOU NEED: ", end='')
        for item in self.list:
            if item not in self.pantry: print(item,end=', ')
shop=Shop()
shop.makelist()
