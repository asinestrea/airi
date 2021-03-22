# Copyright 2016, Sinestrea <git.sinestrea@gmail.com>
#
# This file is part of "gvpp".
#
# "gvpp" is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# "gvpp" is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# "gvpp". If not, see <http://www.gnu.org/licenses/>.

from random import sample

from gvpp import Animation, render, gif

if __name__ == '__main__':

    ga = Animation()
    
    ga.set_direction("LR")
    
    ga.add_node("A")
    ga.gvformat_node("A", "shape=square")
    ga.add_node("B")
    ga.add_node("C")
    ga.add_node("D")
    
    ga.add_edge("A", "B")
    ga.add_edge("B", "C")
    ga.add_edge("A", "D")
    
    ga.next_step()


    for v in ["A", "B", "C", "D"]:
        ga.highlight_node( v )
        ga.gvformat_node("A", "shape=square")
        if v != "D":
            ga.next_step()

    graphs = ga.graphs()

    print(graphs)

    files = render( graphs, 'dfv', 'png' )
    gif( files, 'dfv', 50 )
