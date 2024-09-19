MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
change = 0
machine_on = True  # 머신 상태
quarters = 0
dimes = 0
nickels = 0
pennies = 0

# 1. 커피 머신 자원 상태 출력
def show_state():
    print(f"""  
    water: {resources["water"]}
    milk: {resources["milk"]}
    coffee: {resources["coffee"]}
    """)

# 4. 자원 체크 함수
def check_resource(user_choice):
    ingredients = MENU[user_choice]["ingredients"]

    # 각 자원에 대한 충분한 자원이 있는지 확인
    if (resources["water"] >= ingredients.get("water", 0) and
            resources["milk"] >= ingredients.get("milk", 0) and
            resources["coffee"] >= ingredients["coffee"]):
        return True
    else:
        return False

# 5. 자원 사용 후 업데이트
def update_resources(user_choice):
    ingredients = MENU[user_choice]["ingredients"]
    resources["water"] -= ingredients.get("water", 0)
    resources["milk"] -= ingredients.get("milk", 0)
    resources["coffee"] -= ingredients["coffee"]

# 6. 금액 체크 함수
def check_money(user_choice, quarters, dimes, nickels, pennies):
    price = MENU[user_choice]["cost"]
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    # 총 금액이 음료 가격보다 많은지 확인
    if total >= price:
        change = total - price
        print(f"Here is ${round(change, 2)} in change.")
        print(f"Here is your {user_choice}. Enjoy! ")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

# 커피 머신 루프
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        machine_on = False
        print("Coffee machine is turned off.")
    elif user_choice in MENU:
        if check_resource(user_choice):
            print(f"{user_choice} costs ${MENU[user_choice]['cost']}. Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            if check_money(user_choice, quarters, dimes, nickels, pennies):
                update_resources(user_choice)
                show_state()  # 자원 상태 출력
        else:
            print("Sorry, there are not enough resources.")
    else:
        print("Invalid choice, please try again.")
