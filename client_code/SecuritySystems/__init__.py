from ._anvil_designer import SecuritySystemsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class SecuritySystems(SecuritySystemsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.site_id = properties["site_id"]


  @handle("button_back", "click")
  def button_back_click(self, **event_args):
    open_form('SiteOverview', site_id=f"{self.site_id}")
