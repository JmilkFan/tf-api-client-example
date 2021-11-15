# tf-api-client-example

Example of tf-api-client SDK

# How to use

```bash
$ git clone https://github.com/JmilkFan/tf-api-client-example.git

# edit the config file
$ cp etc/contrail/vnc_api_lib.ini.sample etc/contrail/vnc_api_lib.ini

# help
$ python tf-api-client-example.py -h
Usage: python2 tf-api-client-example.py [options] argv

Options:
  -h, --help            show this help message and exit
  -c CONF_FILE, --config=CONF_FILE
                        Input the config file path of api client.
  -u USE_CASE, --use-case=USE_CASE
                        Choice the use case.

# Execute one of the use cases as below
$ python tf-api-client-example.py -c etc/contrail/vnc_api_lib.ini -u test
Usage: python2 tf-api-client-example.py [options] argv

tf-api-client-example.py: error: option -u: invalid choice: 'test' (choose from 'create_virtal_network_with_user_defined_subnet', 'create_ipam_with_flat_subnet', 'create_ipam_with_user_defined_subnet', 'create_virtal_network_with_flat_subnet')
```
