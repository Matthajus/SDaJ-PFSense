from pfsense.service.static_mapping_service import *


def get_static_mapping():
    get_all_st_mp()


def delete_static_mapping(st_mp_id):
    delete_st_mp(st_mp_id)


def create_static_mapping(mac, ipaddr, descr, hostname):
    create_st_mp(mac, ipaddr, descr, hostname)


def update_static_mapping(st_mp_id, mac, ipaddr, descr, hostname):
    update_st_mp(st_mp_id, mac, ipaddr, descr, hostname)
