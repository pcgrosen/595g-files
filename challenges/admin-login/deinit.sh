#!/bin/bash

# If you're just trying to solve the challenge, you can safely ignore this file.

# https://stackoverflow.com/questions/59895/getting-the-source-directory-of-a-bash-script-from-within
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"

cd "$DIR"
CHALLENGE=$(basename "$DIR")

systemctl -q stop 595g-${CHALLENGE}
systemctl -q disable 595g-${CHALLENGE}
rm /lib/systemd/system/595g-${CHALLENGE}.service
systemctl -q daemon-reload
