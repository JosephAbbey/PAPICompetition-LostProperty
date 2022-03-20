# Setup

## Necessary files for installation

- web.zip
  - data/
    - defImage.png
    - Template.sql
  - templates/
  - static/
  - serverLib's wheel file
  - \_\_main\_\_.py

- setup.py

- setup.sh

## Setup script

 1. Unzips `static/`, `templates/`, `data/`, `serverLib`'s wheel file, and `__main__.py` from `data.zip`
 2. Generate `mainConfig.json` for serverLib
 3. Install the `serverLib` package from its wheel file
 4. Create the database according to `Template.sql`
 5. Get and hash an admin password
 6. Remove installation files

## PI Commands

### Installation commands

```sh
wget "https://github.com/JosephAbbey/PAPICompetition-LostProperty/releases/download/v1.0.1/install.sh"; bash ./install.sh
```

### Run command

```sh
bash ./run.sh
```
