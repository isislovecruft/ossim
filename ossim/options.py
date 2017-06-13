# This is distributed under cc0. See the LICENCE file distributed along with
# this code.

"""Commandline options for simulation."""

import argparse


def makeOptionsParser():
    """Initialise an :class:`argparse.ArgumentParser`, set up some options
    flags, and parse any commandline arguments we received.

    :rtype: tuple
    :returns: A 2-tuple of ``(namespace, parser)``.
    """
    parser = argparse.ArgumentParser()

    # Which spec should we follow?
    prop_group = parser.add_mutually_exclusive_group(required=True)
    prop_group.add_argument("--prop247", action="store_true",
                            help="Where the proposals diverge, follow prop#241.")

    # How should we simulate the network?
    net_group = parser.add_argument_group(
        title="Network Simulation Options",
        description=("Control various simulation options regarding how the local"
                     " network connection for the client is simulated."))
    net_group.add_argument(
        "-N", "--total-relays", type=int,
        help=("The total number of relays in the simulated network.  If this "
              "argument is not given, then a random number of relays in "
              "[100, 10000] will be used."))
    net_group.add_argument(
        "-s", "--sniper-network", action="store_true",
        help=("Simulate a network that does a DoS attack on a client's "
              "non-evil guard nodes with some probability after each "
              "connection."))

    return parser.parse_args()
