

import pandas as pd
import os ,sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from seedtools import return_data_path, configure_data_path,load_seed 



dataset_name = "data_science_job.csv"



data =  load_seed(dataset_name).data

print(data)


# # readed_data = read_seed(dataset_name)

# # print(readed_data)    

# # not_registered = []

# # for i in list_all_files("csv"):
# #     data =  pd.read_csv(i)
# #     try :
# #         register_csv(data,i,desc="Data Description is not yed provided")
# #     except:
# #         not_registered.append(i)



# # print("-"*100)
# # print(not_registered)
