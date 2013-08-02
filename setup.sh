#!/bin/bash
set -x
set -e

ARCHIVE_DIR=$HOME/Downloads
REQUIRE_DIR=.
REQUIRE_FILE=$REQUIRE_DIR/requirements.txt

echo "Downloading required packages"
pip install --download $ARCHIVE_DIR -r $REQUIRE_FILE

echo "Installing package archives"
pip install --no-index --find-links=$ARCHIVE_DIR -r $REQUIRE_FILE
