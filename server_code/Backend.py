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
  return result[0]["FacilityID"]


@anvil.server.callable
def query_overseer(facility_id : int):
  query = f"SELECT * FROM Overseer WHERE FacilityID={facility_id};"
  with sqlite3.connect(data_files["nuclear_facility.db"]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]


@anvil.server.callable
def query_site_name(site_id: int):
  query = f"SELECT location FROM Facility WHERE FacilityID={site_id};"
  with sqlite3.connect(data_files["nuclear_facility.db"]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result

@anvil.server.callable
def delete_overseer(overseer_id : int):
  query = f"DELETE FROM Overseer WHERE OverseerID={overseer_id};"
  with sqlite3.connect(data_files["nuclear_facility.db"]) as conn:
    cur = conn.cursor()
    cur.execute(query)


@anvil.server.callable
def insert_overseer(Firstname: str, Lastname: str, Clearance : int, site_id : int):
  query = f"INSERT INTO Overseer (Firstname, Lastname, Clearance, FacilityID) VALUES ('{Firstname}', '{Lastname}', {Clearance}, {site_id});"
  with sqlite3.connect(data_files["nuclear_facility.db"]) as conn:
    cur = conn.cursor()
    cur.execute(query)