#!/bin/bash
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# This script installs and configures everything the iris
# testing suite requires.
#!/usr/bin/env bash

export DISPLAY=:0
apt install fluxbox -y
set -ve

# Set up a virtual display since we don't have an xdisplay
. $HOME/scripts/xvfb.sh
start_xvfb '1920x1080x24+32' 0

# Re-set `+e` after start_xvfb changes it
set +e

# Start fluxbox
fluxbox &

#Take a screenhot
gnome-screenshot --file=screenshot.png

# cd /app && pipenv install
