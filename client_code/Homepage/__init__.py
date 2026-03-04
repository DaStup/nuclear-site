from ._anvil_designer import HomepageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Homepage(HomepageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    nuclear_sites = anvil.server.call("query_nuclear_sites", 0)
    nuclear_sites_list = []
    for site in nuclear_sites:
      nuclear_sites_list.append(site['location'])
    self.drop_down_nuclear_site.items = nuclear_sites_list

  @handle("button_site_manage", "click")
  def button_site_manage_click(self, **event_args):
     open_form('SiteOverview', my_parameter=f"{self.drop_down_nuclear_site.selected_value}")
