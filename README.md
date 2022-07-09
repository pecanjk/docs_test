# mkdocs test

## Requirements
``` bash
pip install -r requirements.txt
```

## How To

``` bash
mkdir docs
cd docs
mkdocs new . #- Create a new project.
mkdocs build #build and generate static html folder 'site'. put site/ into .gitignore
mkdocs serve #visit local site
```

### Project Layout
```
mkdocs.yml    # The configuration file.
docs/
    index.md  # The documentation homepage.
    ...       # Other markdown pages, images and other files.
```

