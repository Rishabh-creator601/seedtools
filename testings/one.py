from dotenv import load_dotenv ,set_key,find_dotenv
import os
    
    
file =  find_dotenv()

load_dotenv(find_dotenv())

set_key(file,"key","value")