#!/usr/bin/env python
#
# v0.1 -- 
#
# fmount <francesco.pantano@linux.com>
#
#

from os import listdir
from os.path import isfile, join
from cursesmenu import SelectionMenu
from parser import Parser
from argparse import ArgumentParser as argparser
import sys
import libtmux
import json
import config
import logging

'''
TODO:

2. define a function to call the tmux load of the layout

'''

option_cli = argparser(description="Build curses dynamic menu utility")
option_cli.add_argument("-s", "--session", help="Specify the tmux session_id to attach the new layout", action="store", dest="s")

options = option_cli.parse_args()


class Dyn_menu(Parser):
	def __init__(self):
		super(Dyn_menu, self).__init__(config.parameters_json_file_source)
		self.logger = logging.getLogger('Dyn_menu')
	
	#Specialize my parser for the menu ...
	def parse(self):
		#Get the raw_json from the Parser class
		self.menu_params = self.raw_json

	
	def get_layout_list(self, path):
		try:
			layouts = [f for f in listdir(path) if isfile(join(path, f))]
			self.logger.info("[Dyn_menu] Loading %s " % layouts)
			return layouts
		except Exception, notfound:
			self.logger.error("Dyn_menu.get_layout_list(): [%s]" % notfound.__str__())
			sys.exit(0)
	
	
	# Curses menu section ...
	def build_menu(self):
		'''
		Build a dynamic menu starting from the config
		read by a json converted to a dict
		'''
		self.layouts = self.get_layout_list(self.raw_json['globals']['layout_home'])
		selection_menu = SelectionMenu.get_selection(self.layouts)
		print("Hello man, you just selected the %s option" % self.layouts[int(selection_menu)])
		return self.layouts[int(selection_menu)]



	def tmux_loadconf(self, layout, session_id):

		server = libtmux.Server()
	
		# TODO: verify the tmux session
		session = server.get_by_id(session_id)
	
		#Get the pane
		pane = session.attached_pane
	
		cmd = "tmux source-file " + self.layout_home + "/" + layout
		pane.send_keys(cmd, enter=True)



if __name__ == '__main__':
	logging.basicConfig(filename='/tmp/tmux-layout-backup.log', level=logging.DEBUG)
	logging.debug("[INFO] Building layout menu")

	#if not xor(bool(option_cli.1), bool(option_cli.2))
	if options.s:
		try:
			m = Dyn_menu()
			m.parse()
			lyt = m.build_menu()
			#print("Passing %s " % options.s)
			#tmux_loadconf(lyt, options.s)
		except Exception as e:
			print(e)
			sys.exit(-1)
	else:
		print("No session has been passed.. exiting ..")
		sys.exit(-1)
