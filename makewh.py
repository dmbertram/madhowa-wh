import csv


def main():
    cur_aisle = ""
    cur_row = ""
    outf = open("outhouse.csv", 'wb')
    wrt = csv.writer(outf)
    inf = open("Warehouse.csv", 'rb')
    rdr = csv.reader(inf)
    for line in rdr:
        aisle, row, sect = line[1].split("-")
        if aisle != cur_aisle:
            cur_aisle = aisle
            res = aisle + " - MA," + aisle + ",Madhowa Associates,1,All Warehouses - MA"
            wrt.writerow(res.split(","))
        if row != cur_row:
            cur_row = row
            res = row + " - MA," + row + ",Madhowa Associates,1," + cur_aisle + " - MA"
            wrt.writerow(res.split(","))
        res = sect + " - MA," + sect + ",Madhowa Associates,0," + cur_row + " - MA"
        wrt.writerow(res.split(","))
    inf.close()
    outf.close()


if __name__ == '__main__':
    main()
