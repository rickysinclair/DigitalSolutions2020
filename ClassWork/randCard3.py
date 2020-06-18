import random
from guizero import App, PushButton, Window

app = App(layout="grid")
window = Window(app, title="Second Window", layout="grid")
window2 = Window(app, title="Third Window", layout="grid")
window.hide()
window2.hide()
cardList = list(range(1, 53))


def card_display():
    random.shuffle(cardList)
    cardNum1 = cardList[0]
    cardNum2 = cardList[1]
    cardNum3 = cardList[2]
    cardNum4 = cardList[3]
    cardList.remove(cardNum1)
    cardList.remove(cardNum2)
    cardList.remove(cardNum3)
    cardList.remove(cardNum4)

    print(len(cardList))
    card1 = PushButton(app, image="PlayingCards/" + str(cardNum1) + ".png", grid=[0, 1])
    card2 = PushButton(app, image="PlayingCards/" + str(cardNum2) + ".png", grid=[1, 1])
    card3 = PushButton(app, image="PlayingCards/" + str(cardNum3) + ".png", grid=[0, 2])
    card4 = PushButton(app, image="PlayingCards/" + str(cardNum4) + ".png", grid=[1, 2])

    if len(cardList) == 0:
        window.show()
        window2.show()
        app.hide()

button = PushButton(app, command=card_display, text="DEAL", grid=[5, 1])
app.display()
