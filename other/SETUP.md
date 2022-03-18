# Necessary files for installation:

 - web.zip
   - data/
      - defImage.png
      - Template.sql
   - templates/
   - static/
   - serverLib's wheel file
   - \_\_main\_\_.py

 - setup.py


# Setup script

 1. Unzips `static/`, `templates/`, `data/`, `serverLib`'s wheel file, and `__main__.py` from `data.zip`
 2. Install the `serverLib` package from its wheel file
 2. Generate `mainConfig.json` for serverLib
 3. Create the database according to `Template.sql`
 4. Gets and hashes an admin password

# PI Commands:

### install.sh

```
#!/bin/sh

# Install required packages
sudo apt-get install nginx
sudo apt-get install python3-pip

# Install uwsgi
sudo pip3 install uwsgi

# Install the actual LostProperty system
sudo chown www-data LostProperty/
sudo python3 LostProperty/install.py
```

### Installation commands

```
Some wget or git command

sudo bash install.bat
```

### Run command

```
uwsgi --socket 0.0.0.0:8000 --protocol=http --file LostProperty/__main__.py --callable app
```

