from ._anvil_designer import CoolingTowersTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class CoolingTowers(CoolingTowersTemplate):
  
    
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.site_id = properties["site_id"]
    self.reactor_id = properties["reactor_id"]
    self.tower_ids = [int(item[0]) for item in anvil.server.call("query_towers", f"{self.reactor_id}")]
    self.tower_names = []
    for id in self.tower_ids:
      self.tower_names.append("Tower" + str(id))
    self.drop_down_cooling_tower.items = list(zip(self.tower_names, self.tower_ids))
    self.tower_data = anvil.server.call("query_tower_data", self.drop_down_cooling_tower.selected_value)
    self.update_tower_data()

  
  @handle("button_back", "click")
  def button_back_click(self, **event_args):
    open_form('SiteOverview', site_id=f"{self.site_id}")

  @handle("drop_down_cooling_tower", "change")
  def drop_down_cooling_tower_change(self, **event_args):
    self.update_tower_data()

  @handle("button_toggle_sys1", "click")
  def button_toggle_sys1_click(self, **event_args):
    if(self.tower_data[0]["StatusPrim"] == 0):
      anvil.server.call("update_prim_status", self.drop_down_cooling_tower.selected_value, 1)
    else:
       anvil.server.call("update_prim_status", self.drop_down_cooling_tower.selected_value, 0)
    self.update_tower_data()

    
  @handle("button_toggle_sys2", "click")
  def button_toggle_sys2_click(self, **event_args):
    if(self.tower_data[0]["StatusSec"] == 0):
      anvil.server.call("update_sec_status", self.drop_down_cooling_tower.selected_value, 1)
    else:
      anvil.server.call("update_sec_status", self.drop_down_cooling_tower.selected_value, 0)
    self.update_tower_data()

  def update_tower_data(self):
    self.tower_data = anvil.server.call("query_tower_data", self.drop_down_cooling_tower.selected_value)
    if(self.tower_data[0]["StatusPrim"] == 1):
      self.label_status1.text = "On"
    else:
      self.label_status1.text = "Off"
    if(self.tower_data[0]["StatusSec"] == 1):
      self.label_status2.text = "On"
    else:
      self.label_status2.text = "Off"
    self.label_pressure.text = str(self.tower_data[0]["Pressure"]) + " bar"
    self.label_flowrate.text = str(self.tower_data[0]["FlowRate"]) + " L/s"