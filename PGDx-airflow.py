import datetime
import os
import platform
import sys
import warnings

warnings.filterwarnings("ignore")

from pgdx_reporting import process
from pgdx_reporting import setup


def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    """
    if platform.system() == "Windows":
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime


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
            time_dif = (
                datetime.datetime.now()
                - datetime.datetime.fromtimestamp(creation_date(batch_dir))
            ).days

            if time_dif < input_duration:  # <- 8 usually
                process.pgdx_main(batch_dir, req_dir)

    # if not, process latest batch only
    except Exception as e:
        dir = setup.latest_batch_directory(elio_dir)
        batch_dir = os.path.join(elio_dir, dir)
        process.pgdx_main(batch_dir, req_dir)

