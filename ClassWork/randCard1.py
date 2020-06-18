import random
from guizero import App, PushButton

cardList = list(range(1, 53))
random.shuffle(cardList)
cardNum1 = cardList[0]
cardNum2 = cardList[1]
app = App(layout="grid")

card1 = PushButton(app, image="PlayingCards/" + str(cardNum1) + ".png", grid=[0, 1])
card2 = PushButton(app, image="PlayingCards/" + str(cardNum2) + ".png", grid=[1, 1])

app.display()
