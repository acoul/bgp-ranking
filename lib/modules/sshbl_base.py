#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    sshbl parser
    ~~~~~~~~~~~~

    Class used to parse the files provided by sshbl
"""

import datetime
from modules.abstract_module import AbstractModule


class SshblBase(AbstractModule):

    def __init__(self, raw_dir):
        AbstractModule.__init__(self)
        self.directory = raw_dir

    def parse(self):
        self.date = datetime.date.today()
        for file in self.files:
            daily = open(file)
            for line in daily:
                if line[0] != '#':
                    ip = line.strip()
                    if len(ip) == 0:
                        continue
                    entry = self.prepare_entry(ip = ip, source = self.__class__.__name__, timestamp = self.date)
                    self.put_entry(entry)
            daily.close()
            self.move_file(file)
