#!/usr/bin/env python

from os import listdir
from os.path import isfile, join
from cursesmenu import SelectionMenu
from parser import Parser
import sys
import libtmux

'''
TODO:

1. Logging in a structured way

2. define a function to call the tmux load of the layout

3. Create a configuration file and the load conf + main parser
'''

layout_home = "/home/fmount/tmux-menu-files"

def dynamic_menu(config):
	'''
	Build a dynamic menu starting from the config
	read by a json converted to a dict
	'''
	
	#menu = {'title': 'Hello World',
	#		'type': 'command',
	#		'command': 'echo Hello World!'}
	
	#option_1 = {'title': 'Hello World',
	#			'type': 'command',
	#			'command': 'echo Hello World!'}
	
	#menu['options'] = [option_1]

	#m = CursesMenu("Tmux Layout", "Select your layout")

	layouts = get_layout_list(layout_home)
	
	selection_menu = SelectionMenu.get_selection(layouts)
	
	print("Hello man, you just selected the %s option" % layouts[int(selection_menu)])

	return layouts[int(selection_menu)]


def get_layout_list(path):
	try:
		layouts = [f for f in listdir(path) if isfile(join(path, f))]
		return layouts
	except Exception, notfound:
		print(notfound)
		sys.exit(0)

def tmux_loadconf(layout, session_id):
	
	server = libtmux.Server()
	
	# TODO: verify the tmux session
	session = server.get_by_id(session_id)
	
	#Get the pane
	pane = session.attached_pane
	
	cmd = "tmux source-file " + layout_home + "/" + layout
	pane.send_keys(cmd, enter=True)


#path = raw_input("Give me the path of the layout home\n")
#layouts = get_layout_list(path)

#print("%s" % layouts)
p = Parser("/home/fmount/git/tmux-layout-plugin/config/parameters.json")
p.parse()
print(p.raw_json)
#to_load = dynamic_menu(conf)
#tmux_loadconf(to_load, "$2")
