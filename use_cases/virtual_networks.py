import uuid

from vnc_api import vnc_api

import base
import network_ipams


def create_virtal_network_with_flat_subnet(conf_file):
    api_cli = vnc_api.VncApi(conf_file=conf_file)

    sample = base.Sample(api_cli)
    project_o = sample.get_admin_project_obj()
    ipam_o = network_ipams.create_ipam_with_flat_subnet(conf_file)

    # Virtual Network Type, Setup forwarding mode L3 Only,
    # flat-subnet is allowed only with l3 network
    vn_t = vnc_api.VirtualNetworkType(forwarding_mode='l3')

    # Create Virtual Network Object
    vn_name = str(uuid.uuid4())
    print("create virtual network [%s]", vn_name)
    vn_o = vnc_api.VirtualNetwork(name=vn_name,
                                  parent_obj=project_o,
                                  virtual_network_properties=vn_t)

    # Get Flat IPAM Subnet Type form IPAM Object will be OK.
    vn_o.set_network_ipam(ref_obj=ipam_o, ref_data=vnc_api.VnSubnetsType())
    api_cli.virtual_network_create(vn_o)

    vn_o = api_cli.virtual_network_read(fq_name=[sample.domain_name,
                                                 sample.project_name,
                                                 vn_name])
    vn_o.dump()


def create_virtal_network_with_user_defined_subnet(conf_file):
    api_cli = vnc_api.VncApi(conf_file=conf_file)

    sample = base.Sample(api_cli)
    project_o = sample.get_admin_project_obj()
    ipam_o = network_ipams.create_ipam_with_user_defined_subnet(conf_file)

    # Create defined Subnet Type.
    subnet_t = sample.get_subnet_type()
    ipam_subnet_t = vnc_api.IpamSubnetType(subnet=subnet_t)
    vn_subnet_t = vnc_api.VnSubnetsType(ipam_subnets=[ipam_subnet_t])

    # Virtual Network Type, Setup forwarding mode L2 Only.
    vn_t = vnc_api.VirtualNetworkType(forwarding_mode='l2')

    # Create Virtual Network Object
    vn_name = str(uuid.uuid4())
    print("create virtual network [%s]", vn_name)
    vn_o = vnc_api.VirtualNetwork(name=vn_name,
                                  parent_obj=project_o,
                                  virtual_network_properties=vn_t)
    vn_o.set_network_ipam(ref_obj=ipam_o, ref_data=vn_subnet_t)
    api_cli.virtual_network_create(vn_o)

    vn_o = api_cli.virtual_network_read(fq_name=[sample.domain_name,
                                                 sample.project_name,
                                                 vn_name])
    vn_o.dump()
