# This is distributed under cc0. See the LICENCE file distributed along with
# this code.

from __future__ import print_function

from py3k import *

# TODO maybe move these to some central place so we don't have globals everywhere?

#: The number of (van)guards in the service-side of an introductory point circuit
GUARD_LAYERS_IP = 2

#: The number of (van)guards in the service-side of a rendezvous point circuit
GUARD_LAYERS_RP = 3


class OnionServiceGuard(object):
    """An onion service's guard.  Can be at any layer, G1, G2, or G3."""

    def __init__(self, layer, node):
        """Create a new onion service guard.

        :type layer: int
        :param layer: May be `1`, `2`, or `3`. (Or higher, if the design changes
            to include more than three layers of vanguards.)
        :type node: `node.Node`
        :param node: The node currently in this Guard position.
        """
        assert layer in range(1, GUARD_LAYERS_RP+1)

        self.node = node
        self.layer = layer

    def __str__(self):
        """Return the human-readable name for this node."""
        return self.node.__str__()

    @property
    def bandwidth(self):
        """Completely make-believe bandwith.  It's calculated as a random point
        on the probability density function of a gamma distribution over
        (0,100000] in KB/s.
        """
        return self.node.bandwidth()

    @property
    def id(self):
        """Return the hex id for this node"""
        return self.node.id()

    @property
    def running(self):
        """Return true iff this node is truly alive.  Client simulation code
           mustn't call this."""
        return self.node.running()

    @property
    def isAdversarial(self):
        """Return true iff this node is controlled by some (presumedly
           misbehaving) adversary.  Client simulation code mustn't
           call this.
        """
        return self.node.isAdversarial()
