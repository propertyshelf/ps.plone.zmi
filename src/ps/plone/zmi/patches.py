# -*- coding: utf-8 -*-
"""Patch DTML files."""

from OFS.ObjectManager import ObjectManager

ADD_PS_CSS_MANAGE_MAIN = """
<dtml-if "_.len(this().getPhysicalPath()) == 1 or this().meta_type == 'Folder' and 'PloneSite' not in [o.__class__.__name__ for o in this().aq_chain]">
  <!-- Add PS CSS file.-->
  <link rel="stylesheet" type="text/css" href="/++resource++ps-admin-ui.css" />
</dtml-if>
"""

ADD_PS_CSS_MANAGE = """
  <!-- Add PS CSS file.-->
  <link rel="stylesheet" type="text/css" href="/++resource++ps-admin-ui.css" />
"""

manage_main = ObjectManager.manage_main
orig = manage_main.read()
pos = orig.find('<!-- Add object widget -->')

# Add in our button html at the right position
new = orig[:pos] + ADD_PS_CSS_MANAGE_MAIN + orig[pos:]

# Modify the manage_main
manage_main.edited_source = new
manage_main._v_cooked = manage_main.cook()


manage = ObjectManager.manage
orig = manage.read()
pos = orig.find('</head>')

# Add in our button html at the right position
new = orig[:pos] + ADD_PS_CSS_MANAGE + orig[pos:]

# Modify the manage_main
manage.edited_source = new
manage._v_cooked = manage.cook()
