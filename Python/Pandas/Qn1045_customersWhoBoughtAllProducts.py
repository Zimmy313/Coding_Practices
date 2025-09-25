import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    total_product = product['product_key'].nunique()
    
    counts = customer.groupby('customer_id')['product_key'].nunique()
    valid = counts[counts == total_product]
    result = valid.reset_index()[['customer_id']]
    
    return result
    
    
    
    