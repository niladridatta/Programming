import csv
import sys
import sqlite3

path = "C:\Python\WIP"

# dat_file_name = "out_16112017.csv"

dat_file_name = sys.argv[1]
dat_file = path + "\\" + dat_file_name

dat_file_hand = open(dat_file)
dat_reader = csv.reader(dat_file_hand)

next(dat_reader)

db_name = 'example.db'
conn = sqlite3.connect(db_name)

c = conn.cursor()

# Drop table if exists
c.execute('DROP TABLE IF EXISTS test3')

# Create table
c.execute('CREATE TABLE IF NOT EXISTS test3 (SYMBOL text, EXP_DATE text, INSTRUMENT text, STR_PRICE text, OPT_TYPE text, CLOSE_PRICE real, OPEN_INT real, DATE text)')

# Populate table
for row in dat_reader:
	c.execute('INSERT INTO test3 VALUES (?,?,?,?,?,?,?,?)', row)
	
conn.commit()

# Display table
for row in c.execute('SELECT * FROM test3 ORDER BY STR_PRICE'):
	print(row)

# Count records
c.execute('SELECT * FROM test3')
records = c.fetchall()

print("\nRecords: ", len(records))

conn.close()

































