#/bin/bash
echo "root"
curl -X GET -L 'http://127.0.0.1:8000/'
echo "\n"
curl -X GET -L 'http://127.0.0.1:8000/sample/'