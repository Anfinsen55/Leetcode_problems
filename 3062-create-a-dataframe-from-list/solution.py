import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    colum_name=['student_id','age']
    data= pd.DataFrame(student_data, columns=colum_name)
    return data
    
