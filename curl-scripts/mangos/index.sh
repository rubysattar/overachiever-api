#!/bin/bash

curl "http://localhost:8000/decks" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}"

echo
