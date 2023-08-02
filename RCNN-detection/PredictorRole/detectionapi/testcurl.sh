#/bin/bash
echo "root"
curl -X GET -L 'http://127.0.0.1:8083/'
echo "\n" + "detect"
curl -X GET -L 'http://127.0.0.1:8083/detect/'