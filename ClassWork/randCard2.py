import random
from guizero import App, PushButton

app = App(layout="grid")

def card_display():
    cardList = list(range(1, 53))
    random.shuffle(cardList)
    cardNum1 = cardList[0]
    cardNum2 = cardList[1]

    card1 = PushButton(app, image="Cards/PlayingCards/" + str(cardNum1) + ".png", grid=[0, 1])
    card2 = PushButton(app, image="Cards/PlayingCards/" + str(cardNum2) + ".png", grid=[1, 1])

button = PushButton(app, command=card_display, text="DEAL", grid=[5, 1])

app.display()