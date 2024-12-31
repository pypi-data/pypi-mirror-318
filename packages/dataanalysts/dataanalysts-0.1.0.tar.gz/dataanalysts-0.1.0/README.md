# DataAnalysts Package

**DataAnalysts** is a Python library designed to simplify and streamline data analysis tasks, including data cleaning, transformation, and visualization. Whether you're a student, a data analyst, or a researcher, this package is built to handle datasets efficiently and interactively.

---

## 🚀 **Key Features**
- 🧹 **Data Cleaning:** Handle missing values, remove duplicates, and preprocess raw datasets.
- 🔄 **Data Transformation:** Scale, normalize, and encode datasets seamlessly.
- 📊 **Data Visualization:** Generate professional plots (Histogram, Line Plot, Scatter Plot, etc.) interactively.
- 📥 **Data Loading:** Easily load datasets from CSV and Excel files.
- 🛡️ **Error Handling:** Robust exception handling with clear error messages.
- 🎮 **Interactive Tools:** Interactive cleaning, transformation, and plotting tools.

---

## 🛠️ **Installation Steps**

### **1. Install the Package from PyPI**
To use the library in Google Colab or your local environment, install it directly from PyPI:

```python
!pip install dataanalysts

Usage Examples

1. Import the Library
import dataanalysts as da
import pandas as pd

2. Load Data
df = da.csv('data.csv')
df_excel = da.excel('data.xlsx', sheet_name='Sheet1')

3. Data Cleaning
df_cleaned = da.clean(df)
df_interactive_clean = da.interactive_clean(df)

4. Data Transformation
df_transformed = da.transform(df, strategy='standard')
df_interactive_transform = da.interactive_transform(df)

5. Data Visualization
da.histogram(df, column='age')
da.barchart(df, x_col='city', y_col='population')
da.interactive_plot(df)


Contributing
Contributions are welcome! Please submit a pull request via our GitHub Repository.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Support
If you encounter any issues, feel free to open an issue on our GitHub Issues page.

