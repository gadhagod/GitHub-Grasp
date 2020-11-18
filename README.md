# GitHub Grasp
Grasp single files from any public repository onto your computer.

### Installation

    pip3 install github-grasp

### Usage
Scrape a file:

    ghg scrape [OPTIONS]

    Options:
    -r, --repo TEXT    Target repository  [required]
    -b, --branch TEXT  Target branch (default: master)
    -f, --file TEXT    Path of target file  [required]
    -o, --output TEXT  Output to local file'

### Example
Let's say you wanted the file `scripts/authors` from Facebook's [React Repository](https://github.com/facebook/react). \
You could use `git clone`, but the repository is **massive**, and you just need a single file. \
To echo the contents file:

    ghg scrape -r facebook/react -f scripts/authors
    

If you wanted to save the file locally, run the same command, but with the `--output` option.

    ghg scrape -r facebook/react -f scripts/authors -o authors.sh

Now you have `authors.sh` on your computer! \
If you wanted a file from a specific branch, you add the option `--branch`. \
So for example, if you wanted the file `.github/stale.yml` from the branch [`17.0.1`](https://github.com/facebook/react/tree/17.0.1) of the React repository, you would run...

    ghg scrape -r facebook/react -f .github/stale -b 17.0.1 -o test.yml