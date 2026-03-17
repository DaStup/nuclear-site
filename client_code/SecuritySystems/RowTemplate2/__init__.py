from ._anvil_designer import RowTemplate2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate2(RowTemplate2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("check_box_status", "change")
  def check_box_status_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass

  @handle("button_toggle", "click")
  def button_toggle_click(self, **event_args):
    security_system_page = self.parent.parent.parent.parent
    if(self.item["Status"] == "on"):
      anvil.server.call("update_security_status", self.item["SaftySystemsID"], 0)
    else:
      anvil.server.call("update_security_status", self.item["SaftySystemsID"], 1)
    security_system_page.UpdateGrid()