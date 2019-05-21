# Cisco ASA Configuration Tool
This tool will read a JSON configuration file and a base configuration template and then produce a valid configuration which can be pasted into a **NEW!** Cisco ASA 5506 device. **This tool is only meant to work with a default ASA 5506 configuration. Do not use with a production system!**

## Configuration
The program reads from a JSON file. Here is the example config file.
```json
{
    "hostname": "bob",
    "fqdn": "fw.bobs-domain.com",
    "domain_name": "bobs-domain",
    "enable_pw": "enable123",
    "outside_ip": "1.1.1.1",
    "outside_netmask": "255.255.255.252",
    "inside_ip": "192.168.1.1",
    "inside_network": "192.168.1.0",
    "inside_netmask": "255.255.255.0",
    "inet_gateway": "1.1.1.2",
    "dns_server": "8.8.8.8",
    "dhcp_start": "192.168.1.100",
    "dhcp_end": "192.168.1.200",
    "admin_password": "a_super_secure_password_should_be_here"
}
```
All of these parameters must be filled out, otherwise there will be errors in the output configuration. The configuration file is quite self-explanatory, but one thing to note is:
```json
    "inside_ip": "192.168.1.1",
    "inside_network": "192.168.1.0",
```
The ```inside_ip``` is the IP address of the ASA's inside interface. The ```inside_network``` is the network address of the network on which the ASA's inside interface resides. Note that the only difference between the two here is that the inside_network has a _**0**_ as the last digit where the inside_ip has a _**1**_. In almost all cases, the inside_network address will end with a _**0**_

## Usage
To use the tool, ensure that [asa-deploy.py](asa-deploy.py), [base-config.txt](base-config.txt) and [asa-config.json](asa-config.json) are all in the same directory. 
###### Then run 
``` python asa-deploy.py ```

The result will be a file named ```outlook.txt```. It is the contents of this file that can be pasted into the new ASA 5506.
