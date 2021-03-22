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
    N = range( 6 )
    K = 3

    G = dict( ( v, sample( N, K ) ) for v in N )

    ga = Animation()
    ga.set_direction("LR")
    for v, adj in G.items():
        for u in adj:
            ga.add_edge( v, u )
    ga.next_step()

    seen = [ False for v in  N ]
    def dfv( v ):
        ga.highlight_node( v )
        ga.next_step()
        seen[ v ] = True
        for u in G[ v ]:
            if not seen[ u ]:
                ga.highlight_node( v )
                ga.highlight_edge( v, u )
                ga.next_step()
                dfv( u )

    dfv( 0 )

    graphs = ga.graphs()
    files = render( graphs, 'dfv', 'png' )
    gif( files, 'dfv', 50 )
