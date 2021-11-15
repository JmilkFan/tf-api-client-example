from vnc_api import vnc_api


class VNCAPI(object):

    def __init__(self, api_server_host=None, api_server_port=None,
                 auth_host=None, domain_name=None, tenant_name=None,
                 username=None, password=None, conf_file=None):
        if conf_file:
            self.client = vnc_api.VncApi(conf_file=conf_file)
        else:
            self.client = vnc_api.VncApi(
                auth_host=auth_host,
                api_server_host=api_server_host,
                api_server_port=api_server_port,
                domain_name=domain_name,
                tenant_name=tenant_name,
                username=username,
                password=password)
