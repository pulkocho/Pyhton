from data import MENU, resources


def reporte():
    """Imprime en pantalla el reporte de los insumos"""
    for resource in resources:
        print(f'{resource} : {resources[resource]}')


def solicitar_pago(cost):
    """Recibe el costo y solicita el pago y hace la comparación para verificar
    si el pago es suficiente y regresa el cambio"""
    is_billed = False
    quarters = float(input("Qty of quarter?: ")) * 0.25
    dimes = float(input("Qty of dimes?: ")) * 0.1
    nickles = float(input("Qty of nickles?: ")) * .05
    pennies = float(input("Qty of pennies?: ")) * .01
    amount = quarters + dimes + nickles + pennies
    if amount >= cost:
        resources["Money"] += cost
        change = amount - cost
        if change > 0:
            print(f'Here is ${round(change, 2)} dollars in change.')
        is_billed = True
    else:
        print("Sorry that's not enough money. Money refunded.")
    return is_billed


def resource_verify(ingredients):
    """Verifica que los insumos sean suficientes para hacer el caffe"""
    is_enough = True
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            is_enough = False
    return is_enough


def dispensar(drink):
    """Sirve el cafe, verificar que existan todos los ingredientes"""

    for ingredient in MENU[drink]["ingredients"]:
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    print(f'Here is your {drink}. Enjoy! ☕')


def servir(drink):
    if drink in MENU:
        if resource_verify(MENU[drink]["ingredients"]):
            print(f'{drink} cost ${MENU[drink]["cost"]}')
            if solicitar_pago(MENU[drink]["cost"]):
                dispensar(drink)
    else:
        print(f"Sorry!, I don`t have this option. {drink}")


def atender(option):
    if option == "report":
        reporte()
    elif option == "off":
        return False
    else:
        servir(option)
    return True


resources["Money"] = 0

machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    machine_on = atender(choice)
