## imported modules
import pandas as pd
import os
import numpy as np




# Dataset load
class DatasetManager:

    def __init__(self):
        self.df = None
        self.file_path = None



    def load_dataset(self):
        while True:
            path = input("Enter CSV file path (or `q` to quit): ").strip()
            if path.lower().endswith('.csv'):
                try:
                    self.df = pd.read_csv(path).copy()
                    self.file_path = path

                    file_name = os.path.basename(path)
                    print(f"\n☑️ Dataset {file_name} loaded successfully")
                    print(f"Rows: {self.df.shape[0]}")
                    print(f"Columns: {self.df.shape[1]}")
                    return

                except FileNotFoundError:
                    print("❌ File not found")
            elif path.lower() == 'q':
                return
            else:
                print("❌ Please provide a CSV file\n")




    def is_loaded(self):
        return self.df is not None







# Data Cleaner
class DataCleaner:

    def __init__(self, manager):
        self.manager = manager
        
    ## Missing value report
    def missing_value_report(self):
        df = self.manager.df
        print("------[Missing Value Report]-----")
        print(df.isnull().sum())
        print("--------------[In %]-------------")
        print(round((df.isnull().sum() / len(df))*100, 1))

    ## Fill missing values
    def fill_missing_values(self):
        df = self.manager.df

        while True:
            col_name = input("Enter column name ('q' to quit): ").strip()
            if col_name in df.columns:

                ### Data exploration of a specific column
                print("\n--------------[Data Analysis of Column]------------")
                print(f"Column: {col_name}")
                # print(f"\nRows: {df.shape()[0]}")
                print(f"\n[Data Type]... {df[col_name].dtype}")
                print(f"\n[Missing values]... {df[col_name].isnull().sum()}")
                print(f"\n[Missing Value in %]... {round((df[col_name].isnull().sum() / len(df[col_name]))*100, 1)}")
                print(f"\n[First 5 rows]...\n{df[col_name].head()}")
                print(f"\n[Last 5 rows]...\n{df[col_name].tail()}")
                print("---------------------------------------------------\n")

                while True:
                    print("\n==============================")
                    print("1. Mean")
                    print("2. Median")
                    print("3. Mode")
                    print("4. Custom Value")
                    print("5. Forward filling")
                    print("6. Backward Filling")
                    print("7. Linear Filling (Interpolation)")
                    print("8. Back")
                    print("==============================")

                    choice = input("Choose method: ").strip()
                    missing_before = df[col_name].isnull().sum()

                    if choice == '1':
                        if pd.api.types.is_numeric_dtype(df[col_name]):
                            df[col_name] = df[col_name].fillna(round(np.mean(df[col_name]),2))
                            print(f"\n☑️ Filled {missing_before} missing values using Mean\n")
                        else:
                            print("❌ This method is only available for numeric columns.")

                    elif choice == '2':
                        if pd.api.types.is_numeric_dtype(df[col_name]):
                            df[col_name] = df[col_name].fillna(np.median(df[col_name]))
                            print(f"\n☑️ Filled {df[missing_before].isnull().sum()} missing values using Median\n")
                        else:
                            print("❌ This method is only available for numeric columns.")

                    elif choice == '3':
                        df[col_name] = df[col_name].fillna(df[col_name].mode()[0])
                        print(f"\n☑️ Filled {missing_before} missing values using Mode\n")
                        
                    elif choice == '4':
                        custom_value = input("Enter custom value: ").strip()
                        df[col_name] = df[col_name].fillna(custom_value)
                        print(f"\n☑️ Filled {missing_before} missing values using Custom Value\n")
                    
                    elif choice == '5':
                        df[col_name] = df[col_name].ffill()
                        print(f"\n☑️ Filled {missing_before} missing values using Forward filling\n")

                    elif choice == '6':
                        df[col_name] = df[col_name].bfill()
                        print(f"\n☑️ Filled {missing_before} missing values using Backward Filling\n")

                    elif choice == '7':
                        if pd.api.types.is_numeric_dtype(df[col_name]):
                            df[col_name] = df[col_name].interpolate(method='linear')
                            print(f"\n☑️ Filled {missing_before} missing values using Linear Filling (interpolation)\n")
                        else:
                            print("❌ This method is only available for numeric columns.")

                    elif choice == '8':
                        return
                    
                    else:
                        print("❌ Invalid choice. Try again.\n")
                        
            elif col_name.lower() == 'q':
                return
            
            else:
                print("\n❌ Column not found. Try again..")
                print("Note-> column name should same as original column name case(upper/lower).\n")



    ## drop missing rows
    def drop_missing_rows(self):
        df = self.manager.df
        before_rows = df.shape[0]
        after_rows = df.dropna().shape[0]
        removed_rows = before_rows - after_rows
        removed_rows_percentage = round((removed_rows/before_rows)*100, 2) if before_rows else 0

        print("\n---------[Quick View of Missing Rows]-------")
        print(f"Rows Before: {before_rows}")
        print(f"Rows To Remove: {removed_rows}")
        print(f"% of Rows For Remove: {removed_rows_percentage}")
        print(f"Rows After: {after_rows}")
        
        print("----------------------------------------------")

        while True:
            choice = input("⚠️ Are you sure! you wanna proceed (y/n): ").strip()
            if choice.lower() == 'y':
                df.dropna(inplace=True)
                print(f"\n☑️ {removed_rows} rows removed/dropped successfully.\n")
                return 
            elif choice.lower() == 'n':
                return
            else:
                print("❌ Invalid choice. Try again.\n")




    ## drop missing columns
    def drop_missing_columns(self):
        df = self.manager.df
        missing_value_col = df.isnull().sum()
        null_columns = df.columns[df.isnull().any()].tolist()

        print("\n---------[Missing Value Report]-------")
        print(f"Columns with missing values: \n{missing_value_col}")
        print("---------------------------------------")

        while True:
            print("\n==============================")
            print("1. Choose Specific column")
            print("2. Drop all columns with missing values")
            print("3. Back")
            print("==============================")

            choice = input("Enter your choice: ").strip()
            
            ### remove specific column
            if choice == '1':
                while True:
                    col_name = input("Enter column name ('q' to quit): ").strip()
                    if col_name in df.columns:
                        #### give caution of removing non null column.
                        if col_name not in null_columns:
                            print(f"⚠️  Column [{col_name}] has 0 missing values.")

                        while True:
                            confirm = input("⚠️  Are you sure! you wanna proceed (y/n): ").strip()
                            if confirm.lower() == 'y':
                                df.drop(columns=col_name, inplace=True)
                                print(f"\n☑️ Column [{col_name}] removed successfully.\n")
                                return
                            elif confirm.lower() == 'n':
                                return
                            else:
                                print("❌ Invalid choice. Try again.\n")

                    elif col_name.lower() == 'q':
                        return
                    else:
                        print("❌ Invalid choice. Try again.\n") 
                        
            ### remove all columns with NA values
            elif choice == '2':
                while True:
                    confirm = input("⚠️ Are you sure! you wanna proceed (y/n): ").strip()
                    if confirm.lower() == 'y':
                        df.dropna(axis=1, inplace=True)
                        print(f"\n☑️ Columns {null_columns} removed successfully.\n")
                        return 
                    elif confirm.lower() == 'n':
                        return
                    else:
                        print("❌ Invalid choice. Try again.\n")


            elif choice == '3':
                return
            
            else:
                print("❌ Invalid choice. Try again.\n")





    ## remove duplicate rows
    def remove_duplicate_rows(self):
        df = self.manager.df
        duplicate_rows = df.duplicated().sum()

        print("\n--------[Quick View of Duplicate Rows]-------")
        print(f"Duplicate Found: {duplicate_rows}")
        print("---------------------------------------------")

        while True:
            choice = input("⚠️ Are you sure! you wanna proceed (y/n): ").strip()
            if choice.lower() == 'y':
                df.drop_duplicates(inplace=True)
                print(f"\n☑️ {duplicate_rows} duplicate rows removed/dropped successfully.\n")
                return 
            elif choice.lower() == 'n':
                return
            else:
                print("❌ Invalid choice. Try again.\n")





    def save_cleaned_dataset(self):
        df = self.manager.df
        file_name = input("Enter file-name to saved as: ").strip()

        if not file_name.endswith('.csv'):
            file_name += '.csv'
        
        df.to_csv(file_name, index=False)
        print(f"\n☑️  Dataset saved as {file_name}.csv\n")










# App controler
class DatasetAnalyzerApp:
    def __init__(self):
        self.manager = DatasetManager()
        self.cleaner = DataCleaner(self.manager)



    ## Main menu with choice handelling
    def menu_system(self):
        while True:
            print("\n==============================")
            print("   DATASET ANALYZER TOOL")
            print("==============================")
            print("0. Load Dataset")
            print("1. Data Exploration")
            print("2. Data Cleaning")
            print("3. Data Visualization")
            print("4. Exit")
            print("==============================")

            choice = input("Enter your choice: ").strip()

            if choice == '0':
                self.manager.load_dataset()
            elif choice == '1':
                self.data_exploration_menu()
            elif choice == '2':
                self.data_cleaning_menu()
            elif choice == '3':
                self.data_visualization_menu()
            elif choice == '4':
                print("\n\nSee you again!!")
                print("______________________________")
                break
            else:
                print("❌ Invalid choice. Try again.\n")





    ## Data Exploration Menu with choice handelling
    def data_exploration_menu(self):

        ### checking of data loading
        if not self.manager.is_loaded():
            print("\n❌ Please load dataset first.")
            return

        ### menu controler
        while True:
            print("\n==============================")
            print("   DATA EXPLORATION MENU ")
            print("==============================")
            print("1. Dataset Shape")
            print("2. Column Names")
            print("3. Data Types")
            print("4. Dataset Info")
            print("5. First 5 Rows")
            print("6. Last 5 Rows")
            print("7. Statistical Summary")
            print("8. Missing Value Report")
            print("9. Unique Values in Column")
            print("10. Back")
            print("==============================")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                print("--------------[Shape]-------------")
                print(f"\nRows: {self.manager.df.shape[0]}")
                print(f"Columns: {self.manager.df.shape[1]}\n")
            
            elif choice == '2':
                print("-----------[Column Names]---------")
                for col in self.manager.df.columns:
                    print(col)

            elif choice == '3':
                print("-----------[Data Types]----------")
                print(self.manager.df.dtypes)

            elif choice == '4':
                print("-----------[Dataset Info]---------")
                self.manager.df.info()

            elif choice == '5': 
                print("---------[First 5 Rows]-----------")
                print(self.manager.df.head())
            
            elif choice == '6':
                print("---------[Last 5 Rows]-----------")
                print(self.manager.df.tail())
            
            elif choice == '7':
                print("--------[Statical Summary]-------")
                print(self.manager.df.describe())

            elif choice == '8':
                print("------[Missing Value Report]-----")
                print(self.manager.df.isnull().sum())
                print("--------------[In %]-------------")
                print(round((self.manager.df.isnull().sum() / len(self.manager.df))*100, 1))

            elif choice == '9':
                col_name = input("Enter column name: ").strip()
                if col_name in self.manager.df.columns:
                    print(f"----[Unique Values in {col_name.title()}]----")
                    for val in self.manager.df[col_name].unique():
                        print(f"- {val}")

                else:
                    print("\n❌ Column not found. Try again..")
                    print("Note-> column name should same as original column name case(upper/lower).\n")


            elif choice == '10':
                print(".....Back to Main Menu.....\n")
                return
            
            else:
                print("❌ Invalid choice. Try again.\n")
            
            print("----------------------------------")
        




    ## Data cleaning menu with choice handeling
    def data_cleaning_menu(self):

        ### checking of data loading
        if not self.manager.is_loaded():
            print("\n❌ Please load dataset first.")
            return
        
        ### menu controler
        while True:
            print("\n==============================")
            print("DATA CLEANING MENU")
            print("==============================")
            print("1. Missing Value Report")
            print("2. Fill Missing Values")
            print("3. Drop Missing Rows")
            print("4. Drop Missing Columns")
            print("5. Remove Duplicate Rows")
            print("6. Save Cleaned Dataset")
            print("7. Back")
            print("==============================")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                self.cleaner.missing_value_report()
            elif choice == '2':
                self.cleaner.fill_missing_values()
            elif choice == '3':
                self.cleaner.drop_missing_rows()
            elif choice == '4':
                self.cleaner.drop_missing_columns()
            elif choice == '5':
                self.cleaner.remove_duplicate_rows()
            elif choice == '6':
                self.cleaner.save_cleaned_dataset()
            elif choice == '7':
                return
            else:
                print("❌ Invalid choice. Try again.\n")
            
            print("----------------------------------")





    ## Data visualization menu
    def data_visualization_menu(self):

        ### checking of data loading
        if not self.manager.is_loaded():
            print("\n❌ Please load dataset first.")
            return
        
        print("⚠️ Work in under dovelopement")
        print("This option will coming soon!")
        







## Run complete file in main module
if __name__ == "__main__":
    app = DatasetAnalyzerApp()
    app.menu_system()


