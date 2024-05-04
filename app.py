
from time import sleep


def exit(): 
    print('Okay, exiting...')
    sleep(2)
    print('Program closed!')

def shoppingListUX(): 
    while True: 
        var_choice = str(input('Would you like to use the shopping list? [Y/N]: '))

        if var_choice.upper() == 'Y':
            list_shopping = []

            while True: 
                try: 
                    var_product_name = str(input('Enter the product name: '))
                    var_price = float(input('Enter the product price: '))

                    list_shopping.append((var_product_name, var_price))

                    add_more = str(input('Would you like to add more? [Y/N]: '))

                    if add_more.upper() == 'N': 
                        break
                except ValueError: 
                    print('Invalid input: please try again!')
            
            print('---- Shopping List ----')
            for product_name, price in list_shopping: 
                print(f'{product_name}: ${price:.2f}')
        elif var_choice.upper() == 'N': 
            exit()
            break
        else: 
            print(f'Error001: Invalid choice!')
if __name__ == '__main__': 
    shoppingListUX()