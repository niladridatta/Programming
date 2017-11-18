import csv
import sys

path = "C:\Python\WIP"

# dat_file_name = "ts16112017.csv"

dat_file_name = sys.argv[1]

date = dat_file_name[2:10]
out_file_name = "out_" + date + ".csv"

dat_file = path + "\\" + dat_file_name
out_file = path + "\\" + out_file_name

dat_file_hand = open(dat_file)
dat_reader = csv.reader(dat_file_hand)

out_file_hand = open(out_file, 'w')
out_writer = csv.writer(out_file_hand, lineterminator='\n')

data = []

data.append(["SYMBOL", "EXP_DATE", "INSTRUMENT", "STR_PRICE", "OPT_TYPE", "CLOSE_PRICE", "OPEN_INT", "DATE"])
out_writer.writerow(["SYMBOL", "EXP_DATE", "INSTRUMENT", "STR_PRICE", "OPT_TYPE", "CLOSE_PRICE", "OPEN_INT", "DATE"])

next(dat_reader)

cur_str = 10200
low_str = cur_str - 700
upr_str = cur_str + 700

cur_exp = '30/11/2017'
nxt_exp = '28/12/2017'

for row in dat_reader:

	if row[1].strip() == 'NIFTY' and row[2] == cur_exp or row[2] == nxt_exp:
	
		SYMBOL = row[1].strip()
		EXP_DATE = row[2].strip()
		INSTRUMENT = row[0].strip()
		STR_PRICE = int(float(row[3].lstrip("0")))
		OPT_TYPE = row[4].strip()
		CLOSE_PRICE = float(row[8].lstrip("0"))
		OPEN_INT = int(row[9].lstrip("0").strip())
		DATE = date
		
		if STR_PRICE >= low_str and STR_PRICE <= upr_str:
		
			data.append([SYMBOL, EXP_DATE, INSTRUMENT, STR_PRICE, OPT_TYPE, CLOSE_PRICE, OPEN_INT, DATE])
			out_writer.writerow([SYMBOL, EXP_DATE, INSTRUMENT, STR_PRICE, OPT_TYPE, CLOSE_PRICE, OPEN_INT, DATE])
		
	else:
		break

dat_file_hand.close()
out_file_hand.close()

for dat in data:
	print(dat)
	
print("\nRecords: ", len(data) - 1)




























