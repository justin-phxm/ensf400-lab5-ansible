import ansible_runner
import requests

result = ansible_runner.interface.run(
    private_data_dir='./',
    playbook = "./hello.yml",
    inventory = "./hosts.yml",
)

print(result.stats)

for i in range(3):
    try:
        response = requests.get('http://0.0.0.0')
        if response.ok:
            print(response.text)
        else:
            print(f'Server on failed to respond with status code: {response.status_code}')
    except requests.ConnectionError:
        print(f'Server could not be reached.')
