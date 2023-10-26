import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    #using slicing
    #return employees[:3]
    

    #using head
    return employees.head(3)
    
