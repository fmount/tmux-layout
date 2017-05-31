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
		self.logger.debug("Acquiring parameters: [%s] - [%s] - [%s]" % (self.layout, self.layout_home, self.session))
		
		print("Acquiring parameters: [%s] - [%s] - [%s]" % (self.layout, self.layout_home, self.session))
		

	def exist_session(self, curr_sess):
		if curr_sess is not None:
			return True
		return False


	def build_command(self):
		cmd = "tmux source-file " + '/'.join([self.layout_home, self.layout])
		self.logger.debug("Building command %s" % cmd)
		print("Building command %s" % cmd)
		return cmd


	def tmux_loadconf(self):

		session = self.server.get_by_id("$" + str(self.session))
		print(session)
		if self.exist_session(session) and self.layout is not None:
			#Get the pane
			print("send_command")
			pane = session.attached_pane
			cmd = self.build_command()
			pane.send_keys(cmd, enter=True)


# MAIN FOR DEBUG PURPOSES ...
if __name__ == '__main__':
	params = {"layout": "monitor", "session": 2, 'layout_home': "/home/fmount/tmux-menu-files"}
	t = Tmuxer(params)
	t.build_command()
	t.tmux_loadconf()
