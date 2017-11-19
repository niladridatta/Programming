#! /usr/bin/python3

import csv
import sys
import sqlite3

path = "/root/Python"

dat_file_name = sys.argv[1]
dat_file = path + "/" + dat_file_name

dat_file_hand = open(dat_file)
dat_reader = csv.reader(dat_file_hand)

next(dat_reader)

db_name = 'example.db'
conn = sqlite3.connect(db_name)

c = conn.cursor()

# Drop table if exists
c.execute('DROP TABLE IF EXISTS test4')

## ["SYMBOL", "INSTRUMENT", "EXPIRY_DT", "STRIKE_PR", "OPTION_TYP", "CLOSE", "OPEN_INT", "CHG_IN_OI", "TIMESTAMP"]

# Create table
c.execute('CREATE TABLE IF NOT EXISTS test4 (SYMBOL text, INSTRUMENT text, EXPIRY_DT test, STRIKE_PR real, OPTION_TYP text, CLOSE real, CHG_IN_OI real, OPEN_INT real, TIMESTAMP text)')

# Populate table
for row in dat_reader:
    c.execute('INSERT INTO test4 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', row)

conn.commit()

# Display table
for row in c.execute('SELECT * FROM test4 ORDER BY EXPIRY_DT, STRIKE_PR'):
    print(row)

# Count records
c.execute('SELECT * FROM test4')
records = c.fetchall()

print("\nRecords: ", len(records))
print()

conn.close()


































