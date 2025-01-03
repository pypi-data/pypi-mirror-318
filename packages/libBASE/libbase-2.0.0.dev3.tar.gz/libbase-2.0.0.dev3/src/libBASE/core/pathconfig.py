#!/bin/bash
import importlib.resources
import os
import platform


def getdatapath(package, resource):
    with importlib.resources.path(package, resource) as ans:
        return str(ans)


# set local paths
igblast_internal_data = "/ncbi-igblast-1.15.0/internal_data"
igblast_auxiliary_data = "/ncbi-igblast-1.15.0/optional_file/human_gl.aux"
constantdb = getdatapath("BASEoriginaldata.data.db", "human_gl_C.fasta")
blast_path = "blastn"
igblast_path = "/ncbi-igblast-1.15.0/bin/igblastn"

"""these germline db files are saved in the / directory"""
germlinedb_V = getdatapath("BASEoriginaldata.data.db", "V_without_orphons")
germlinedb_J = getdatapath("BASEoriginaldata.data.db", "J_without_orphons")
germlinedb_D = getdatapath("BASEoriginaldata.data.db", "D_without_orphons")
