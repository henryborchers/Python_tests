import csv
from enum import Enum

__author__ = 'Henry'
import matplotlib.pyplot as plt
from collections import namedtuple
Data = namedtuple("Data", ['years', 'glob', 'NHem', 'SHem'])


def plot(data: Data):
    fig=plt.figure()
    rect = fig.patch
    rect.set_facecolor('white')
    # plt.subplot(211)
    plt.xlabel("Years")
    plt.ylabel("Degrees Celsius")
    plt.plot(data.years, data.glob, label="Global Means")
    plt.plot(data.years, data.NHem, label="Northern Hemisphere")
    plt.plot(data.years, data.SHem, label="Southern Hemisphere")
    plt.legend(loc='upper left')
    # plt.legend(bbox_to_anchor=(.5,1))
    plt.title("Global and Hemispheric Monthly Means and Zonal Annual Means.")
    plt.show()


def parse_data() -> Data:
    years = []
    glob = []
    NHem = []
    SHem = []

    with open("ExcelFormattedGISTEMPData2CSV.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        # Data = namedtuple("Data", next(reader))
        next(reader)
        for row in reader:
            # print(row)
            years.append(row[0])
            glob.append(row[1])
            NHem.append(row[2])
            SHem.append(row[3])
    data = Data(years=years, glob=glob, NHem=NHem, SHem=SHem)

    return data


def main():
    print("Hello")
    data = parse_data()

    plot(data)

if __name__ == '__main__':
    main()
