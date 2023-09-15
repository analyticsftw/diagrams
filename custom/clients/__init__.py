"""
OnPrem provides a set of general on-premise services.
"""

from diagrams import Node


class _Clients(Node):
    _provider = "clients"
    _icon_dir = "resources/clients"

    fontcolor = "#ffffff"
