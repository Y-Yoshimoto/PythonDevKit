host="localhost"
port="8000"
domein="http://$host:$port"

# rootパス
#curl ${domein}/

# curl ${domein}/RestSample/2

# curl ${domein}/RestSample/2 -X POST -H "Content-Type: application/json" -d '{"id":2, "name":"test", "date": "2024-08-09"}'
# curl ${domein}/RestSample/ -X POST -H "Content-Type: application/json" -d '{"id":2, "name":"test"}'

# curl ${domein}/RestSample/ -X PUT -H "Content-Type: application/json" -d '{"id":2, "name":"test"}'

# curl ${domein}/GraphQLSample/graphql

curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"query": "{ user { id name age } }"}' \
  ${domein}/GraphQLSample/graphql

# doc
# curl ${domein}/docs