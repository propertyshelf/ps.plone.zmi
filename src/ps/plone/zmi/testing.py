# -*- coding: utf-8 -*-
"""Test Layer for ps.plone.zmi."""

# zope imports
from plone.app.testing import (
    IntegrationTesting,
    PloneSandboxLayer,
    PLONE_FIXTURE,
)
from zope.configuration import xmlconfig


class PSPloneZMI(PloneSandboxLayer):
    """Custom Test Layer for ps.plone.zmi."""
    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        """Set up Zope for testing."""
        # Load ZCML
        import ps.plone.zmi
        xmlconfig.file(
            'configure.zcml', ps.plone.zmi,
            context=configurationContext,
        )
        xmlconfig.file(
            'overrides.zcml', ps.plone.zmi,
            context=configurationContext,
        )


PS_PLONE_ZMI_FIXTURE = PSPloneZMI()
PS_PLONE_ZMI_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PS_PLONE_ZMI_FIXTURE, ),
    name='PSPloneZMI:Integration',
)
