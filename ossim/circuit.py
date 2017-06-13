# This is distributed under cc0. See the LICENCE file distributed along with
# this code.

from __future__ import print_function

from py3k import *


class Circuit(object):
    """A circuit through the Tor network."""

    def __init__(self):
        #: An ordered list of nodes in this circuit.
        self.cpath = []

        #: The time this circuit was created.
        self.created = 0

        #: Whether this circuit is finished constructing.
        self.built = False
        
    @property
    def nodes(self):
        """Learn which nodes are in this circuit."""
        return [node.id for node in self.cpath]

    def bandwidthMin(self):
        """The (optimistic) minimum bandwidth of this circuit.

        For example, if there are three nodes in our cpath, with 10 KB/s, 50
        KB/s, and 100 KB/s respectively, then this method should return "10".
        """
        raise NotImplemented # TODO

    def bandwidthAvg(self):
        """The average bandwidth of this circuit since creation.

        For example, if there are three nodes in our cpath, with 10 KB/s, 50
        KB/s, and 100 KB/s respectively, then this method should return "10".
        """
        raise NotImplemented # TODO

    def build(self):
        """Construct a circuit."""
        if not self.built:
            pass # TODO

        self.built = True

        raise NotImplemented # TODO


class ServiceIntroductoryCircuit(Circuit):
    """An onion-service-side circuit to an introductory point."""

    def __init__(self):
        super(self, ServiceIntroductoryCircuit).__init__(self)
        raise NotImplemented # TODO


class ServiceRendezvousCircuit(Circuit):
    """An onion-service-side circuit to a rendezvous point."""

    def __init__(self):
        super(self, ServiceRendezvousCircuit).__init__(self)
        raise NotImplemented # TODO


class ClientIntroductoryCircuit(Circuit):
    """An client-side circuit to an introductory point."""

    def __init__(self):
        super(self, ClientIntroductoryCircuit).__init__(self)
        raise NotImplemented # TODO


class ClientRendezvousCircuit(Circuit):
    """An client-side circuit to an rendezvous point."""

    def __init__(self):
        super(self, ClientRendezvousCircuit).__init__(self)
        raise NotImplemented # TODO
