#!/bin/bash
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

# This script installs and configures everything the iris
# testing suite requires.
#!/usr/bin/env bash

set -ve
# This allows packages to be installed without human interaction
# export DEBIAN_FRONTEND=noninteractive


python3.7 -m pip install pipenv
python3.7 -m pip install psutil
python3.7 -m pip install zstandard
