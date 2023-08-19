import pandas as pd

master_csv = pd.read_csv('C:/Users/softy/DataEngineer/Data-Engineer-mini-projects/Data Sets/master.csv')
slave_csv = pd.read_csv('C:/Users/softy/DataEngineer/Data-Engineer-mini-projects/Data Sets/slave.csv')
print(master_csv)
master_pass = master_csv[master_csv["RESULTS"].str[-4:] == "Pass"]
master_fail = master_csv[master_csv["RESULTS"].str[-4:] == "Fail"]
master_slave_csv = slave_csv.merge(master_csv,
                                   how='left',
                                   right_on='POD_NAME',
                                   left_on='name')

master_result = master_slave_csv[['name', 'POD_VERSION', 'POD_TYPE', 'RESULTS']].copy()

master_result.rename(columns={'name': 'POD_NAME'}, inplace=True)

print(master_result)

master_fail.to_csv('C:/Users/softy/DataEngineer/Data-Engineer-mini-projects/Data Sets/master_fail.csv')
master_result.to_csv('C:/Users/softy/DataEngineer/Data-Engineer-mini-projects/Data Sets/master_result.csv')
