# This is distributed under cc0. See the LICENCE file distributed along with
# this code.


class Client(object):
    """A next-gen onion service client."""

    def __init__(self):
        self.circuits = []

    def getCircuit(self):
        """Choose one of our pre-built circuits or build one if necessary."""
        raise NotImplemented # TODO

    def buildCircuit(self):
        """Build a circuit."""
        raise NotImplemented # TODO

    def requestService(self):
        """Make a request to an onion service."""
        raise NotImplemented # TODO
