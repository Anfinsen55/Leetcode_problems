import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    df=pd.DataFrame(students)
    df=df[df['student_id']==101]
    df=df[['name','age']]
    return df
