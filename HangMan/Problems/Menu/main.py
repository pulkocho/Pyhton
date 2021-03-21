food = input()
menu = ['pizza', 'salad', 'soup']
pizza = 'Margherita, Four Seasons, Neapolitan, Vegetarian, Spicy'
salad = 'Caesar salad, Green salad, Tuna salad, Fruit salad'
soup = 'Chicken soup, Ramen, Tomato soup, Mushroom cream soup'

if food in menu:
    if food in 'pizza':
        print(pizza)
    elif food in 'salad':
        print(salad)
    else:
        print(soup)
else:
    print("Sorry, we don't have it in the menu")