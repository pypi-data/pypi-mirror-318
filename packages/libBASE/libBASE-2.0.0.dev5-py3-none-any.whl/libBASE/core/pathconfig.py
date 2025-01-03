#!/bin/bash
import os

import BASEoriginaldata


def getconstantdb():
    file = BASEoriginaldata.getdatapath("data", "db", "__init__.py")
    dirname = os.path.dirname(file)
    ans = os.path.join(dirname, "human_gl_C.fasta")
    return ans


# set local paths
igblast_internal_data = "/ncbi-igblast-1.15.0/internal_data"
igblast_auxiliary_data = "/ncbi-igblast-1.15.0/optional_file/human_gl.aux"
constantdb = getconstantdb()
blast_path = "blastn"
igblast_path = "/ncbi-igblast-1.15.0/bin/igblastn"

"""these germline db files are saved in the / directory"""
germlinedb_V = BASEoriginaldata.getdatapath("data", "db", "V_without_orphons")
germlinedb_J = BASEoriginaldata.getdatapath("data", "db", "J_without_orphons")
germlinedb_D = BASEoriginaldata.getdatapath("data", "db", "D_without_orphons")
