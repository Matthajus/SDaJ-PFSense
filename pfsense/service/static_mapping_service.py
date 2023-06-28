import http.client
import json
from pfsense.model.AuthUser import get_auth_user

AUTH_USER = get_auth_user()
URL = '/api/v1/services/dhcpd/static_mapping'


def prepare_payload():
    return {
        'client-id': AUTH_USER['user'],
        'client-token': AUTH_USER['password'],
        'interface': 'lan'
    }


def prepare_header():
    return {
        'Content-Type': 'application/json'
    }


def handle_request(http_method, header, payload):
    conn = http.client.HTTPSConnection(AUTH_USER['host'])
    conn.request(http_method, URL, payload, header)
    res = conn.getresponse()
    data = res.read()
    obj = json.loads(data.decode('utf-8'))
    json_formatted_str = json.dumps(obj, indent=4)
    print(json_formatted_str)


def get_all_st_mp():
    prepared_payload = prepare_payload()
    payload = json.dumps(prepared_payload)
    header = prepare_header()
    handle_request('GET', header, payload)


def delete_st_mp(st_mp_id):
    prepared_payload = prepare_payload()
    prepared_payload['id'] = st_mp_id
    payload = json.dumps(prepared_payload)
    header = prepare_header()
    handle_request("DELETE", header, payload)


def create_st_mp(mac, ipaddr, descr, hostname):
    prepared_payload = prepare_payload()
    prepared_payload['mac'] = mac
    prepared_payload['ipaddr'] = ipaddr
    prepared_payload['descr'] = descr
    prepared_payload['hostname'] = hostname
    payload = json.dumps(prepared_payload)
    header = prepare_header()
    handle_request("POST", header, payload)


def update_st_mp(st_mp_id, mac, ipaddr, descr, hostname):
    prepared_payload = prepare_payload()
    prepared_payload['id'] = st_mp_id
    prepared_payload['mac'] = mac
    prepared_payload['ipaddr'] = ipaddr
    prepared_payload['descr'] = descr
    prepared_payload['hostname'] = hostname
    payload = json.dumps(prepared_payload)
    header = prepare_header()
    handle_request("PUT", header, payload)
