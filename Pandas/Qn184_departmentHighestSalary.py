import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(
        department,
        how='inner',
        left_on='departmentId',
        right_on='id',
        suffixes=('_e', '_d')
    )

    merged_df['rank'] = merged_df.groupby('departmentId')['salary'].rank(method='dense', ascending=False)
    result = merged_df[merged_df['rank'] == 1]
    result = result[['name_d', 'name_e', 'salary']].rename(
        columns ={'name_d': 'Department', 'name_e': 'Employee', 'salary': 'Salary'}
    )
    return result
    

