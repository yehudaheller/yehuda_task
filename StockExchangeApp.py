# run_program.py
import subprocess
import os

def run_init_db():
    print("Initializing database...")
    subprocess.run(["python", "DataLayer/Read_sql_to_db.py"])
    print("Database initialization complete.")

def run_ui_layer():
    print("Running UI layer...")
    subprocess.run(["python", "UILayer/ui_layer.py"])
    print("UI layer execution complete.")

if __name__ == "__main__":
    run_init_db()
    run_ui_layer()
