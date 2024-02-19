import datetime
import sys

def map_time_military(time):
    is_am = time[-2:] == "AM"
    time_split = time[:-3].split(":")
    if is_am:
        if time_split[0] == "12":
            return f"0:{time_split[1]}:{time_split[2]}"
    else:
        if time_split[0] != "12":
            new_hour = int(time_split[0])+12
            return f"{new_hour}:{time_split[1]}:{time_split[2]}"
    return time[:-3]

def get_session_bounds(tokens):
    m = int(tokens[2])
    d = int(tokens[3])
    y = int(tokens[4])
    date = str(datetime.date(year=y, month=m, day=d))

    # get military time from am/pm time
    st = tokens[5]
    et = tokens[6]
    mst = map_time_military(st)
    met = map_time_military(et)

    # get date time as string
    sdt_str = f'{date} {mst}'
    edt_str = f'{date} {met}'

    sdt = datetime.datetime.strptime(sdt_str, '%Y-%m-%d %H:%M:%S')
    edt = datetime.datetime.strptime(edt_str, '%Y-%m-%d %H:%M:%S')

    # return sdt, edt
    return sdt, edt


    # do_log --> file path to do_log_final.csv
    # output_dir_path --> path to directory to produce output
    # act24_file --> file path to processed act24 data (kirina dir)
    # id --> id of file being processed (102,103,...,etc)
def get_sessions(do_log_file, output_dir_path, act24_file, id):

    # Get time bounds for 2 sessions from do log
    do_log = open(do_log_file, 'r') # open do log
    do_log.readline()  # read header
    dict = {}
    for line in do_log:
        tokens = line.split(',')
        if tokens[0] == id: # get session info for given id
            # (key, value) --> (session_num, session_data)
            dict[tokens[1]] = tokens # store session info in dictionary

    # for each session get the session bounds using get_session_bounds function
    sess_1 = get_session_bounds(dict["1"])
    lb1, ub1 = sess_1

    sess_2 = get_session_bounds(dict["2"])
    lb2, ub2 = sess_2

    do_log.close()

    # read
    act24_fin = open(act24_file, 'r')
    act24_fin.readline() # read header

    # create outputs for 2 sessions
    fout1 = open(f"{output_dir_path}/ACT24_{id}_1.csv", "w")
    fout2 = open(f"{output_dir_path}/ACT24_{id}_2.csv", "w")

    # write headers to files
    fout1.write('time,x,y,z\n')
    fout2.write('time,x,y,z\n')

    # Output data within each session period
    for line in act24_fin:
        obs_tokens = line.split(',')
        # read in obs datetime
        obs_dt = datetime.datetime.strptime(obs_tokens[0], '%Y-%m-%d %H:%M:%S.%f')

        # if obs datetime is within session 1 --> output to session 1 file
        if (lb1 <= obs_dt <= ub1):
            fout1.write(line)

        # if obs datetime is within session 2 --> output to session 2 file
        if (lb2 <= obs_dt <= ub2):
            fout2.write(line)

    fout1.close()
    fout2.close()








# file path to do log, directory containing cleaned act 24 data, output directory
# naming conventions ACT24_102_output.csv ACT24_117_output.csv ACT24_134_output.csv ACT24_103_output.csv
# time,x,y,z


if __name__ == '__main__':

    args = sys.argv
    if len(args) < 5:
        print()
        print("How to Run:")
        print()
        print("python3 process_sessions.py <do_log_path> <output_dir_path> <act24_file> <file_id>")
        print("\t<do_log_path> - path to do_log_final.csv")
        print("\t<output_dir_path> - path to directory to store output files in")
        print("\t<act24_file> - processed act24 data (time,x,y,z)")
        print("\t<file_id> - id for given act24 file (num in file name)")
        print()
        sys.exit()

    do_log = args[1]
    output_dir = args[2]
    act24_file = args[3]
    id = args[4]

    get_sessions(do_log, output_dir, act24_file, id)


