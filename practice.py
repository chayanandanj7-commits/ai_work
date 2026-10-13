import requests
import pandas as pd
url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url, timeout=15)
response.raise_for_status()


users = response.json()

print(response.json())

df=pd.DataFrame(users)
max=df["id"].max()
print(f"the total number of ids : {max}")
names=[]

names=df["name"]
print(names)
print(df["name"])
print(df["address"][2])

if(df["name"]=="Bret"):
    print(df["name"]["Bret"])
    
    
    
for user in users:
    print("Name:", user["name"])
    print("Email:", user["email"])
    print("-------------------")