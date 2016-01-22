# -*- coding: utf-8 -*-
"""Test Views for ps.plone.zmi."""

# python imports
try:
    import unittest2 as unittest
except ImportError:
    import unittest

# zope imports
from zope.component import getMultiAdapter

# local imports
from ps.plone.zmi.testing import (
    PS_PLONE_ZMI_INTEGRATION_TESTING,
)


class TestViews(unittest.TestCase):
    """Views Test Case for ps.plone.zmi."""

    layer = PS_PLONE_ZMI_INTEGRATION_TESTING

    def setUp(self):
        """Additional test setup."""
        self.app = self.layer['app']
        self.portal = self.layer['portal']

    def test_view_is_registered(self):
        view = getMultiAdapter(
            (self.app, self.portal.REQUEST),
            name='plone-overview',
        )
        self.assertIn('propertyshelf', view())

    def test_propertyshelf_logo(self):
        """Validate that the propertyshelf logo is shown."""
        view = getMultiAdapter(
            (self.app, self.portal.REQUEST),
            name='plone-overview',
        )
        self.assertIn('/++resource++propertyshelf-logo.png', view())
