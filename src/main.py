from dbHandler import createTables
from views.App import App
from views.Home import Home
from views.Game import Game
from views.SignIn import SignIn
from views.SignUp import SignUp
from store import store

createTables()


app = App({
    'home': Home,
    'game': Game,
    'signin': SignIn,
    'signup': SignUp
}, 'signin')

store.setApp(app)

app.start()
