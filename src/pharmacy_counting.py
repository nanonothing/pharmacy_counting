import pandas as pd
import numpy as np
import urllib
import csv
url="https://raw.githubusercontent.com/InsightDataScience/pharmacy_counting/master/insight_testsuite/tests/test_1/input/itcont.txt"
loc="C:\\Users\\G Liu\\Documents\\Python Scripts\\itcont.cvs"
urllib.request.urlretrieve(url, loc)
Pharm=pd.read_csv(loc)
Pharm.columns = ["id", "Last Name", "First Name", "drug Name", "drug cost"]
print(Pharm)
