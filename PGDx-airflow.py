import datetime
import os
import time
import sys
import warnings

warnings.filterwarnings("ignore")


from pgdx_reporting import process


if __name__ == "__main__":
    # set fixed locations
    elio_dir = os.path.abspath(os.path.join("/mnt", "pgdx_v1", "ElioConnect_Output",))
    req_dir = os.path.abspath(
        os.path.join("/mnt", "pgdx_v1", ".Bioinformatics", "requirements")
    )
    # if there's an input then process batch less than input days old
    try:
        input_duration = int(sys.argv[1])
        for dir in os.listdir(elio_dir):
            batch_dir = os.path.join(elio_dir, dir)
            time_dif = datetime.timedelta(
                seconds=(time.time() - os.path.getctime(batch_dir))
            ).days
            if time_dif < input_duration:  # <- 8 usually
                process.pgdx_main(batch_dir, req_dir)
    # if not, process latest batch only
    except Exception as e:
        print(e)
        dirs = [os.path.join(elio_dir, dir) for dir in os.listdir(elio_dir)]
        batch_dir = max(dirs, key=os.path.getctime)
        process.pgdx_main(batch_dir, req_dir)

