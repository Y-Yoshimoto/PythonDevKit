host="localhost"
port="8000"
domein="http://$host:$port"

# rootパス
#curl ${domein}/

# curl ${domein}/methodsample/2

# curl ${domein}/methodsample/2 -X POST -H "Content-Type: application/json" -d '{"id":2, "name":"test", "date": "2024-08-09"}'
curl ${domein}/methodsample/ -X POST -H "Content-Type: application/json" -d '{"id":2, "name":"test"}'
# doc
# curl ${domein}/docs