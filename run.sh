#!/usr/bin/env bash

uwsgi --socket 0.0.0.0:8000 --protocol=http --file __main__.py --callable app
