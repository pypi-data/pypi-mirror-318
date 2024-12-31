import pandas as pd
import logging
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
from dataanalysts.exceptions import DataTransformationError

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    filename='transformer.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def transform(df, strategy='standard'):
    """
    Apply scaling to numeric columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        strategy (str): Scaling strategy ('standard', 'minmax', 'robust').

    Returns:
        pd.DataFrame: Scaled DataFrame.
    """
    try:
        numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

        if numeric_columns.empty:
            raise DataTransformationError("No numeric columns found for scaling.")

        if strategy == 'standard':
            scaler = StandardScaler()
        elif strategy == 'minmax':
            scaler = MinMaxScaler()
        elif strategy == 'robust':
            scaler = RobustScaler()
        else:
            raise ValueError("Invalid strategy: Choose 'standard', 'minmax', or 'robust'")

        df[numeric_columns] = scaler.fit_transform(df[numeric_columns])
        logging.info(f"✅ {strategy.capitalize()} Scaling applied successfully on numeric columns.")
        print(f"✅ {strategy.capitalize()} Scaling applied successfully on numeric columns.")
        return df

    except Exception as e:
        logging.error(f"❌ Scaling Error: {str(e)}")
        raise DataTransformationError(f"❌ Scaling Error: {str(e)}")


def interactive_transform(df):
    """
    Interactive Transformation Tool for Numeric Columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Transformed DataFrame.
    """
    try:
        print("\n🔄 Interactive Data Transformation")
        print("Select an option:")
        print("1. Standard Scaling")
        print("2. Min-Max Scaling")
        print("3. Robust Scaling")
        print("4. Exit Transformation")

        option = input("Enter your choice (1-4): ").strip()

        if option == '1':
            return transform(df, strategy='standard')
        elif option == '2':
            return transform(df, strategy='minmax')
        elif option == '3':
            return transform(df, strategy='robust')
        elif option == '4':
            print("✅ Exiting Transformation. No changes made.")
            return df
        else:
            print("❌ Invalid option. Please try again.")
            return interactive_transform(df)

    except Exception as e:
        logging.error(f"❌ Interactive Transformation Error: {str(e)}")
        raise DataTransformationError(f"❌ Interactive Transformation Error: {str(e)}")
