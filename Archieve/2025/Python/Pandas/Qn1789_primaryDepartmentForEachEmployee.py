import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    # 1. Count how many departments each employee has
    counts = employee['employee_id'].value_counts()

    # 2. Get IDs of employees who are in only ONE department
    employee_one = counts[counts == 1].index  # <-- FIX: .index, NOT .index()

    # 3. Case 1: Keep all rows for employees with only one department
    df_1 = employee[employee['employee_id'].isin(employee_one)].drop(columns=['primary_flag'])

    # 4. Case 2: For employees with multiple departments, keep only the rows where primary_flag == 'Y'
    df_2 = employee[
        (~employee['employee_id'].isin(employee_one)) & (employee['primary_flag'] == 'Y')
    ].drop(columns=['primary_flag'])

    # 5. Combine both
    result = pd.concat([df_1, df_2], ignore_index=True)
    return result