import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    # Self-join to match employees with their managers
    df = employees.merge(
        employees[['employee_id', 'name']],
        how='left',
        left_on='reports_to',
        right_on='employee_id',
        suffixes=('_a', '_b')  # a = employee, b = manager
    )

    # Filter out top-level managers (where reports_to is NULL)
    df = df[df['reports_to'].notnull()]

    # Group by manager
    result = (
        df.groupby(['employee_id_b', 'name_b'])
        .agg(
            reports_count=('employee_id_a', 'count'),
            average_age=('age', 'mean')
        )
        .reset_index()
    )

    # Round average_age
    result['average_age'] = result['average_age'].round()

    # Order by employee_id (manager_id)
    result = result.sort_values(by='employee_id_b', ascending=True)

    result = result.rename(columns = {
        'employee_id_b': 'employee_id',
    'name_b': 'name'
    })

    return result