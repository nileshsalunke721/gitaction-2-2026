import pandas as pd 


def extraction():
    data = {
    "id":[1, 2, 3],
    "name":["John", "Jane", "Doe"],
    "age":[25, 30, 35]
    }

    df = pd.DataFrame(data) 
    print(df)

extraction()