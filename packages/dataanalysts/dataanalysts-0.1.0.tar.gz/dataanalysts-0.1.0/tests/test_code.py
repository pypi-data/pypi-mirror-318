
import dataanalysts as da
import pandas as pd
import time
from google.colab import files

# 📥 Upload Dataset Files
print("\n🔹 Step 3: Upload Dataset Files")
uploaded = files.upload()

# Check uploaded files
for filename in uploaded.keys():
    print(f"✅ Uploaded file: {filename}")

# Load Dataset Based on File Extension
print("\n🔹 Step 4: Load Dataset")
try:
    for filename in uploaded.keys():
        if filename.endswith('.csv'):
            df = da.csv(filename)
        elif filename.endswith('.xlsx'):
            df = da.excel(filename)
        else:
            print(f"❌ Unsupported file format: {filename}")
            df = None

    if df is not None:
        print("\n📊 Dataset Preview:")
        print(df.head())
except da.DataLoadingError as e:
    print(e)

# 🧹 Data Cleaning
print("\n🔹 Step 5: Data Cleaning")
try:
    # Clean missing values
    df_cleaned = da.clean(df, strategy='mean')
    print("\n✅ Cleaned Dataset Preview:")
    print(df_cleaned.head())
    
    # Interactive Cleaning (Uncomment to test)
    # df_interactive_clean = da.interactive_clean(df)
except da.DataCleaningError as e:
    print(e)

# 🔄 Data Transformation
print("\n🔹 Step 6: Data Transformation")
try:
    # Apply Standard Scaling
    df_transformed = da.transform(df_cleaned, strategy='standard')
    print("\n✅ Transformed Dataset Preview:")
    print(df_transformed.head())
    
    # Interactive Transformation (Uncomment to test)
    # df_interactive_transform = da.interactive_transform(df_cleaned)
except da.DataTransformationError as e:
    print(e)

# 📊 Data Visualization
print("\n🔹 Step 7: Data Visualization")
try:
    # Histogram
    da.histogram(df_transformed, column=df_transformed.columns[0])
    
    # Bar Chart
    da.barchart(df_transformed, x_col=df_transformed.columns[0], y_col=df_transformed.columns[1])
    
    # Line Chart
    da.linechart(df_transformed, x_col=df_transformed.columns[0], y_col=df_transformed.columns[1])
    
    # Scatter Plot
    da.scatter(df_transformed, x_col=df_transformed.columns[0], y_col=df_transformed.columns[1])
    
    # Heatmap
    da.heatmap(df_transformed)
    
    # Interactive Plot (Uncomment to test)
    # da.interactive_plot(df_transformed)
except da.DataVisualizationError as e:
    print(e)

# 🎯 Final Message
print("\n🎯 All Steps Completed Successfully!")
