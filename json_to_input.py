import json

# Mapowanie nazw dróg na ID
road_name_to_id = {
    "stachiewicza": 0,
    "wybickiego": 1,
    "wroclawska": 2,
    "radzikowskiego": 3
}

# Domyślne linie dojazdowe i wyjazdowe dla uproszczenia
default_inbound_lanes = {
    0: 0.1,
    1: 1.1,
    2: 2.2,
    3: 3.1
}

default_outbound_lanes = {
    0: 0.0,
    1: 1.0,
    2: 2.0,
    3: 3.0
}

# Wczytanie commands.json
with open("commands.json", "r") as file:
    data = json.load(file)

lines = []
for cmd in data["commands"]:
    if cmd["type"] == "addVehicle":
        vehicle_id = cmd["vehicleId"]
        start = road_name_to_id[cmd["startRoad"].lower()]
        end = road_name_to_id[cmd["endRoad"].lower()]
        from_lane = default_inbound_lanes[start]
        to_lane = default_outbound_lanes[end]
        lines.append(f"ADD {vehicle_id} {{{from_lane}, {to_lane}}}")
    elif cmd["type"] == "step":
        lines.append("STEP")
        
with open("input.txt", "w") as f:
    f.write("\n".join(lines))

print("✅ Wygenerowano input.txt na podstawie commands.json")
