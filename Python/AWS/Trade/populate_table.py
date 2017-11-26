#! /usr/bin/python3

import os
import csv
import sqlite3

out_dir = '/root/Downloads/output'

print("Output DIR:")
out_files = [file for file in os.listdir(out_dir) if file.endswith(".csv")]
print(out_files)
print()

os.chdir(out_dir)

for dat_file_name in out_files:
        dat_file = out_dir + "/" + dat_file_name

        print("dat_file: ", dat_file)
        print()

        dat_file_hand = open(dat_file)
        dat_reader = csv.reader(dat_file_hand)

        next(dat_reader)

        db_name = 'example.db'
        conn = sqlite3.connect(db_name)

        c = conn.cursor()

        # Drop table if exists
        # c.execute('DROP TABLE IF EXISTS test10')

        ## ["SYMBOL", "INSTRUMENT", "EXPIRY_DT", "STRIKE_PR", "OPTION_TYP", "CLOSE", "OPEN_INT", "CHG_IN_OI", "TIMESTAMP"]

        # Create table
        c.execute('CREATE TABLE IF NOT EXISTS test10 (SYMBOL text, INSTRUMENT text, EXPIRY_DT test, STRIKE_PR real, OPTION_TYP text, CLOSE real, CHG_IN_OI real, OPEN_INT real, TIMESTAMP text)')

        # Populate table
        for row in dat_reader:
                c.execute('INSERT INTO test10 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', row)

        conn.commit()

        # Display table
        for row in c.execute('SELECT * FROM test10 ORDER BY EXPIRY_DT, STRIKE_PR'):
                print(row)

        # Count records
        c.execute('SELECT * FROM test10')
        records = c.fetchall()

        print("\nRecords: ", len(records))
        print()

        conn.close()
