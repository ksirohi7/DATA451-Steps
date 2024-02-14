import os
import csv
from datetime import datetime, timedelta
from tqdm import tqdm
import sys

def act24_conversion(file_path, output_dir):
    path = file_path

    # reading in file and getting top four lines (aka up to date/time)
    with open(path, 'r') as file:
        header = []
        for i in range(4):
            header.append(next(file))

        # extracting the start time and date
        time_line = [line for line in header if 'Start Time' in line][0]
        time = time_line.split(',')[0].split()[-1]

        date_line = [line for line in header if 'Start Date' in line][0]
        date = date_line.split(',')[0].split()[-1]

        # saving date time to preferred format (YYYY-MM-DD HH:MM:SS.FFFF)
        dateTime = datetime.strptime(date + ' ' + time, '%m/%d/%Y %H:%M:%S')

        # skipping over next 7 lines to reach the actual data
        for i in range(7):
            next(file)

        # creating output file
        file_name = os.path.basename(file_path).split()[0]
        out_file = os.path.join(output_dir, f"{file_name}_output.csv")

        with open(out_file, 'w', newline='') as out:
            writer = csv.writer(out)
            writer.writerow(["time", 'x', 'y', 'z'])

            # going through each line and changing seconds and appending values
            line_no = 0
            for line in tqdm(file):
                values = line.strip().split(',')
                seconds = dateTime + timedelta(seconds=line_no * 0.0125)
                row = [seconds.strftime('%Y-%m-%d %H:%M:%S.%f'), values[0], values[1], values[2]]
                writer.writerow(row)
                line_no += 1


if __name__ == "__main__":
    act24_conversion(sys.argv[1], sys.argv[2])
    # when running, do: python3 act24_conversion.py "data/datasets/ACT24/{file}.csv" "/data/kasirohi"
