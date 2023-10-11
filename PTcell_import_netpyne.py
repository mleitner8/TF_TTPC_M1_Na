from netpyne import specs
import json

netParams = specs.NetParams()

cell = netParams.importCellParams('PT', 'TTPC_M1_Na_HHTF.py', 'Na1612Model_TF')

out_file = open("Na1216TF", "w")
json.dump(cell, out_file)