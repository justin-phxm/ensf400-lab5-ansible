import ansible_runner
import json

# Load inventory
inventory = ansible_runner.get_inventory(action="list", inventories=['./hosts.yml'])
inventory_json = json.loads(inventory[0])  # Assuming the first item is the JSON inventory

# Extract host variables and group details
hostvars = inventory_json['_meta']['hostvars']
groups = inventory_json['all']['children']

# Print host names, IP addresses, and group names
for group_name in groups:
    print(f"\nGroup: {group_name}")
    group_hosts = inventory_json.get(group_name, {}).get('hosts', [])
    for hostname in group_hosts:
        ip_address = hostvars[hostname].get('ansible_host', 'N/A')
        print(f"  Host: {hostname}")
        print(f"    IP Address: {ip_address}")


# Run a ping test on all hosts
print("\nRunning ping test on all hosts...")
r = ansible_runner.run(
    private_data_dir='./',
    inventory="./hosts.yml",
    playbook="./ping.yml",
    container_image='my-nginx-image'

)

# Check and print the results
if r.status == "successful":
    print("Ping test successful for all hosts.")
else:
    print("Ping test failed for one or more hosts.")
