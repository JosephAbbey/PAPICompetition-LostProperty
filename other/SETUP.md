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

 - setup.sh


# Setup script

 1. Unzips `static/`, `templates/`, `data/`, `serverLib`'s wheel file, and `__main__.py` from `data.zip`
 2. Generate `mainConfig.json` for serverLib
 3. Install the `serverLib` package from its wheel file
 4. Create the database according to `Template.sql`
 5. Get and hash an admin password
 6. Remove installation files

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
sudo sudo chmod -R a+rwx ./
sudo python3 ./install.py
```

### Installation commands

```
Some wget or git command

sudo sh install.bat
```

### Run command

```
uwsgi --socket 0.0.0.0:8000 --protocol=http --file __main__.py --callable app
```