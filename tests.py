#!/usr/bin/env python
# Copyright (c) 2015 Heikki Hokkanen <hoxu at users.sf.net>
# License: GPLv3
import shutil
import subprocess
import tempfile
import unittest

class TestGig(unittest.TestCase):
    def setUp(self):
        # Create bare origin repository
        self.origin = tempfile.mkdtemp('gigtestorigin')
        subprocess.call(['git', 'init', '--bare', self.origin])

        # Clone origin repository
        self.clone = tempfile.mkdtemp('gigtestclone')
        subprocess.call(['git' 'clone', self.origin, self.clone])

    def tearDown(self):
        shutil.rmtree(self.origin)
        shutil.rmtree(self.clone)

    pass

if __name__ == '__main__':
    unittest.main()
