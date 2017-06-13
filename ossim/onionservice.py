# This is distributed under cc0. See the LICENCE file distributed along with
# this code.

from __future__ import print_function

from py3k import *
from guard import GUARD_LAYERS_RP


class OnionService(object):
    """A next-gen onion service."""

    def __init__(self):
        self.guards = {
            "layerOne": [],
            "layerTwo": [],
            "layerThree": [],
        }
        self.circuits = []
        self._fqdn = ""

    @property
    def fqdn(self):
        """The onion service's domain name, e.g. "7y35c6p2lq7sk45h.onion"."""
        return self._fqdn

    def getCircuit(self):
        """Choose one of our pre-built circuits or build one if necessary."""
        raise NotImplemented # TODO

    def buildCircuit(self):
        """Build a circuit."""
        raise NotImplemented # TODO

    def chooseGuard(self, level=0):
        """Pick a guard for a certain `level`.

        :type level: int
        :param level: The guard level to choose: `1` for G1, `2` for
            G2, or `3` for G3.
        """
        assert level in range(1, GUARD_LAYERS_RP+1)

        raise NotImplemented # TODO
