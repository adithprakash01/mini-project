import pandas as pd
import numpy as np

# Generate synthetic sales data
np.random.seed(0)
data = {
    'Date': pd.date_range(start='2022-01-01', end='2022-12-31'),
    'Revenue': np.random.randint(1000, 5000, size=365),
    'Advertising': np.random.randint(50, 200, size=365),
    'Price': np.random.randint(10, 50, size=365)
}

# Create a DataFrame
sales_data = pd.DataFrame(data)

# Save the DataFrame to a CSV file
sales_data.to_csv('sales_data.csv', index=False)
