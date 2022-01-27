import os
from pgdx_reporting import pgdx_process


if __name__ == "__main__":
    # # this for testing only
    batch_dir = os.path.abspath(
        os.path.join(
            "..", "pgdx-reporting", "ElioConnect_Output", "B22-4_ETCR-CFX-545448"
        )
    )
    req_dir = os.path.abspath("requirements")
    pgdx_process(batch_dir, req_dir)
