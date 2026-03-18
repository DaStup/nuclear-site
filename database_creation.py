import sqlite3

# Verbindung zur SQLite-Datenbank herstellen (Datei wird erstellt falls sie nicht existiert)
conn = sqlite3.connect("nuclear_facility.db")
cursor = conn.cursor()

# Foreign Keys aktivieren (wichtig bei SQLite!)
cursor.execute("PRAGMA foreign_keys = ON;")

# ------------------------
# Tabelle: Facility
# ------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Facility (
    FacilityID INTEGER PRIMARY KEY,
    location VARCHAR(100)
);
""")

# ------------------------
# Tabelle: Reactor
# ------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Reactor (
    ReactorID INTEGER PRIMARY KEY,
    Pressure DOUBLE,
    Temperature DOUBLE,
    NeutronFlux DOUBLE,
    ControlRodPos INTEGER,
    FacilityID INTEGER,
    FOREIGN KEY (FacilityID) REFERENCES Facility(FacilityID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
""")

# ------------------------
# Tabelle: CoolingTower
# ------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS CoolingTower (
    CoolingTowerID INTEGER PRIMARY KEY,
    FlowRate INTEGER,
    StatusPrim INTEGER,
    StatusSec INTEGER,
    Pressure DOUBLE,
    ReactorID INTEGER,
    FOREIGN KEY (ReactorID) REFERENCES Reactor(ReactorID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
""")

# ------------------------
# Tabelle: SafetySystems
# ------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS SafetySystems (
    SaftySystemsID INTEGER PRIMARY KEY,
    Type VARCHAR(100),
    InstallDate DATE,
    Status INTEGER,
    ReactorID INTEGER,
    FOREIGN KEY (ReactorID) REFERENCES Reactor(ReactorID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
""")

# ------------------------
# Tabelle: Overseer
# ------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS Overseer (
    OverseerID INTEGER PRIMARY KEY,
    Firstname VARCHAR(100),
    Lastname VARCHAR(100),
    Clearance INTEGER,
    FacilityID INTEGER,
    FOREIGN KEY (FacilityID) REFERENCES Facility(FacilityID)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
""")

# Änderungen speichern und Verbindung schließen
conn.commit()
conn.close()

print("Datenbank und Tabellen erfolgreich erstellt.")