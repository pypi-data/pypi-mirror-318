import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import logging
from dataanalysts.exceptions import DataVisualizationError

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    filename='visualizer.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ✅ 1. Histogram
def histogram(df, column):
    """
    Plot a histogram for a specified column.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        column (str): Column name for plotting.
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], bins=30, kde=True, color='skyblue')
        plt.title(f'🔍 Histogram of {column}', fontsize=14)
        plt.xlabel(column, fontsize=12)
        plt.ylabel('Frequency', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()
        logging.info(f"✅ Histogram plotted for column: {column}")
    except Exception as e:
        logging.error(f"❌ Histogram Error: {str(e)}")
        raise DataVisualizationError(f"❌ Histogram Error: {str(e)}")


# ✅ 2. Bar Chart
def barchart(df, x_col, y_col):
    """
    Plot a bar chart for two specified columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        x_col (str): Column for x-axis.
        y_col (str): Column for y-axis.
    """
    try:
        plt.figure(figsize=(12, 7))
        sns.barplot(x=x_col, y=y_col, data=df, palette='viridis')
        plt.title(f'📊 Bar Chart: {x_col} vs {y_col}', fontsize=14)
        plt.xlabel(x_col, fontsize=12)
        plt.ylabel(y_col, fontsize=12)
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.show()
        logging.info(f"✅ Bar Chart plotted for columns: {x_col} vs {y_col}")
    except Exception as e:
        logging.error(f"❌ Bar Chart Error: {str(e)}")
        raise DataVisualizationError(f"❌ Bar Chart Error: {str(e)}")


# ✅ 3. Line Plot
def linechart(df, x_col, y_col):
    """
    Plot a line chart for two specified columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        x_col (str): Column for x-axis.
        y_col (str): Column for y-axis.
    """
    try:
        plt.figure(figsize=(12, 7))
        sns.lineplot(x=x_col, y=y_col, data=df, marker='o', color='blue')
        plt.title(f'📈 Line Plot: {x_col} vs {y_col}', fontsize=14)
        plt.xlabel(x_col, fontsize=12)
        plt.ylabel(y_col, fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.show()
        logging.info(f"✅ Line Plot plotted for columns: {x_col} vs {y_col}")
    except Exception as e:
        logging.error(f"❌ Line Plot Error: {str(e)}")
        raise DataVisualizationError(f"❌ Line Plot Error: {str(e)}")


# ✅ 4. Scatter Plot
def scatter(df, x_col, y_col):
    """
    Plot a scatter plot for two specified columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        x_col (str): Column for x-axis.
        y_col (str): Column for y-axis.
    """
    try:
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=x_col, y=y_col, data=df, color='green')
        plt.title(f'🔵 Scatter Plot: {x_col} vs {y_col}', fontsize=14)
        plt.xlabel(x_col, fontsize=12)
        plt.ylabel(y_col, fontsize=12)
        plt.show()
        logging.info(f"✅ Scatter Plot plotted for columns: {x_col} vs {y_col}")
    except Exception as e:
        logging.error(f"❌ Scatter Plot Error: {str(e)}")
        raise DataVisualizationError(f"❌ Scatter Plot Error: {str(e)}")


# ✅ 5. Heatmap
def heatmap(df):
    """
    Plot a heatmap showing the correlation between numeric columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
    """
    try:
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('🌡️ Heatmap of Correlation Matrix', fontsize=14)
        plt.show()
        logging.info("✅ Heatmap plotted successfully.")
    except Exception as e:
        logging.error(f"❌ Heatmap Error: {str(e)}")
        raise DataVisualizationError(f"❌ Heatmap Error: {str(e)}")


# ✅ 6. Interactive Visualization
def interactive_plot(df):
    """
    Interactive function for selecting visualization types.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
    """
    try:
        print("\n🔄 Interactive Data Visualization")
        print("1. Histogram")
        print("2. Bar Chart")
        print("3. Line Plot")
        print("4. Scatter Plot")
        print("5. Heatmap")
        print("6. Exit Visualization")

        option = input("Enter your choice (1-6): ").strip()

        if option == '1':
            column = input("Enter column for Histogram: ").strip()
            histogram(df, column)
        elif option == '2':
            x_col = input("Enter X-axis column: ").strip()
            y_col = input("Enter Y-axis column: ").strip()
            barchart(df, x_col, y_col)
        elif option == '3':
            x_col = input("Enter X-axis column: ").strip()
            y_col = input("Enter Y-axis column: ").strip()
            linechart(df, x_col, y_col)
        elif option == '4':
            x_col = input("Enter X-axis column: ").strip()
            y_col = input("Enter Y-axis column: ").strip()
            scatter(df, x_col, y_col)
        elif option == '5':
            heatmap(df)
        elif option == '6':
            print("✅ Exiting Visualization. No graph displayed.")
        else:
            print("❌ Invalid option. Please try again.")
            interactive_plot(df)

    except Exception as e:
        logging.error(f"❌ Interactive Visualization Error: {str(e)}")
        raise DataVisualizationError(f"❌ Interactive Visualization Error: {str(e)}")
