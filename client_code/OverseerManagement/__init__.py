from ._anvil_designer import OverseerManagementTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class OverseerManagement(OverseerManagementTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.site_id = properties["site_id"]
    self.repeating_panel_overseer.items = anvil.server.call("query_overseer", self.site_id)
    

  @handle("button_back", "click")
  def button_back_click(self, **event_args):
    open_form('Homepage')

  @handle("button_add_overseer", "click")
  def button_add_overseer_click(self, **event_args):
    if self.text_box_firstname.text != "" and self.text_box_lastname.text != "":
      anvil.server.call("insert_overseer", self.text_box_firstname.text, self.text_box_lastname.text, self.drop_down_clearance.selected_value, self.site_id)
    self.repeating_panel_overseer.items = anvil.server.call("query_overseer", self.site_id)
