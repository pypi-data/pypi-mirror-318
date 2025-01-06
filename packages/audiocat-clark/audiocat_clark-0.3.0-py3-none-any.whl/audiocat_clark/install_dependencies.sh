#!/bin/bash
set -e
set -x
set -o pipefail

sudo $(which apt) update
sudo $(which apt) install minimodem
sudo $(which apt) install gpg
