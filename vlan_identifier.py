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

device_params = {
    "device_type": "cisco_ios",
    "username": "admin",
    "password": "",
    "secret": "",
}

# Dictionary to store VLAN data
vlan_data = {}

for switch_name, ip in switches.items():
    print(f"Connecting to {switch_name} ({ip})...")

    # Update IP address in connection parameters
    device_params["ip"] = ip

    try:
        # Establish connection
        net_connect = ConnectHandler(**device_params)

        net_connect.enable()

        # Run the VLAN command (modify if using Nexus switches)
        output = net_connect.send_command("show vlan brief")

        # Store output
        vlan_data[switch_name] = output

        # Save output to a file
        with open(f"{switch_name}_vlans.txt", "w") as file:
            file.write(output)

        print(f"VLAN information retrieved for {switch_name}")

        # Close connection
        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to connect to {switch_name} ({ip}): {str(e)}")

print("\nVLAN retrieval complete. Check the generated text files.")
