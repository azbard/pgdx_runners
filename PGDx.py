from pgdx_reporting import process
from pgdx_reporting import setup
import os


if __name__ == "__main__":
    # %% set basic folders
    run_dir = os.path.abspath(os.curdir)  # MUST be run at root of pgdx SFA
    elio_dir = os.path.abspath(os.path.join(run_dir, r"ElioConnect_Output"))
    req_dir = os.path.join(run_dir, ".Bioinformatics", "requirements")

    while True:
        user_input = setup.get_user_input()

        if user_input == "":
            # if user just hits enter then get latest batch folder
            latest_batch = setup.latest_batch_directory(elio_dir)
            if latest_batch == "None":
                input("\nCannot find a batch folder!\nPress enter to continue.\n")
                continue
            else:
                batch_dir = os.path.join(elio_dir, latest_batch)
                break

        else:
            # set batch dir using input if found
            batch_dir_name = setup.get_dir_from_batch(elio_dir, user_input)
            if batch_dir_name == "None":
                input("\nCannot find that batch!\nPress enter to continue.\n")
                continue
            else:
                batch_dir = os.path.join(elio_dir, batch_dir_name)
                break

    process.pgdx_process(batch_dir, req_dir)

