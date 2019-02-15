import pandas as pd
import numpy as np
import urllib, csv

url="https://raw.githubusercontent.com/InsightDataScience/pharmacy_counting/master/insight_testsuite/tests/test_1/input/itcont.txt"
loc="C:\\Users\\G Liu\\Documents\\Python Scripts\\itcont.cvs"
urllib.request.urlretrieve(url, loc)
Pharm=pd.read_csv(loc)
Pharm.columns = ["id", "Last_Name", "First_Name", "drug_name", "drug_cost"]
print(Pharm)
#find the number of rows in the list
row_count = sum(1 for row in Pharm)
drug_count=0
#define class to store drug name, number of prescriber and total cost
class drug:
    def __init__(self, name):
        self.name=name
        self.num_prescriber=0
        self.total_cost=0

#check

drug_list={drug_count:"drug name"}

for index, row in Pharm.iterrows():
    x=row["drug_name"]
    if x in drug_list.values():
       drug(x).num_prescriber=drug(x).num_prescriber+1
       drug(x).total_cost=drug(x).total_cost+row["drug_cost"]
    else:
         drug_count=drug_count+1
         drug(x)
         drug_list.update({drug_count:x})
       
 
 #create x.drug("name")
print(drug_list)
for i in range(drug_count+1):
   x=drug_list[i]
   print(x,drug(x).num_prescriber,drug(x).total_cost) 
   
