import random

MAX_LINES = 3
balance = None
lines = None
bet = None

COLS = 3

symbols = {
    "A": 3,
    "B": 4,
    "C": 6,
    "D": 7,
}

values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def checkwins(columns):
    winnings = 0;
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol]*bet

    return winnings
def getslotmachinespin():
    all_symbols =[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            #print(all_symbols)

    columns=[]
    for _ in range(COLS):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(lines):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def printslots(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) -1:
                print("\033[33m"+column[row], end=" | ")
            else:
                print("\033[33m"+column[row], end="")
        print()

def deposit():
    while True:
        global balance
        balance = input("\033[36mDeposit $$ ")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print("Enter more than 0")
        else:
            print("Enter a number")


def setlines():
    while True:
        global lines
        lines = input(f"How many lines max is {MAX_LINES}. ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number ")
        else:
            print("Enter a number")

def setbet():
    while True:
        global bet
        bet = input("Bet per line? ")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                break
            else:
                print("Bet more than $0 ")
        else:
            print("Enter a real number ")

def checkbet():
    while True:
        setbet()
        totalbet=bet*lines

        if totalbet > balance:
            print(f"Your balance isn't enough you have ${balance}")
        else: break

def confirm():
    answer = input(f"Total bet: ${bet*lines} \"change\" ")
    if (answer == "change"):
        setlines()
        checkbet()
        confirm()
        print(balance,lines,bet)

def playagain():
    global balance
    if(balance==0):
        print("\033[31mYOU LOSE")
        main()
    setlines()
    checkbet()
    confirm()
    balance -= bet * lines
    currentroll = getslotmachinespin()
    printslots(currentroll)
    winnings = checkwins(currentroll)
    balance += winnings
    print(f"\033[36mWinnings: {winnings}")
    print(f"\033[36mBalance: {balance}")
    playagain()

def main():
    deposit()
    playagain()

main()