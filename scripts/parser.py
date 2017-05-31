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


from abc import ABCMeta, abstractmethod
from os import path
import six
import abc
import json
import logging

#@six.add_metaclass(abc.ABCMeta)
class Parser(object):
	__metaclass__ = abc.ABCMeta

	def __init__(self, config):
		self.logger = logging.getLogger('parser')
		if config is None:
			raise Exception("[Parser]: json config not found on filesystem")
		
		cfiles = list(filter(lambda x: path.exists(x), [config[i] for i in config.keys()]))
		if(len(cfiles) == 0):
			raise Exception("Json config not found on filesystem")

		self.config = cfiles[0]
		self.logger.info("[Parser] Processing config file: [%s]" % self.config)

		try:
			with open(self.config, 'r') as f:
				self.raw_json = json.load(f)
		except Exception as js_except:
			self.logger.error("Parser.__init__(): [%s]" % js_except.__str__())
			raise js_except

		

	@abstractmethod
	def parse(self):
		raise NotImplemetedException("[ERR] Base Class -  You have to derive and implement your own specialized version.")
