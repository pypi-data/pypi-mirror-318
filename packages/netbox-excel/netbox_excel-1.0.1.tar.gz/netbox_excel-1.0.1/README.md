# netbox-excel
Plugin import file excel cho netbox, dùng để import device, ip, rack ....


## Install Require

netbox version >= 4.0

## Known Issues

- WARNING: This plugin is only tested with a single NetBox version at this time.

## Installation Guide

### In mono service:

To install the plugin, first using pip and install netbox-excel:

   ```
   cd /opt/netbox
   source venv/bin/activate
   pip install netbox-excel
   ```

Package requirements.txt
   ```
   pip install openpyxl pandas
   ```


Next, enable the plugin in /opt/netbox/netbox/netbox/configuration.py, or if you have a /configuration/plugins.py file, the plugins.py file will take precedence.

   ```
   PLUGINS = [
      'netbox_excel'
   ]
   ```