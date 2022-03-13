# Necessary files for installation:

 - web.zip
   - data/
      - defImage.png
      - Template.sql
   - templates/
   - static/
   - serverLib/
   - \_\_main\_\_.py

 - setup.py


# Setup script

 1. Unzips `static/`, `templates/`, and `data/` from `data.zip`
 2. Generate `mainConfig.json` for serverLib
 3. Create the database according to `Template.sql`
 4. Gets and hashes an admin password

# PI Commands:

```
sudo apt-get install nginx
sudo apt-get install python3-pip
sudo pip3 install uwsgi

Some wget or git command

sudo chown www-data LostProperty/
sudo python3 install.py
uwsgi --socket 0.0.0.0:80 --protocol=http --file __main__.py --callable app
```