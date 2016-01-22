# -*- coding: utf-8 -*-
"""ZMI customizations for Plone instances."""

# local imports
from . import patches
patches = patches  # PyFlakes


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
