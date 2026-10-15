import menu
import func
from archive import *

arc = 'testing.txt'

if not archive(arc):
    creat(arc)

menu.menu(arc)
