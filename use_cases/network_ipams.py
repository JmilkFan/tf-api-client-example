import uuid

from vnc_api import vnc_api

import base


def create_ipam_with_flat_subnet(conf_file):

    api_cli = vnc_api.VncApi(conf_file=conf_file)

    sample = base.Sample(api_cli)
    project_o = sample.get_admin_project_obj()
    subnet_t = sample.get_subnet_type()

    # IPAM Subnet Type
    print("setup a ipam subnet type.")
    ipam_subnet_t = vnc_api.IpamSubnetType(subnet=subnet_t)

    # IPAM Subnets Type
    ipam_subnets_t = vnc_api.IpamSubnets(subnets=[ipam_subnet_t])

    # Network IPAM Type
    print("setup a ipam type.")
    ipam_t = vnc_api.IpamType(ipam_method='dhcp', cidr_block=subnet_t)

    # Create Network IPAM Object
    ipam_name = str(uuid.uuid4())
    print("create network ipam [%s]", ipam_name)
    ipam_o = vnc_api.NetworkIpam(name=ipam_name,
                                 parent_obj=project_o,
                                 network_ipam_mgmt=ipam_t,
                                 ipam_subnets=ipam_subnets_t,
                                 ipam_subnet_method='flat-subnet')
    api_cli.network_ipam_create(ipam_o)

    ipam_o = api_cli.network_ipam_read(fq_name=[sample.domain_name,
                                                sample.project_name,
                                                ipam_name])
    print(ipam_o.dump())

    return ipam_o


def create_ipam_with_user_defined_subnet(conf_file):

    api_cli = vnc_api.VncApi(conf_file=conf_file)

    sample = base.Sample(api_cli)
    project_o = sample.get_admin_project_obj()

    # Network IPAM Type
    print("setup a ipam type.")
    ipam_t = vnc_api.IpamType(ipam_method='dhcp')

    # Create Network IPAM Object
    ipam_name = str(uuid.uuid4())
    print("create network ipam [%s]", ipam_name)
    ipam_o = vnc_api.NetworkIpam(name=ipam_name,
                                 parent_obj=project_o,
                                 network_ipam_mgmt=ipam_t,
                                 ipam_subnet_method='user-defined-subnet')
    api_cli.network_ipam_create(ipam_o)

    ipam_o = api_cli.network_ipam_read(fq_name=[sample.domain_name,
                                                sample.project_name,
                                                ipam_name])
    print(ipam_o.dump())

    return ipam_o
