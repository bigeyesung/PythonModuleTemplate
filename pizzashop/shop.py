# Print Python module search path
import sys, os
from pprint import pprint

# Path hack. Add parent dir level
sys.path.insert(0, os.path.abspath('./'))
pprint(sys.path)

#import pizzapy.menu
#print(pizzapy.menu.MENU)
from pizzapy import pizza
