from guizero import App, PushButton, TextBox, Window, Text

user_pw = 'letmein'
user_un = 'ricky'
app = App(title='Login', layout='grid')
window = Window(app, title="Second Window", layout="grid")
window.hide()
username = TextBox(app, grid=[0, 0])
password = TextBox(app, grid=[0, 1])

def check_cred():
    text = Text(app, grid=[0, 4])
    text.clear()
    if password.value == user_pw and username.value == user_un:
        window.show()
    else:
        text = Text(app, text='Incorrect login!', grid=[0, 4])

submit = PushButton(app, text='SUBMIT', grid=[0, 3], command=check_cred)

app.display()
