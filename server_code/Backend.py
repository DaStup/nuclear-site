import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.files
from anvil.files import data_files
import anvil.server
import sqlite3


database_file = "nuclear_facility1.db"

@anvil.server.callable
def query_nuclear_sites(self):
  query = "SELECT location FROM Facility;"
  with sqlite3.connect(data_files[database_file]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def query_reactor_data(reactorID:int):
  query = f"SELECT Pressure, Temperature, NeutronFlux, ControlRodPos FROM Reactor WHERE ReactorID={reactorID};"
  with sqlite3.connect(data_files[database_file]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def query_reactors(facilityID: int):
  query = f"SELECT ReactorID FROM Reactor WHERE FacilityID={facilityID};"
  with sqlite3.connect(data_files[database_file]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result

@anvil.server.callable
def query_facility_id(facilityName: str):
  query = f"SELECT FacilityID FROM Facility WHERE location='{facilityName}';"
  with sqlite3.connect(data_files[database_file]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result[0]["FacilityID"]


@anvil.server.callable
def query_overseer(facility_id : int):
  query = f"SELECT * FROM Overseer WHERE FacilityID={facility_id};"
  with sqlite3.connect(data_files[database_file]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]


@anvil.server.callable
def query_site_name(site_id: int):
  query = f"SELECT location FROM Facility WHERE FacilityID={site_id};"
  with sqlite3.connect(data_files[database_file]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result

@anvil.server.callable
def delete_overseer(overseer_id : int):
  query = f"DELETE FROM Overseer WHERE OverseerID={overseer_id};"
  with sqlite3.connect(data_files[database_file]) as conn:
    cur = conn.cursor()
    cur.execute(query)


@anvil.server.callable
def insert_overseer(Firstname: str, Lastname: str, Clearance : int, site_id : int):
  query = f"INSERT INTO Overseer (Firstname, Lastname, Clearance, FacilityID) VALUES ('{Firstname}', '{Lastname}', {Clearance}, {site_id});"
  with sqlite3.connect(data_files[database_file]) as conn:
    cur = conn.cursor()
    cur.execute(query)

@anvil.server.callable
def query_security_systems(reactor_id : int):
  query = f"SELECT * FROM SafetySystems WHERE ReactorID={reactor_id};"
  with sqlite3.connect(data_files[database_file]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def update_security_status(security_system_id : int, toggle_value : int):
  query = f"UPDATE SafetySystems SET Status={toggle_value} WHERE SaftySystemsID={security_system_id};"
  with sqlite3.connect(data_files[database_file]) as conn:
    cur = conn.cursor()
    cur.execute(query)

@anvil.server.callable
def query_towers(reactor_id: int):
  query = f"SELECT CoolingTowerID FROM CoolingTower WHERE ReactorID={reactor_id};"
  with sqlite3.connect(data_files[database_file]) as conn:
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return result


@anvil.server.callable
def query_tower_data(tower_id : int):
  query = f"SELECT StatusPrim, StatusSec, Pressure, FlowRate FROM CoolingTower WHERE CoolingTowerID={tower_id};"
  with sqlite3.connect(data_files[database_file]) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    result = cur.execute(query).fetchall()
  return [dict(row) for row in result]

@anvil.server.callable
def update_prim_status(tower_id : int, toggle_value : int):
  query = f"UPDATE CoolingTower SET StatusPrim={toggle_value} WHERE CoolingTowerID={tower_id};"
  with sqlite3.connect(data_files[database_file]) as conn:
    cur = conn.cursor()
    cur.execute(query)

@anvil.server.callable
def update_sec_status(tower_id : int, toggle_value : int):
  query = f"UPDATE CoolingTower SET StatusSec={toggle_value} WHERE CoolingTowerID={tower_id};"
  with sqlite3.connect(data_files[database_file]) as conn:
    cur = conn.cursor()
    cur.execute(query)