# This is distributed under cc0. See the LICENCE file distributed along with
# this code.

from __future__ import print_function

from py3k import *
from node import Node


class Adversary(object):
    """An adversary which attempts some type of attack on an onion service."""

    def __init__(self):
        raise NotImplemented # TODO


class Pwnie(Adversary):
    """An adversary which attempts to pwn other nodes."""

    def __init__(self, successProbability, timeToPwnage):
        """Create a new pwning adversary.

        :type successProbability: float
        :ivar successProbability: The probability of an attack from
            this adversary resulting in a successful compromise of a node.
        :type timeToPwnage: int
        :ivar timeToPwnage: The average ammount of time it takes
            before this adversary can pop its target.
        """
        self.successProbability = 0.0
        self.timeToPwnage = 0 # TODO see `Node.pwntime`

        raise NotImplemented # TODO

    def pop(self, node):
        """Attempt to break into another node of interest, with some
        `successProbability`.
        """
        raise NotImplemented # TODO


class Sybil(Node):
    """An adversary which runs a node in order to try to end up in an onion
    service client's path.
    """

    def __init__(self):
        raise NotImplemented # TODO
