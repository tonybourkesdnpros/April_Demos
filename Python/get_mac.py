import pyeapi

switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4']
pyeapi.load_config('eapi.conf')

for switch in switches:
    connect = pyeapi.connect_to(switch)
    cmd_result = connect.enable(['show mac address-table'])
    for mac in cmd_result[0]['result']['unicastTable']['tableEntries']:
        print(mac['macAddress'])
