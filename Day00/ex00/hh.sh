#!/bin/sh

OUTPUT_FILE="./hh.json"
VACANCY_AMOUNT="20"
JQ="/Users/marlean/homebrew/bin/jq"


VACANCY_NAME="${1/ /+}"

curl -k -H 'User-Agent: api-test-agent' -G "https://api.hh.ru/vacancies?text=$VACANCY_NAME&per_page=$VACANCY_AMOUNT" | $JQ > $OUTPUT_FILE

#run the script       ./hh.sh 'data scientist'