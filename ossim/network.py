#!/usr/bin/python
# This is distributed under cc0. See the LICENCE file distributed along with
# this code.

"""
   Let's simulate a tor network!  We're only going to do enough here
   to try out guard selection/replacement algorithms from proposal
   259, and some of its likely variants.
"""

import random

from math import floor

from py3k import *


def _randport():
    """Generate and return a random port."""
    return random.randint(1,65535)


def compareNodeBandwidth(this, other):
    if this.bandwidth < other.bandwidth: return -1
    elif this.bandwidth > other.bandwidth: return 1
    else: return 0


class Network(object):
    """Base class to represent a simulated Tor network."""

    def __init__(self, num_nodes, pevil=0.5,
                 avgnew=1.5, avgdel=0.5):
        """Create a new network with 'num_nodes' randomly generated nodes.
           Each node should be evil with
           probability 'pevil'.  Every time the network churns,
           'avgnew' nodes should be added on average, and 'avgdel'
           deleted on average.
        """
        self._pevil = pevil

        # a list of all the Nodes on the network, dead and alive.
        self._wholenet = [ Node("node%d"%n,
                                port=_randport(pfascistfriendly),
                                evil=random.random() < pevil)
                           for n in xrange(num_nodes) ]
        for node in self._wholenet:
            node.updateRunning()

        # lambda parameters for our exponential distributions.
        self._lamdbaAdd = 1.0 / avgnew
        self._lamdbaDel = 1.0 / avgdel

        # total number of nodes ever added on the network.
        self._total = num_nodes

    def new_consensus(self):
        """Return a list of the running guard nodes."""
        return [ node for node in self._wholenet if node.runningp() ]

    def do_churn(self):
        """Simulate churn: delete and add nodes from/to the network."""
        nAdd = int(random.expovariate(self._lamdbaAdd) + 0.5)
        nDel = int(random.expovariate(self._lamdbaDel) + 0.5)

        # kill nDel non-dead nodes at random.
        random.shuffle(self._wholenet)
        nkilled = 0
        for node in self._wholenet:
            if nkilled == nDel:
                break
            if not node._dead:
                node.kill()
                nkilled += 1

        # add nAdd new nodes.
        for n in xrange(self._total, self._total+nAdd):
            node = Node("node%d"%n,
                        port=_randport(),
                        evil=random.random() < self._pevil)
            self._total += 1

    def updateRunning(self):
        """Enough time has passed for some nodes to go down and some to come
           up."""
        for node in self._wholenet:
            node.updateRunning()

    def probe_node_is_up(self, node):
        """Called when a simulated client is trying to connect to 'node'.
           Returns true iff the connection succeeds."""
        return node.running()


class _NetworkDecorator(object):
    """Decorator class for Network: wraps a network and implements all its
       methods by calling down to the base network.  We use these to
       simulate a client's local network connection."""

    def __init__(self, network):
        self._network = network

    def new_consensus(self):
        return self._network.new_consensus()

    def do_churn(self):
        self._network.do_churn()

    def probe_node_is_up(self, node):
        return self._network.probe_node_is_up(node)

    def updateRunning(self):
        self._network.updateRunning()


class FascistNetwork(_NetworkDecorator):
    """Network that blocks all connections except those to ports 80, 443"""
    def probe_node_is_up(self, node):
        return (node.getPort() in [80,443] and
                self._network.probe_node_is_up(node))


class EvilFilteringNetwork(_NetworkDecorator):
    """Network that blocks connections to non-evil nodes with P=pBlockGood"""
    def __init__(self, network, pBlockGood=1.0):
        super(EvilFilteringNetwork, self).__init__(network)
        self._pblock = pBlockGood

    def probe_node_is_up(self, node):
        if not node.isAdversarial():
            if random.random() < self._pblock:
                return False
        return self._network.probe_node_is_up(node)


class SniperNetwork(_NetworkDecorator):
    """Network that does a DoS attack on a client's non-evil nodes with
       P=pKillGood after each connection."""
    def __init__(self, network, pKillGood=1.0):
        super(SniperNetwork, self).__init__(network)
        self._pkill = pKillGood

    def probe_node_is_up(self, node):
        result = self._network.probe_node_is_up(node)

        if not node.isAdversarial() and random.random() < self._pkill:
            node.kill()

        return result


class FlakyNetwork(_NetworkDecorator):
    """A network where all connections succeed only with probability
       'reliability', regardless of whether the node is up or down."""
    def __init__(self, network, reliability=0.9):
        super(FlakyNetwork, self).__init__(network)
        self._reliability = reliability

    def probe_node_is_up(self, node):
        if random.random() >= self._reliability:
            return False
        return self._network.probe_node_is_up(node)
