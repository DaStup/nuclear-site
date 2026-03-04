from ._anvil_designer import SiteOverviewTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class SiteOverview(SiteOverviewTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    site_name = properties['my_parameter']
    self.headline_nuclear_site.text = site_name
    self.canvas_reactor_data.height = 500
    self.canvas_reactor_data.reset_context()
    site_id = anvil.server.call("query_facility_id", f"{site_name}")[0]['FacilityID']
    self.drop_down_reactor.items = anvil.server.call("query_reactors", f"{site_id}")
  

  @handle("canvas_reactor_data", "reset")
  def canvas_reactor_data_reset(self, **event_args):
    rdc = self.canvas_reactor_data
    rdc.scale(2, 2)
    rdc.stroke_style = "#2196F3"
    rdc.line_width = 3
    rdc.fill_style = "#FF0000"
    rdc.fill_rect(10, 10, 10, 100)
    rdc.fill_rect(30, 10, 10, 100)

  @handle("drop_down_reactor", "change")
  def drop_down_reactor_change(self, **event_args):
    pass
