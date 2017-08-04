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
        print "aisle = %s, row = %s, sect = %s \n" % (aisle, row, sect)
        if aisle != cur_aisle:
            cur_aisle = aisle
            print ">>>>>>  create new parent warehouose = " + cur_aisle
    inf.close()
    outf.close()


if __name__ == '__main__':
    main()
