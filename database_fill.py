import sqlite3
from datetime import date

conn = sqlite3.connect("nuclear_facility.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

# ------------------------
# Facility Daten
# ------------------------
facilities = [
    (1, "Berlin"),
    (2, "Hamburg"),
    (3, "München"),
    (4, "Wien"),
    (5, "Zürich")
]

cursor.executemany("INSERT INTO Facility VALUES (?, ?);", facilities)

# ------------------------
# Reactor Daten
# ------------------------
reactors = [
    (1, 155.2, 320.5, 1.2e14, 75, 1),
    (2, 160.1, 330.0, 1.5e14, 60, 1),
    (3, 150.0, 310.2, 1.1e14, 80, 2),
    (4, 170.3, 340.8, 1.7e14, 55, 3),
    (5, 165.5, 335.5, 1.6e14, 65, 4),
    (6, 158.8, 325.0, 1.3e14, 70, 5)
]

cursor.executemany("INSERT INTO Reactor VALUES (?, ?, ?, ?, ?, ?);", reactors)

# ------------------------
# CoolingTower Daten
# ------------------------
cooling_towers = [
    (1, 500, 1, 1, 10.5, 1),
    (2, 550, 1, 0, 11.0, 1),
    (3, 480, 1, 1, 10.2, 2),
    (4, 600, 0, 1, 12.5, 3),
    (5, 620, 1, 1, 12.0, 4),
    (6, 580, 1, 0, 11.8, 5),
    (7, 530, 1, 1, 10.9, 6)
]

cursor.executemany("INSERT INTO CoolingTower VALUES (?, ?, ?, ?, ?, ?);", cooling_towers)

# ------------------------
# SafetySystems Daten
# ------------------------
safety_systems = [
    (1, "Emergency Cooling", "2020-01-15", 1, 1),
    (2, "Radiation Shield", "2019-06-20", 1, 1),
    (3, "Fire Suppression", "2021-03-10", 1, 2),
    (4, "Backup Power", "2018-11-05", 0, 3),
    (5, "Containment", "2022-07-22", 1, 4),
    (6, "Emergency Cooling", "2023-02-14", 1, 5),
    (7, "Radiation Shield", "2020-09-09", 1, 6)
]

cursor.executemany("INSERT INTO SafetySystems VALUES (?, ?, ?, ?, ?);", safety_systems)

# ------------------------
# Overseer Daten
# ------------------------
overseers = [
    (1, "Anna", "Schmidt", 5, 1),
    (2, "Max", "Müller", 4, 1),
    (3, "Laura", "Weber", 3, 2),
    (4, "Paul", "Fischer", 5, 3),
    (5, "Sophie", "Wagner", 4, 4),
    (6, "Lukas", "Becker", 2, 5)
]

cursor.executemany("INSERT INTO Overseer VALUES (?, ?, ?, ?, ?);", overseers)

conn.commit()
conn.close()

print("Testdaten erfolgreich eingefügt.")