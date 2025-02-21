# vlan_identifier.py

from netmiko import ConnectHandler

# Switch login credentials
switches = {
    "Local_Switch": "10.10.1.24",
    "IT_Network": "10.10.1.30",
    "MGMT_Network": "10.10.1.31",
    "ACCT_Network": "10.10.1.32",
    "User_Network": "10.10.1.22"
}

# Switch connection settings
device_params = {
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "",
    "secret": "",
}

# Loop through switches and retrieve VLAN info
vlan_data = {}

for switch_name, ip in switches.items():
    print(f"Connecting to {switch_name} ({ip})...")
    
    device_params["ip"] = ip
    net_connect = ConnectHandler(**device_params)

    net_connect.enable()

    # Run the command to get VLANs
    output = net_connect.send_command("show vlan brief")

    # Store output
    vlan_data[switch_name] = output

    # Save output to a file
    with open(f"{switch_name}_vlans.txt", "w") as file:
        file.write(output)

    print(f"VLAN information retrieved for {switch_name}")

    # Close connection
    net_connect.disconnect()

print("\nVLAN retrieval complete. Check the generated text files.")

