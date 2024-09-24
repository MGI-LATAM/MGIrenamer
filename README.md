# MGIrenamer

This repository stores a script to convert FASTQ file names from MGI format to Illumina format.

## Definition

**mgirenamer** is a Python script that renames `FASTQ` files from an MGI routine directory to another directory, and the names are converted to Illumina format. MGI to Illumina fastq name converter.

### How to use

```bash
mgirenamer.py -h
```

#### Help

```bash
usage: mgirenamer.py [-h] source_directory destination_directory flowcell lane

Rename files in a directory

positional arguments:
  source_directory      Directory with the original files
  destination_directory
                        Destination directory for renamed files
  flowcell              Flowcell ID
  lane                  Lane ID, e.g., L01

options:
  -h, --help            show this help message and exit
```

#### Usage

```bash
python mgirenamer.py diretorio_origem diretorio_destino flowcell lane 
```

- All libraries required in this script are already installed on the DNBSEQ sequencers, so they do not need to be installed.
