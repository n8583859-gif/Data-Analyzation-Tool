## imported modules
import pandas as pd
import os




## Dataset load
class DatasetManager:

    def __init__(self):
        self.df = None
        self.file_path = None



    def load_dataset(self, path):
        if path.lower().endswith('.csv'):
            try:
                self.df = pd.read_csv(path)
                self.file_path = path

                file_name = os.path.basename(path)
                print(f"\n☑️ Dataset {file_name} loaded successfully")
                print(f"Rows: {self.df.shape[0]}")
                print(f"Columns: {self.df.shape[1]}")

            except FileNotFoundError:
                print("❌ File not found")
        else:
            print("❌ Please provide a CSV file\n")



    def is_loaded(self):
        return self.df is not None





## App controler
class DatasetAnalyzerApp:
    def __init__(self):
        self.manager = DatasetManager()

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
                path = input("Enter CSV file path: ").strip()
                self.manager.load_dataset(path)
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

        if not self.manager.is_loaded():
            print("\n❌ Please load dataset first.")
            return


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
        if not self.manager.is_loaded():
            print("\n❌ Please load dataset first.")
            return
        
        print("⚠️ Work in under dovelopement")
        print("This option will coming soon!")

    ## Data visualization menu with choice handeling
    def data_visualization_menu(self):
        if not self.manager.is_loaded():
            print("\n❌ Please load dataset first.")
            return
        
        print("⚠️ Work in under dovelopement")
        print("This option will coming soon!")
        




## Run complete file in main module
if __name__ == "__main__":
    app = DatasetAnalyzerApp()
    app.menu_system()


