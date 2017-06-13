# This is distributed under cc0. See the LICENCE file distributed along with
# this code.

import random


class Node(object):
    def __init__(self, name, port, evil=False, reliability=0.96):
        """Create a new Tor node."""

        # name for this node.
        self._name = name

        # What port does this node expose?
        assert 1 <= port <= 65535
        self._port = port

        # Is this a hostile node?
        self._evil = evil

        # How much of the time is this node running?
        self._reliability = 0.999

        # True if this node is running
        self._up = True

        # True if this node has been killed permanently
        self._dead = False

        # random hex string.
        self._id = "".join(random.choice("0123456789ABCDEF") for _ in xrange(40))

        # Some completely made up number for the bandwidth of this guard.
        self._bandwidth = 0

    def __str__(self):
        """Return the human-readable name for this node."""
        return self._name

    @property
    def bandwidth(self, alpha=1.0, beta=0.5, bandwidth_max=100000):
        """Completely make-believe bandwith.  It's calculated as a random point
        on the probability density function of a gamma distribution over
        (0,100000] in KB/s.
        """
        if not self._bandwidth:
            self._bandwidth = \
                int(floor(random.gammavariate(alpha, beta) * bandwidth_max))
        return self._bandwidth

    @property
    def id(self):
        """Return the hex id for this node"""
        return self._id

    @property
    def port(self):
        """Return this node's ORPort"""
        return self._port

    @property
    def running(self):
        """Return true iff this node is truly alive.  Client simulation code
           mustn't call this."""
        return self._up

    @property
    def isAdversarial(self):
        """Return true iff this node is controlled by some (presumedly
           misbehaving) adversary.  Client simulation code mustn't
           call this.
        """
        return self._evil

    def updateRunning(self):
        """Enough time has passed that some nodes are no longer running.
           Update this node randomly to see if it has come up or down."""

        # XXXX Actually, it should probably take down nodes a while to
        # XXXXX come back up.  I wonder if that matters for us.

        if not self._dead:
            self._up = random.random() < self._reliability

    def kill(self):
        """Mark this node as completely off the network, until resurrect
           is called."""
        self._dead = True
        self._up = False

    def resurrect(self):
        """Mark this node as back on the network."""
        self._dead = False
        self.updateRunning()


class Sybil(Node):
    pass
