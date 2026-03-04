import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3

@anvil.server.callable
def query_nuclear_sites(self):
  query = "SELECT location FROM Facility;"
  with sqlite3.connect(data_files["nuclear_facility.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def query_reactor_data(reactorID:int):
  query = f"SELECT Pressure, Temperature, NeutronFlux, ControlRodPos FROM Reactor WHERE ReactorID={reactorID};"
  with sqlite3.connect(data_files["nuclear_facility.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def query_reactors(facilityID: int):
  query = f"SELECT ReactorID FROM Reactor WHERE FacilityID={facilityID};"
  with sqlite3.connect(data_files["nuclear_facility.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result

@anvil.server.callable
def query_facility_id(facilityName: str):
  query = f"SELECT FacilityID FROM Facility WHERE location='{facilityName}';"
  with sqlite3.connect(data_files["nuclear_facility.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]