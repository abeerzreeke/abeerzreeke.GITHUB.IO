from typing import Dict

def main():
    # This loop terminates when user select 2.EXIT option when asked
    # in try it will ask user for an option as an integer (1 or 2)
    # if correct then proceed else continue asking options
    total_price = 0

    while True:
        try:
            ch = int(input("1.CHOOSE PRODUCT\n2.EXIT\nEnter your choice : "))
        except ValueError:
            print("\nERROR: Choose only digits from the given option")
            continue
        else:
            # check the option selected
            # by user is 1 i.e. to buy an item
            if ch == 1:
                product = input("Enter product name : ")
                products = convertTextFileToDict("items.txt")
                if product in products:
                    product_price = int(products.get(product))
                    print(f"you choose {product} with price {product_price}")
                    total_price += product_price
                else:
                    print("item not found")
            elif ch == 2:
                try:
                    fed = int(input("You wants to submit a review of the supermarket\n 1.Yes\n2.No\nEnter your choice :"))
                except ValueError:
                    print("\nERROR: Choose only 1-Yes/2-No")
                    continue
                else:
                    if fed != 1 and fed != 2:
                        print("Error Choose only 1-Yes/2-No")
                        break
                    elif fed == 1:
                        reviews = ["Propose new items please", "Submit a comment please", "Rate the supermarket out of 5 please "]
                        review = int(input("1.Propose new items\n2.Submit a comment\n3.Rate the supermarket out of 5\nEnter your choice : "))
                        print(reviews[review-1])
                        break
                    else:
                        print(f"you total price is {total_price}")
                        break

#function to convert texe file to dict
def convertTextFileToDict(fileName: str) -> Dict:
    productsDict = {}
    with open(fileName, 'r') as products:
        for product in products:
            k, v = product.strip().split('-')
            productsDict[k] = v

    return productsDict


if __name__ == '__main__':
    main()

