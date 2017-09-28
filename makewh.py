import csv

def norma(aisle):
    num = int(aisle.split("w")[1])
    return "Row" + "{0:0>2}".format(num)


def normr(row):
    num = int(row[1:])
    return "R" + "{0:0>3}".format(num)


def main():
    cur_aisle = ""
    outf = open("outhouse.csv", 'wb')
    wrt = csv.writer(outf)
    inf = open("Warehouse.csv", 'rb')
    rdr = csv.reader(inf)
    for line in rdr:
        aisle, row, sect = line[1].split("-")
        aisle = norma(aisle)
        if aisle != cur_aisle:
            cur_aisle = aisle
            res = ",," + aisle + ",Madhowa Associates,1,Main Warehouse - MA"
            wrt.writerow(res.split(","))
        cur_sect = normr(row) + sect
        res = ",," + cur_aisle + "-" + cur_sect + ",Madhowa Associates,0," + cur_aisle + " - MA"
        wrt.writerow(res.split(","))
    inf.close()
    outf.close()


if __name__ == '__main__':
    main()
