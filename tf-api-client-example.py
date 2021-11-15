import optparse
import os
import sys

from use_cases import network_ipams
from use_cases import virtual_networks

USE_CASES = {
    'create_ipam_with_flat_subnet': network_ipams.create_ipam_with_flat_subnet,  # noqa
    'create_ipam_with_user_defined_subnet': network_ipams.create_ipam_with_user_defined_subnet,  # noqa
    'create_virtal_network_with_flat_subnet': virtual_networks.create_virtal_network_with_flat_subnet,  # noqa
    'create_virtal_network_with_user_defined_subnet': virtual_networks.create_virtal_network_with_user_defined_subnet,  # noqa
}


def parse_args():
    """The function define how to use this script and provide help manual.
    """

    usage = "usage: python2 %prog [options] argv"
    p = optparse.OptionParser(usage=usage)

    p.add_option('-c', '--config', dest='conf_file',
                 default='/etc/contrail/vnc_api_lib.ini',
                 help="Input the config file path of api client.")

    p.add_option('-u', '--use-case', action='store', dest='use_case',
                 type='choice', choices=USE_CASES.keys(),
                 help="Choice the use case.")

    options, _ = p.parse_args()

    if (options.conf_file and options.use_case) is None:
        p.error("plase use the help -h | --help")
        sys.exit(1)

    kwargs = {
        'conf_file': options.conf_file,
        'use_case': options.use_case
    }

    return kwargs


def main():
    os.environ['LANG'] = 'en_US.UTF8'

    kwargs = parse_args()
    USE_CASES[kwargs['use_case']](kwargs['conf_file'])


if __name__ == '__main__':
    main()
