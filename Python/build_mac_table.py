import pyeapi


switches = ['leaf1', 'leaf2', 'leaf3', 'leaf4']
pyeapi.load_config('eapi.conf')
mac_table_set = set()


connect = pyeapi.connect_to('leaf1')
cmd_result = connect.enable('show mac address-table')
print(cmd_result[0]['result']['unicastTable']['tableEntries'])

