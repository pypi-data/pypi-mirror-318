#!/bin/bash
import os
import platform

# set local paths
igblast_internal_data = "/ncbi-igblast-1.15.0/internal_data"
igblast_auxiliary_data = "/ncbi-igblast-1.15.0/optional_file/human_gl.aux"
constantdb = "/data/db/human_gl_C.fasta"
blast_path = "blastn"
igblast_path = "/ncbi-igblast-1.15.0/bin/igblastn"

"""these germline db files are saved in the / directory"""
germlinedb_V = "/data/db/V_without_orphons"
germlinedb_J = "/data/db/J_without_orphons"
germlinedb_D = "/data/db/D_without_orphons"
