import json


def correct_ip_address(ip_address):
    parts = ip_address.split('.')
    parts = [str(int(part)) for part in parts]
    corrected_ip = '.'.join(parts)
    return corrected_ip


def parse_w3sa_json_file(json_file):
    with open(json_file, 'r') as file:
        json_data = json.load(file)

    result = []

    for obj in json_data:
        for ip_obj in obj['ip_obj']:
            result.append({
                'mac': ip_obj['mac'],
                'name': ip_obj['name'],
                'domain_name': ip_obj['domain_obj']['name'],
                'addr': correct_ip_address(ip_obj['_addr'])
            })

    return result
