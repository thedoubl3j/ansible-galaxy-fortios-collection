#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
# Copyright 2019-2020 Fortinet, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fortios_firewall_shaper_per_ip_shaper
short_description: Configure per-IP traffic shaper in Fortinet's FortiOS and FortiGate.
description:
    - This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the
      user to set and modify firewall_shaper feature and per_ip_shaper category.
      Examples include all parameters and values need to be adjusted to datasources before usage.
      Tested with FOS v6.2.0
version_added: "2.8"
author:
    - Link Zheng (@chillancezen)
    - Jie Xue (@JieX19)
    - Hongbin Lu (@fgtdev-hblu)
    - Frank Shen (@frankshen01)
    - Miguel Angel Munoz (@mamunozgonzalez)
    - Nicolas Thomas (@thomnico)
notes:
    - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

requirements:
    - ansible>=2.9.0
options:
    access_token:
        description:
            - Token-based authentication.
              Generated from GUI of Fortigate.
        type: str
        required: false
    vdom:
        description:
            - Virtual domain, among those defined previously. A vdom is a
              virtual instance of the FortiGate that can be configured and
              used as a different unit.
        type: str
        default: root

    state:
        description:
            - Indicates whether to create or remove the object.
              This attribute was present already in previous version in a deeper level.
              It has been moved out to this outer level.
        type: str
        required: false
        choices:
            - present
            - absent
        version_added: 2.9
    firewall_shaper_per_ip_shaper:
        description:
            - Configure per-IP traffic shaper.
        default: null
        type: dict
        suboptions:
            state:
                description:
                    - B(Deprecated)
                    - Starting with Ansible 2.9 we recommend using the top-level 'state' parameter.
                    - HORIZONTALLINE
                    - Indicates whether to create or remove the object.
                type: str
                required: false
                choices:
                    - present
                    - absent
            bandwidth_unit:
                description:
                    - Unit of measurement for maximum bandwidth for this shaper (Kbps, Mbps or Gbps).
                type: str
                choices:
                    - kbps
                    - mbps
                    - gbps
            diffserv_forward:
                description:
                    - Enable/disable changing the Forward (original) DiffServ setting applied to traffic accepted by this shaper.
                type: str
                choices:
                    - enable
                    - disable
            diffserv_reverse:
                description:
                    - Enable/disable changing the Reverse (reply) DiffServ setting applied to traffic accepted by this shaper.
                type: str
                choices:
                    - enable
                    - disable
            diffservcode_forward:
                description:
                    - Forward (original) DiffServ setting to be applied to traffic accepted by this shaper.
                type: str
            diffservcode_rev:
                description:
                    - Reverse (reply) DiffServ setting to be applied to traffic accepted by this shaper.
                type: str
            max_bandwidth:
                description:
                    - Upper bandwidth limit enforced by this shaper (0 - 16776000). 0 means no limit. Units depend on the bandwidth-unit setting.
                type: int
            max_concurrent_session:
                description:
                    - Maximum number of concurrent sessions allowed by this shaper (0 - 2097000). 0 means no limit.
                type: int
            name:
                description:
                    - Traffic shaper name.
                required: true
                type: str
'''

EXAMPLES = '''
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure per-IP traffic shaper.
    fortios_firewall_shaper_per_ip_shaper:
      vdom:  "{{ vdom }}"
      state: "present"
      access_token: "<your_own_value>"
      firewall_shaper_per_ip_shaper:
        bandwidth_unit: "kbps"
        diffserv_forward: "enable"
        diffserv_reverse: "enable"
        diffservcode_forward: "<your_own_value>"
        diffservcode_rev: "<your_own_value>"
        max_bandwidth: "8"
        max_concurrent_session: "9"
        name: "default_name_10"

'''

RETURN = '''
build:
  description: Build number of the fortigate image
  returned: always
  type: str
  sample: '1547'
http_method:
  description: Last method used to provision the content into FortiGate
  returned: always
  type: str
  sample: 'PUT'
http_status:
  description: Last result given by FortiGate on last operation applied
  returned: always
  type: str
  sample: "200"
mkey:
  description: Master key (id) used in the last call to FortiGate
  returned: success
  type: str
  sample: "id"
name:
  description: Name of the table used to fulfill the request
  returned: always
  type: str
  sample: "urlfilter"
path:
  description: Path of the table used to fulfill the request
  returned: always
  type: str
  sample: "webfilter"
revision:
  description: Internal revision number
  returned: always
  type: str
  sample: "17.0.2.10658"
serial:
  description: Serial number of the unit
  returned: always
  type: str
  sample: "FGVMEVYYQT3AB5352"
status:
  description: Indication of the operation's result
  returned: always
  type: str
  sample: "success"
vdom:
  description: Virtual domain used
  returned: always
  type: str
  sample: "root"
version:
  description: Version of the FortiGate
  returned: always
  type: str
  sample: "v5.6.3"

'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import FortiOSHandler
from ansible_collections.fortinet.fortios.plugins.module_utils.fortios.fortios import check_legacy_fortiosapi
from ansible_collections.fortinet.fortios.plugins.module_utils.fortimanager.common import FAIL_SOCKET_MSG


def filter_firewall_shaper_per_ip_shaper_data(json):
    option_list = ['bandwidth_unit', 'diffserv_forward', 'diffserv_reverse',
                   'diffservcode_forward', 'diffservcode_rev', 'max_bandwidth',
                   'max_concurrent_session', 'name']
    dictionary = {}

    for attribute in option_list:
        if attribute in json and json[attribute] is not None:
            dictionary[attribute] = json[attribute]

    return dictionary


def underscore_to_hyphen(data):
    if isinstance(data, list):
        for i, elem in enumerate(data):
            data[i] = underscore_to_hyphen(elem)
    elif isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_data[k.replace('_', '-')] = underscore_to_hyphen(v)
        data = new_data

    return data


def firewall_shaper_per_ip_shaper(data, fos):
    vdom = data['vdom']
    if 'state' in data and data['state']:
        state = data['state']
    elif 'state' in data['firewall_shaper_per_ip_shaper'] and data['firewall_shaper_per_ip_shaper']['state']:
        state = data['firewall_shaper_per_ip_shaper']['state']
    else:
        state = True
    firewall_shaper_per_ip_shaper_data = data['firewall_shaper_per_ip_shaper']
    filtered_data = underscore_to_hyphen(filter_firewall_shaper_per_ip_shaper_data(firewall_shaper_per_ip_shaper_data))

    if state == "present":
        return fos.set('firewall.shaper',
                       'per-ip-shaper',
                       data=filtered_data,
                       vdom=vdom)

    elif state == "absent":
        return fos.delete('firewall.shaper',
                          'per-ip-shaper',
                          mkey=filtered_data['name'],
                          vdom=vdom)
    else:
        fos._module.fail_json(msg='state must be present or absent!')


def is_successful_status(status):
    return status['status'] == "success" or \
        status['http_method'] == "DELETE" and status['http_status'] == 404


def fortios_firewall_shaper(data, fos):

    if data['firewall_shaper_per_ip_shaper']:
        resp = firewall_shaper_per_ip_shaper(data, fos)
    else:
        fos._module.fail_json(msg='missing task body: %s' % ('firewall_shaper_per_ip_shaper'))

    return not is_successful_status(resp), \
        resp['status'] == "success" and \
        (resp['revision_changed'] if 'revision_changed' in resp else True), \
        resp


def main():
    mkeyname = 'name'
    fields = {
        "access_token": {"required": False, "type": "str", "no_log": True},
        "vdom": {"required": False, "type": "str", "default": "root"},
        "state": {"required": False, "type": "str",
                  "choices": ["present", "absent"]},
        "firewall_shaper_per_ip_shaper": {
            "required": False, "type": "dict", "default": None,
            "options": {
                "state": {"required": False, "type": "str",
                          "choices": ["present", "absent"]},
                "bandwidth_unit": {"required": False, "type": "str",
                                   "choices": ["kbps",
                                               "mbps",
                                               "gbps"]},
                "diffserv_forward": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "diffserv_reverse": {"required": False, "type": "str",
                                     "choices": ["enable",
                                                 "disable"]},
                "diffservcode_forward": {"required": False, "type": "str"},
                "diffservcode_rev": {"required": False, "type": "str"},
                "max_bandwidth": {"required": False, "type": "int"},
                "max_concurrent_session": {"required": False, "type": "int"},
                "name": {"required": True, "type": "str"}

            }
        }
    }

    check_legacy_fortiosapi()
    module = AnsibleModule(argument_spec=fields,
                           supports_check_mode=False)

    versions_check_result = None
    if module._socket_path:
        connection = Connection(module._socket_path)
        if 'access_token' in module.params:
            connection.set_option('access_token', module.params['access_token'])

        fos = FortiOSHandler(connection, module, mkeyname)

        is_error, has_changed, result = fortios_firewall_shaper(module.params, fos)
        versions_check_result = connection.get_system_version()
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    if versions_check_result and versions_check_result['matched'] is False:
        module.warn("Ansible has detected version mismatch between FortOS system and galaxy, see more details by specifying option -vvv")

    if not is_error:
        if versions_check_result and versions_check_result['matched'] is False:
            module.exit_json(changed=has_changed, version_check_warning=versions_check_result, meta=result)
        else:
            module.exit_json(changed=has_changed, meta=result)
    else:
        if versions_check_result and versions_check_result['matched'] is False:
            module.fail_json(msg="Error in repo", version_check_warning=versions_check_result, meta=result)
        else:
            module.fail_json(msg="Error in repo", meta=result)


if __name__ == '__main__':
    main()
