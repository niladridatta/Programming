import csv
import sqlite3

path = "C:\Python\WIP"

dat_file_name = "out_data.txt"
dat_file = path + "\\" + dat_file_name

dat_file_hand = open(dat_file)
dat_reader = csv.reader(dat_file_hand)

next(dat_reader)

db_name = 'example.db'
conn = sqlite3.connect(db_name)

c = conn.cursor()

# Drop table if exists
c.execute('DROP TABLE IF EXISTS test2')

# Create table
c.execute('CREATE TABLE IF NOT EXISTS test2 (INSTRUMENT text, STR_PRICE text, OPT_TYPE text, CLOSE_PRICE real, OPEN_INT real)')

# Populate table
for row in dat_reader:
	c.execute('INSERT INTO test2 VALUES (?,?,?,?,?)', row)
	
conn.commit()

# Display table
for row in c.execute('SELECT * FROM test2 ORDER BY STR_PRICE'):
	print(row)

conn.close()

































