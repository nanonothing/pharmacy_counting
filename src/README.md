This is the directory where your source code would reside.<br/>
# Project: Pharmacy Counting <br/>
## Purpose<br/>
## Demo Instruction<br/>
The script pharmcy_counting.py is written in Python 3.7.2.
## Input data<br/>
 The input data will be a text file provides information on prescription drugs prescribed by individual physicians and other health care providers. <br/>
 Each line of this file contain these fields:<br/>
 * Id: Identitiy number of the prescribers
 * Last_name: last name of the prescribers
 * First_name: first name of the prescribers
 * drug_name: drug name of the prescription
 * cost: Cost of the medication
## Output data<br/>
Each line of this file contain these fields:<br/>

* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers<br/>

The data will be sorted in the descending order according to the total cost of the drug.
