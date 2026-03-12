from ._anvil_designer import SiteOverviewTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables




class SiteOverview(SiteOverviewTemplate):
  reactor_data = [{0}, {0}]
  def __init__(self, **properties):
    self.init_components(**properties)
    site_name = properties['my_parameter']
    self.headline_nuclear_site.text = site_name
    site_id = anvil.server.call("query_facility_id", f"{site_name}")[0]['FacilityID']
    reactors_ids = [int(item[0]) for item in anvil.server.call("query_reactors", f"{site_id}")]
    reactor_names = []
    for id in reactors_ids:
      reactor_names.append("Reactor " + str(id));
    self.drop_down_reactor.items = list(zip(reactor_names, reactors_ids))
    self.reactor_data = anvil.server.call("query_reactor_data", f"{self.drop_down_reactor.selected_value}")
    
    self.plot_pressure.data = [
      go.Bar(
        x = [0],
        y = [self.reactor_data[0]["Pressure"]],
        name = 'Pressure'
      )
    ]
    self.plot_temp.data = [
      go.Bar(
        x = [0],
        y = [self.reactor_data[0]["Temperature"]],
        name = 'Temperature'
      )
    ]
    
    self.plot_neutron.data = [
      go.Bar(
        x = [0],
        y = [self.reactor_data[0]["NeutronFlux"]],
        name = 'Temperature'
      )
    ]
    self.plot_rod.data = [
      go.Bar(
        x = [0],
        y = [self.reactor_data[0]["ControlRodPos"]],
        name = 'Temperature'
      )
    ]
   
  
  @handle("drop_down_reactor", "change")
  def drop_down_reactor_change(self, **event_args):
    self.reactor_data = anvil.server.call("query_reactor_data", f"{self.drop_down_reactor.selected_value}")
    self.plot_pressure.data = [
      go.Bar(
        x = [0],
        y = [self.reactor_data[0]["Pressure"]],
        name = 'Pressure'
      )
    ]
    self.plot_temp.data = [
      go.Bar(
        x = [0],
        y = [self.reactor_data[0]["Temperature"]],
        name = 'Temperature'
      )
    ]
    
    self.plot_neutron.data = [
      go.Bar(
        x = [0],
        y = [self.reactor_data[0]["NeutronFlux"]],
        name = 'Temperature'
      )
    ]
    self.plot_rod.data = [
      go.Bar(
        x = [0],
        y = [self.reactor_data[0]["ControlRodPos"]],
        name = 'Temperature'
      )
    ]
