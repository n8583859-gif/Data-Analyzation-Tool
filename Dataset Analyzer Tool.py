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



    def is_loding(self):
        return self.df is not None





## App controler
class DatasetAnalyzerApp:
    def __init__(self):
        self.manager = DatasetManager()

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
                print("⚠️ Work in under dovelopement")
            elif choice == '2':
                print("⚠️ Work in under dovelopement")
            elif choice == '3':
                print("⚠️ Work in under dovelopement")
            elif choice == '4':
                print("\n\nSee you again!!")
                print("______________________________")
                break
            else:
                print("❌ Invalid choice. Try again.\n")





## Run complete file in main module
if __name__ == "__main__":
    app = DatasetAnalyzerApp()
    app.menu_system()




