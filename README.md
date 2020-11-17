# GitHub Grasp
Get single files from any public repository onto your computer.

### Installation

    pip3 install github-grasp

### Usage
Scrape a file:

    ghg scrape [OPTIONS]

    Options:
    -r, --repo TEXT    Target repository  [required]
    -b, --branch TEXT  Target branch (default: master)
    -f, --file TEXT    Path of target file  [required]
    -o, --output TEXT  Output to local file