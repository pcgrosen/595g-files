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

apt install -y virtualenv 2> /dev/null

virtualenv "${CHALLENGE}-env"
source "${CHALLENGE}-env/bin/activate"

pip install flask

JUMBLE=$(python -c 'import random; import string; print("".join(random.choice(string.ascii_letters) for _ in range(64)))')
echo "595g{$JUMBLE}" > flag

cat > /lib/systemd/system/595g-${CHALLENGE}.service <<EOF
[Unit]
Description=systemd service for 595g challenge $CHALLENGE

[Service]
User=$CHALLENGE
Group=$CHALLENGE
Environment=PATH=$DIR/${CHALLENGE}-env/bin
WorkingDirectory=$DIR
ExecStart=$DIR/${CHALLENGE}-env/bin/python server.py

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable 595g-${CHALLENGE}
systemctl start 595g-${CHALLENGE}
