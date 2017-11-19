#! /usr/bin/python3

import csv
import sys

path = "/root/Python"

dat_file_name = sys.argv[1]

date = dat_file_name[2:11]
out_file_name = "out_" + date + ".csv"

dat_file = path + "/" + dat_file_name
out_file = path + "/" + out_file_name

dat_file_hand = open(dat_file)
dat_reader = csv.reader(dat_file_hand)

out_file_hand = open(out_file, 'w')
out_writer = csv.writer(out_file_hand, lineterminator='\n')

data = []

next(dat_reader)

data.append(["SYMBOL", "INSTRUMENT", "EXPIRY_DT", "STRIKE_PR", "OPTION_TYP", "CLOSE", "OPEN_INT", "CHG_IN_OI", "TIMESTAMP"])
out_writer.writerow(["SYMBOL", "INSTRUMENT", "EXPIRY_DT", "STRIKE_PR", "OPTION_TYP", "CLOSE", "OPEN_INT", "CHG_IN_OI", "TIMESTAMP"])

cur_str = 10200
low_str = cur_str - 700
upr_str = cur_str + 700

cur_exp = '30-Nov-2017'
nxt_exp = '28-Dec-2017'

for row in dat_reader:

    if ( row[1].strip() == 'NIFTY' and ( int(row[3]) % 100 == 0 ) and row[2] == cur_exp) or ( row[1].strip() == 'NIFTY' and ( int(row[3]) % 100 == 0 ) and row[2] == nxt_exp):

        SYMBOL = row[1]
        EXPIRY_DT = row[2]
        INSTRUMENT = row[0]
        STRIKE_PR = int(float(row[3]))
        OPTION_TYP = row[4]
        CLOSE = float(row[8])
        OPEN_INT = int(row[12])
        CHG_IN_OI = int(row[13])
        TIMESTAMP = row[14]

        if STRIKE_PR >= low_str and STRIKE_PR <= upr_str:

                data.append([SYMBOL, INSTRUMENT, EXPIRY_DT, STRIKE_PR, OPTION_TYP, CLOSE, OPEN_INT, CHG_IN_OI, TIMESTAMP])
                out_writer.writerow([SYMBOL, INSTRUMENT, EXPIRY_DT, STRIKE_PR, OPTION_TYP, CLOSE, OPEN_INT, CHG_IN_OI, TIMESTAMP])

dat_file_hand.close()
out_file_hand.close()

for dat in data:
        print(dat)

print("\nRecords: ", len(data) - 1)
print()

