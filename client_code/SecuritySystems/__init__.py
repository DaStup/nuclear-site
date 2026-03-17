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
    self.reactor_id = properties["reactor_id"]
    self.UpdateGrid()

  @handle("button_back", "click")
  def button_back_click(self, **event_args):
    open_form('SiteOverview', site_id=f"{self.site_id}")


  def UpdateGrid(self):
    security_data = anvil.server.call("query_security_systems", self.reactor_id)
    for data in security_data:
      if data["Status"] == 0:
        data["Status"] = "off"
      else:
        data["Status"] = "on"
    self.repeating_panel_security.items = security_data
  