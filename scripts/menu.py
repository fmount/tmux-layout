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
from utils.parser import Parser as Parser
from argparse import ArgumentParser as argparser
from tmuxer import Tmuxer
import sys
import libtmux
import json
import config
import logging


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
		except Exception as notfound:
			self.logger.error("Dyn_menu.get_layout_list(): [%s]" % notfound.__str__())
			sys.exit(-1)
	
	
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



if __name__ == '__main__':
	logging.basicConfig(filename='/tmp/tmux-layout.log', level=logging.DEBUG)
	logging.debug("[INFO] Building layout menu")
	params = {}

	if options.s:
		try:
			m = Dyn_menu()
			m.parse()
			lyt = m.build_menu()
	
			params = { "layout": lyt, "session": options.s, 'layout_home': m.menu_params['globals']['layout_home'] }
			#print(params)
			t = Tmuxer(params)
			t.build_command()
			t.tmux_loadconf()
		except Exception as e:
			print(e)
			sys.exit(-1)
	else:
		print("No session has been passed.. exiting ..")
		sys.exit(-1)
