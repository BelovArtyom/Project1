# Code below checks for float/integer/string of user input
def askfunc(questiontext):
    user_in = input(questiontext)
    try:
        # when a "." is detected, tries to turn it into a float
        if "." in user_in:
            return float(user_in)
        # else tries to turn the string input into an integer
        else:
            return int(user_in)
# if input is not float or int compatible, ValueError will appear. recurses function in the event of an incorrect answer
    except ValueError:
        print("ОШИБКА: Ввод должен быть числом.")
# function recurses onto itself, reusing the input it was originally called with until a satisfactory answer is received
        return askfunc(questiontext)


# message describing the purpose of the program
print("Водросль Спирогира распространяется по водоёму Байкал.\nПри помощи математической симуляции озера, вы можете предположить, сможет ли озеро Байкал быть очищенным от водросли Спирогира.")

# Lake Baikal is 23615.39 km cubed of water
baikalVolume = 23615.39
# amount of Lake Baikal currently polluted by spyrogyra in km cubed. has to be negative to enter while loop
amountpolluted = -1
# spyrogyra growth speed in km per day. technically can be negative and null
growthspeed = 0
# speed at which we're experminating spyrogyra in km per day. has to be negative to enter while loop
exterminationspeed = -1


# asking user for input on amount of volume polluted by spyrogyra at onset
while amountpolluted < 0:
    amountpolluted = askfunc("Какой объём озера Байкал загрязнена водрослью Спирогира? (км/куб)")
if amountpolluted < 0:
    print("ОШИБКА: объём загрязнения не может быть меньше нуля.")

# spyrogyra can have negative growth (die off naturally), 0 growth (not growing) and positive growth.
growthspeed = askfunc("Какова скорость прироста водросли Спирогира в озере Байкал? (км/куб в день)")

# extermination can not help spyrogyra grow, therefore can not be less than 0
while exterminationspeed < 0:
    exterminationspeed = askfunc("С какой скоростью ведётся очищение озера Байкал от водросли Спирогира?(км/куб в день)\n(Если не ведётся, введите 0.)")
    if exterminationspeed < 0:
        print("ОШИБКА: Очистка не может идти со скоростью меньше нуля.")


# checks for if lake is being polluted
if exterminationspeed - growthspeed < 0:
    print("Озеро Байкал загрязняется. Оно будет полностью загрязнено через", (baikalVolume - amountpolluted) / (growthspeed - exterminationspeed), "дней.")

# checks for if the lake is being cleaned
if exterminationspeed - growthspeed > 0:
    if amountpolluted is 0 :
        print("Озеро Байкал чисто и не загрязняется.")
    else:
        print("Озеро Байкал очищается. Оно будет полностью очищено через", amountpolluted / (exterminationspeed - growthspeed), "дней.")

# checks for if the lake is not being cleaned nor polluted.
if exterminationspeed - growthspeed is 0:
    if amountpolluted is 0:
        print("Озеро Байкал чисто и не загрязняется.")
    else:
        print("Озеро Байкал не загрязняется и не очищается. Объём незагрязнённого озера ", baikalVolume - amountpolluted, "километров кубических.")
