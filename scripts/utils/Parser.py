#!/usr/bin/env python

#	 Licensed under the Apache License, Version 2.0 (the "License");
#	 you may not use this file except in compliance with the License.
#	 You may obtain a copy of the License at
#
#		 http://www.apache.org/licenses/LICENSE-2.0
#
#	 Unless required by applicable law or agreed to in writing, software
#	 distributed under the License is distributed on an "AS IS" BASIS,
#	 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#	 See the License for the specific language governing permissions and
#	 limitations under the License.
#
#	 author: fmount <francesco.pantano@linux.com>


'''
TODO: Create class with static fields to load the paths of the config files [see cbk implementation]
'''

from prettytable import PrettyTable
import re
import json
import logging

class Parser():
	
	
	def __init__(self, config):
		
		if config is None:
			raise Exception("[Parser]: json config not found on filesystem")
		
		self.config = config
		

	def parse(self):
		try:
			with open(self.config, 'r') as json_file:
				self.raw_json = json.load(json_file)
		except Exception as json_extract_error:
			raise json_extract_error




if __name__ == '__main__':
	logging.basicConfig(filename='../log/tmux-layout-plugin.log', level=logging.DEBUG)
	logging.debug("[LOG] Start Parsing config parameters")
	p = Parser("../config/parameters.json")
	p.parse()
	print(p.raw_json)
