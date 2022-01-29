import datetime
import os
import time
import sys
import warnings

warnings.filterwarnings("ignore")


from pgdx_reporting import process
from pgdx_reporting import setup


if __name__ == "__main__":
    # set fixed locations
    elio_dir = os.path.abspath(os.path.join("/mnt", "pgdx_v1", "ElioConnect_Output",))
    req_dir = os.path.abspath(
        os.path.join("/mnt", "pgdx_v1", ".Bioinformatics", "requirements")
    )
    # if there's an input then process batch less than input days old
    try:
        input_duration = 25  # int(sys.argv[1])
        for dir in os.listdir(elio_dir):
            batch_dir = os.path.join(elio_dir, dir)
            time_dif = datetime.datetime(time.time() - os.path.getctime(batch_dir))
            # datetime.timedelta(
            # seconds=(
            # time.time() - os.path.getctime(batch_dir))
            # )
            print(batch_dir, time_dif)
            # if time_dif < input_duration:  # <- 8 usually
            #     print("GO!!!!")
            # process.pgdx_main(batch_dir, req_dir)
    # if not, process latest batch only
    except Exception as e:
        print(e)
        dir = setup.latest_batch_directory(elio_dir)
        batch_dir = os.path.join(elio_dir, dir)
        process.pgdx_main(batch_dir, req_dir)

