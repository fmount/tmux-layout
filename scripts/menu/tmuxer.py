#!/usr/bin/env python
#
# v0.1 --
#
# fmount <francesco.pantano@linux.com>
#
#

from argparse import ArgumentParser as argparser
import libtmux
import logging
import subprocess as sub

'''

'''

class Tmuxer(object):
	def __init__(self, args):
		self.logger = logging.getLogger('Tmuxer')

		for attr in args.keys():
			setattr(self, attr, args.get(attr, None))

		
		self.server = libtmux.Server()
		self.logger.debug("Acquiring parameters: [%s] - [%s] - [%s] [%s]" \
				% (self.layout, self.layout_home, self.session, self.main_pane))
		

	def exist_session(self, curr_sess):
		if curr_sess is not None:
			return True
		return False


	def build_command(self):
		cmd = "tmux source-file " + '/'.join([self.layout_home, self.layout])
		self.logger.debug("Building command %s" % cmd)
		return cmd

	
	def get_pane_by_id(self, pane, pid):
		if pane._pane_id == pid:
			return True
		return False


	def select_pane(self, session):
		current_window = session.attached_window
		for p in current_window.list_panes():
			self.logger.debug("[#PANE PROCESSING] Found %s" % (p._pane_id))
			if self.get_pane_by_id(p, self.main_pane):
				return p
		return None


	def tmux_loadconf(self):

		session = self.server.get_by_id("$" + str(self.session))
		if self.exist_session(session) and self.layout is not None:
			
			#Get the main pane where the command can be send
			
			#pane = session.attached_pane
			pane = self.select_pane(session)

			cmd = self.build_command()
			self.logger.debug("Sending command to main pane %s" % str(pane))
			pane.send_keys(cmd, enter=True)


# MAIN FOR DEBUG PURPOSES ...
if __name__ == '__main__':
	params = {"layout": "monitor", "session": 2, 'layout_home': "/home/fmount/tmux-menu-files", "main_pane": 75}
	t = Tmuxer(params)
	t.build_command()
	t.tmux_loadconf()
