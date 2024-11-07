import FreeSimpleGUI.window
from functions import get_todos, write_todos

import FreeSimpleGUI

window = FreeSimpleGUI.Window('My To-Do App', layout=[""])
window.read()
window.close()