# import csv
#
# with open('data.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

import pandas as pd
import os


def read_csv(file):
    df = pd.read_csv(file)
    var = df['no']
    for i in var:
        print(i)


def list_dir(my_dir):
    for file in os.listdir(my_dir):
        if file.endswith(".csv"):
            # print(os.path.join("/media/mrrobot/ACADEMIC/pycharm Projects/csv reader", file))
            print(file)
            read_csv(file)


if __name__ == "__main__":
    my_dir = "/media/mrrobot/ACADEMIC/pycharm Projects/csv reader"
    list_dir(my_dir)