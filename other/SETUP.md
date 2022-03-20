# Setup

## Necessary files for installation

- web.zip
  - data/
    - defImage.png
    - Template.sql
  - static/
  - templates/
  - \_\_main\_\_.py
  - LICENSE
  - README.md
  - run.sh
  - serverLib's wheel file

- setup.py

- setup.sh

## Setup script

 1. Unzips files from `data.zip`
 2. Generate `mainConfig.json` for serverLib
 3. Install the `serverLib` package from its wheel file
 4. Create the database according to `Template.sql`
 5. Get and hash an admin password
 6. Remove installation files

## PI Commands

### Installation commands

```sh
wget "https://github.com/JosephAbbey/PAPICompetition-LostProperty/releases/latest/download/install.sh"; bash ./install.sh
```

### Run command

```sh
bash ./run.sh
```
