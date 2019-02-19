#programming in Python 3.7.2
import pandas as pd
import numpy as np
import urllib, csv , operator


loc="../input/itcont.cvs"
Pharm=pd.read_csv(loc)
Pharm.columns = ["id", "Last_Name", "First_Name", "drug_name", "drug_cost"]

#find the number of rows in the list
#row_count = sum(1 for row in Pharm)

#define class to store drug name, number of prescriber and total cost
class drug:
    def __init__(self, name ,cost):
        self.name=name
        self.num_prescriber=1
        self.total_cost=cost

#drug_list: use this dictionary to store all distinct drugs
#drug_count: index of distinct drugs
drug_count=0        
drug_list={drug_count:"drug name"}        

#output_data: list of all drug class element
output_data=[]
output_data.append(drug("drug name",0))

#read the input data row by row
for index, row in Pharm.iterrows():
    x=row["drug_name"]
#if the drug name already appeared in previous row, add 1 to number of prescriber
# and add drug cost to total cost
    if x in drug_list.values():
       output_data[drug_count].num_prescriber=output_data[drug_count].num_prescriber+1
       output_data[drug_count].total_cost=output_data[drug_count].total_cost+row["drug_cost"]
#if the drug name is new, creat new class object drug(x,cost) and update drug_count,drug_list
    else:
        drug_count=drug_count+1
        output_data.append(drug(x, row["drug_cost"]))
        drug_list.update({drug_count:x})
       

#sorted the output_data according to the total_cost value in descending order
sorted_data=sorted(output_data, key=operator.attrgetter('total_cost'),reverse=True)

#write the sorted_data into the text file row by row
f=open('pharmacy_counting/output/top_cost_drug.txt','w')
f.write("drug_name,num_prescriber,total_cost\n")
for i in range(drug_count): 
    f.write(sorted_data[i].name+','+'%d'%sorted_data[i].num_prescriber+','+'%d' %sorted_data[i].total_cost+'\n')
f.close()
   

        
   
