#!/bin/bash

curl "http://localhost:8000/decks/${ID}" \
  --include \
  --request DELETE \
  --header "Authorization: Token ${TOKEN}"

echo
