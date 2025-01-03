=======
libBASE
=======

Overview
--------

This project is the adaptation of libBASE from the CodeOcean capsule. See the original paper for more information.

Installation
------------

To install ``libBASE``, you can use ``pip``. Open your terminal and run:

.. code-block:: bash

    pip install libBASE

License
-------

The license can be found in the LICENSE file.

Links
-----

* `Documentation <https://pypi.org/project/libBASE>`_
* `Download <https://pypi.org/project/libBASE/#files>`_
* `Original Paper <https://pubmed.ncbi.nlm.nih.gov/33032524/>`_
* `Source <https://github.com/johannes-programming/libBASE>`_

Original README.md
------------------

.. code-block:: md

    # Brain Antibody Sequence Evaluation (BASE): an easy-to-use software for complete data analysis in single cell immunoglobulin cloning

    In this capsule, we provide the validation dataset of BASE functionality as described in (Reincke et al. 2019). To interactively use the functionality of BASE, please launch a CloudWorkstation. Additionally, we provide all the raw sequencing data corresponding to (Kreye et al. 2021).

    # Background information about BASE
    Repertoire analysis of patient-derived recombinant monoclonal antibodies is an important tool to study the role of B cells in autoimmune diseases of the human brain and beyond. Current protocols for generation of patient-derived recombinant monoclonal antibody libraries are time-consuming and contain repetitive steps, some of which can be assisted with the help of software automation. We developed BASE, an easy-to-use software for complete data analysis in single cell immunoglobulin cloning. BASE consists of two modules: aBASE for immunological annotations and cloning primer lookup, and cBASE for plasmid sequence identity confirmation before expression.

    BASE offers an easy-to-use software solution suitable for complete Ig sequence data analysis and tracking during recombinant mcAB cloning from single cells. Plasmid sequence identity confirmation by cBASE offers functionality not provided by existing software solutions in the field and will help to reduce time-consuming steps of the monoclonal antibody generation workflow.

    # Data generated in this capsule
    In the capsule, the aBASE and cBASE validation datasets are generated from the sequence files in /data/SeqData. This dataset includes all monoclonal antibody chains of unknown specificity from a CSF cell sample processed using mcAB repertoire cloning in our laboratory (sample ID #AI ENC 113, Kreye et al. in preparation).
    1. aBASE validation: This capsule runs aBASE on the input file aBASE-113-input.xlsx. aBASE automatically generates immunological annotations and cloning primer lookups and saves the output to /results/aBASE-output.xlsm. To validatate aBASE, we compared the automatic analysis with our own previous manual analysis (Reincke et al. 2019).
    2. cBASE validation: This capsule runs cBASE on the input file cBASE-113-input.xlsx. cBASE aligns and compares the plasmid Ig sequence with the amplified cDNA-derived Ig sequence by displaying nucleotide differences and saves the output to /results/cBASE-output.xlsx. In this file, we included our previous manual analysis in column D as well as our interpretation of the differences in column G.

    # Update 2021-09-05
    Five additional antibody sequences have been deposited in the capsule after publication of the corresponding manuscript "Encephalitis patient derived monoclonal GABAA receptor antibodies cause epileptic seizures" (Kreye et al. 2021).


    # References and Links

    S. Momsen Reincke,  Harald Prüss,  Jakob Kreye. "Brain Antibody Sequence Evaluation (BASE): an easy-to-use software for complete data analysis in single cell immunoglobulin cloning". bioRxiv. doi: https://doi.org/10.1101/836999.

    J. Kreye et al., "Encephalitis patient derived monoclonal GABAA receptor antibodies cause epileptic seizures". Journal of Experimental Medicine. doi: https://doi.org/10.1084/jem.20210012.

    For more information, updates of the software, and instructions for standalone installations, see: https://github.com/automatedSequencing/BASE.
