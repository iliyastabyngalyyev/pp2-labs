import json

with open("/Users/kydyrtabyngalyyev/Desktop/lb4/Json/sample_data.json", "r") as file:
    data = json.load(file)

interfaces = data["imdata"]
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)


for interface in interfaces:
    attributes = interface["l1PhysIf"]["attributes"]

    dn = attributes["dn"]
    description = attributes["descr"] if attributes["descr"] else "N/A"
    speed = attributes["speed"]  
    mtu = attributes["mtu"]

    print("{:<50} {:<20} {:<10} {:<10}".format(dn, description, speed, mtu))
    