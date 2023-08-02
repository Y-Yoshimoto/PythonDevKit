#!/bin/bash
unitd --no-daemon --control unix:/var/run/control.unit.sock &

curl -X PUT -d @/www/start.json --unix-socket /var/run/control.unit.sock http://localhost/ \
    && tail -f /www/start.json
