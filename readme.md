
# <center> <u> SeedTools </u>  </center>

- while doing Machine learning projects , not able to load data fast enough ?

- tired of writing same code again and again for same datasets 

**seedtools** is a Python utility package for reading, versioning, and managing seed data files — especially useful for machine learning projects, database seeding, and automated data workflows.

<u> Here is our Solution </u> 👍

- just make a directory which contains all the datasets and use it anywhere across the pc 




### Features

- 🔄 Load and preprocess versioned seed data files
- 📁 Supports CSV and other tabular formats
- 🔍 Easily inspect, debug, and manage seed data across versions

### Installation

```bash
pip install seedtools

```

### SET `Data Path` once and use it anywhere 

``` python
from seedtools import configure_data_path, reset_path

reset_path() # default path 
configure_data_path("you path")
```

## How to load data from directory 

``` python 
from seedtools import load_seed
data = load_seed("data_science_jobs.csv")
print(data.data)
```


**If  already have version**

``` python 
data = load_seed("data_science_jobs.csv","v2")
print(data.data)
```


## How to register it first ?

``` python 
data = load_seed("data_science_jobs.csv")
data.register(desc="wonderful_dataset") # will create a seed file in same dir 
```


## How to register version ?

``` python 
data = load_seed("data_science_jobs.csv")
data.register_version("v_name",drop_cols=["col1","col2"],cols_maps={"Gender":"auto","City":{"London":1."Delhi":0}})  
# will register in the seed file 
# auto will convert gender = > Male :  1 , female : 0
# you can make custom mapping also 
```


## How to Check Available Versions ? 
``` python 
data = load_seed("data_science_jobs.csv")
print(data.versions_list())
``` 

## How to check seed File (rarely needed) ?

``` python 
data = load_seed("data_science_jobs.csv")
print(data.seed_file())
``` 


## Terminate Version 

``` python 
data = load_seed("data_science_jobs.csv")
data.terminate_version("v3")
```


