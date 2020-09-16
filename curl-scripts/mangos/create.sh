#!/bin/bash

curl "http://localhost:8000/decks" \
  --include \
  --request POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Token ${TOKEN}" \
  --data '{
    "deck": {
      "name": "'"${NAME}"'",
      "color": "'"${COLOR}"'",
      "ripe": "'"${RIPE}"'"
    }
  }'

echo
