import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Create Synthetic Customers
cust_data = {
    'customer_id': [f'cust_{i}' for i in range(1, 101)],
    'customer_unique_id': [f'unique_{i % 20}' for i in range(1, 101)], # Some repeat customers
    'customer_city': np.random.choice(['Sao Paulo', 'Rio', 'Curitiba'], 100)
}
pd.DataFrame(cust_data).to_csv('olist_customers_dataset.csv', index=False)

# 2. Create Synthetic Orders
order_data = {
    'order_id': [f'order_{i}' for i in range(1, 101)],
    'customer_id': [f'cust_{i}' for i in range(1, 101)],
    'order_purchase_timestamp': [datetime.now() - timedelta(days=np.random.randint(1, 365)) for _ in range(100)],
    'order_status': 'delivered'
}
pd.DataFrame(order_data).to_csv('olist_orders_dataset.csv', index=False)

# 3. Create Synthetic Payments
pay_data = {
    'order_id': [f'order_{i}' for i in range(1, 101)],
    'payment_value': np.random.uniform(20, 500, 100),
    'payment_type': 'credit_card'
}
pd.DataFrame(pay_data).to_csv('olist_order_payments_dataset.csv', index=False)

print("✅ Success! 3 CSV files created in your folder.")