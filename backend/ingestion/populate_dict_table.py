import csv
import json
import psycopg2

# get database credentials
with open('../backend/secrets.json') as f:
  secrets = json.load(f)
  local_db = secrets['local_database']

# connect to database with processed credentials
conn = psycopg2.connect(local_db['DATABASE_URL'])

# get cursor for db operations
cur = conn.cursor()

# process dictionary csv file
with open('./dictionary.csv', newline='') as csvfile:
  dict_data = csv.reader(csvfile)
  for row in dict_data:
    print(row)
    cur.execute("""
      INSERT INTO dictionary VALUES (%s, %s, %s);
      """,
      (row[0], row[1], row[2])
    )

  conn.commit()

# close communication with database
cur.close()
conn.close()
