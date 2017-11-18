import csv

path = "C:\Python\WIP"

dat_file_name = "test_data.txt"
out_file_name = "out_data.txt"

dat_file = path + "\\" + dat_file_name
out_file = path + "\\" + out_file_name

dat_file_hand = open(dat_file)
dat_reader = csv.reader(dat_file_hand)

out_file_hand = open(out_file, 'w')
out_writer = csv.writer(out_file_hand, lineterminator='\n')

data = []

data.append(["INSTRUMENT", "STR_PRICE", "OPT_TYPE", "CLOSE_PRICE", "OPEN_INT"])
out_writer.writerow(["INSTRUMENT", "STR_PRICE", "OPT_TYPE", "CLOSE_PRICE", "OPEN_INT"])

next(dat_reader)

for row in dat_reader:

	INSTRUMENT = row[0].strip()
	STR_PRICE_F = float(row[3].strip("0"))
	STR_PRICE = int(STR_PRICE_F)
	OPT_TYPE = row[4].strip()
	CLOSE_PRICE = float(row[8].lstrip("0"))
	OPEN_INT = int(row[9].lstrip("0").strip())

	data.append([INSTRUMENT, STR_PRICE, OPT_TYPE, CLOSE_PRICE, OPEN_INT])

	out_writer.writerow([INSTRUMENT, STR_PRICE, OPT_TYPE, CLOSE_PRICE, OPEN_INT])


dat_file_hand.close()
out_file_hand.close()

for dat in data:
	print(dat)




