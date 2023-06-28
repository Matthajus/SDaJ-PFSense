from dotenv import load_dotenv
import os
import ssl
from pfsense.tools.w3sa_convertor import parse_w3sa_json_file
from pfsense.controller.PFSenseController import *


def create_http_context():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context


if __name__ == '__main__':
    create_http_context()
    w3sa_data = parse_w3sa_json_file('w3sa_priklad_pre_vlan196.json')

    for item in w3sa_data:
        print(item)

    get_static_mapping()
    # delete_static_mapping(2)

    # this will fail, ip address must be within interface subnet
    # create_st_mp(w3sa_data[0]['mac'], w3sa_data[0]['addr'], w3sa_data[0]['domain_name'], w3sa_data[0]['name'])

    # if you don't want to update any param, put None value
    update_static_mapping(0, 'ea:4a:45:29:44:19', '10.0.0.37', None, 'username')
