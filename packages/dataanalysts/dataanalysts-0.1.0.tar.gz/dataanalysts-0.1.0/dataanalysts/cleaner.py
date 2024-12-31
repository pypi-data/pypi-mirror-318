import pandas as pd
import logging
from dataanalysts.exceptions import DataCleaningError

# Logging Configuration
logging.basicConfig(
    level=logging.INFO,
    filename='cleaner.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def clean(df, strategy='mean'):
    """
    Handle missing values in numeric and non-numeric columns.

    Parameters:
        df (pd.DataFrame): Input DataFrame.
        strategy (str): Strategy for filling missing values ('mean', 'median', 'mode').

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    try:
        numeric_columns = df.select_dtypes(include=['number']).columns
        non_numeric_columns = df.select_dtypes(exclude=['number']).columns

        if strategy == 'mean':
            df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())
        elif strategy == 'median':
            df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
        elif strategy == 'mode':
            for col in df.columns:
                df[col] = df[col].fillna(df[col].mode()[0])
        else:
            raise ValueError("Invalid strategy: Choose 'mean', 'median', or 'mode'.")

        # Handle non-numeric columns (fill with mode by default)
        for col in non_numeric_columns:
            if df[col].isnull().any():
                df[col] = df[col].fillna(df[col].mode()[0])

        logging.info("✅ Missing values handled successfully using strategy: %s", strategy)
        print(f"✅ Missing values handled using strategy: {strategy}")
        return df

    except Exception as e:
        logging.error(f"❌ Data Cleaning Error: {str(e)}")
        raise DataCleaningError(f"❌ Data Cleaning Error: {str(e)}")


def interactive_clean(df):
    """
    Interactive Data Cleaning with user inputs.

    Parameters:
        df (pd.DataFrame): Input DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    try:
        print("\n🔄 Interactive Data Cleaning")
        print("1. Handle Missing Values (mean/median/mode)")
        print("2. Remove Duplicates")
        print("3. Drop Columns")
        print("4. Fill Missing with Custom Value")
        print("5. Exit")

        option = input("Choose an option (1-5): ").strip()

        if option == '1':
            strategy = input("Enter strategy (mean/median/mode): ").strip()
            df = clean(df, strategy)
        elif option == '2':
            df.drop_duplicates(inplace=True)
            print("✅ Duplicates removed.")
        elif option == '3':
            cols = input("Enter columns to drop (comma-separated): ").split(',')
            df.drop(columns=cols, inplace=True, errors='ignore')
            print("✅ Columns dropped successfully.")
        elif option == '4':
            column = input("Enter column name: ").strip()
            value = input("Enter value to fill: ").strip()
            df[column] = df[column].fillna(value)
            print(f"✅ Column '{column}' filled with value: {value}.")
        elif option == '5':
            print("✅ Exiting Interactive Cleaning.")
        else:
            print("❌ Invalid option. Please try again.")
            interactive_clean(df)

        return df

    except Exception as e:
        logging.error(f"❌ Interactive Cleaning Error: {str(e)}")
        raise DataCleaningError(f"❌ Interactive Cleaning Error: {str(e)}")
