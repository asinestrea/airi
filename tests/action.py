# Copyright 2016, Sinestrea <git.sinestrea@gmail.com>
#
# This file is part of "airi".
#
# "airi" is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# "airi" is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# "airi". If not, see <http://www.gnu.org/licenses/>.

import unittest

from airi.animation import Step
import airi.action as ga

class TestActions( unittest.TestCase ):
	def setUp(self):
		self.steps = [ Step() ]

	def tearDown( self ):
		self.steps = None

	def test_remove_unlabeled_node( self ):
		ga.RemoveNode( 0 )( self.steps )

	def test_unlabel_unexistent_node( self ):
		ga.UnlabelNode( 0 )( self.steps )

if __name__ == '__main__':
	unittest.main()
