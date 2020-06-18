from guizero import App, Window, TextBox, Text, PushButton

app = App(title='Login Screen', layout='grid')  # inialise app window
window = Window(app, title='GUI', layout='grid')  # initialise 2nd screen
window.hide()  # hide 2nd screen

user_un = 'sinclair'  # stored credentials
user_pw = 'letmein'

username_txt = TextBox(app, grid=[0, 0])  # initialise textboxes
password_txt = TextBox(app, grid=[0, 1])


def check_cred():
    text = Text(app, grid=[0, 2])
    text.clear()
    if username_txt.value == user_un and password_txt.value == user_pw:
        window.show()
    else:
        text = Text(app, text='Incorrect Credentials', grid=[0, 4])

submit = PushButton(app, text='SUBMIT!', grid=[0,3], command=check_cred)

app.display()
