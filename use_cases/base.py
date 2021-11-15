from vnc_api import vnc_api


class Sample(object):

    def __init__(self, api_cli):
        self.domain_name = 'default-domain'
        self.project_name = 'admin'
        self.subnet_cidr = '192.168.1.0/24'
        self.api_cli = api_cli

    def get_default_domain_obj(self):
        print "use default domain: [%s]." % self.domain_name
        return self.api_cli.domain_read(fq_name=[self.domain_name])

    def get_admin_project_obj(self):
        print "use admin project [%s]." % self.project_name
        return self.api_cli.project_read(fq_name=[self.domain_name,
                                                  self.project_name])

    def get_subnet_type(self):
        print "setup a subnet type, CIDR [%s]." % self.subnet_cidr
        prefix, prefix_len = self.subnet_cidr.split('/')
        return vnc_api.SubnetType(ip_prefix=prefix,
                                  ip_prefix_len=int(prefix_len))
