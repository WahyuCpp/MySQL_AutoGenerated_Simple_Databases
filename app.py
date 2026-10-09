import os
import time
import random
import mysql.connector
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Connect using environment variables
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor()

print("Starting data generation (10 records/sec). Press Ctrl+C to stop.")

try:
    while True:
        start_time = time.time()
        
        batch_data = []
        for _ in range(10):
            fake_name = f"User_{random.randint(1000, 9999)}"
            fake_value = round(random.uniform(1.0, 100.0), 2)
            batch_data.append((fake_name, fake_value))
            
        query = "INSERT INTO generated_data (name, value) VALUES (%s, %s)"
        cursor.executemany(query, batch_data)
        db.commit()
        
        elapsed = time.time() - start_time
        sleep_time = max(0, 1.0 - elapsed)
        time.sleep(sleep_time)

except KeyboardInterrupt:
    print("\nProgram stopped by user.")
finally:
    cursor.close()
    db.close()
