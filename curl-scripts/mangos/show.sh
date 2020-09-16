#!/bin/bash

curl "http://localhost:8000/decks/${ID}" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
