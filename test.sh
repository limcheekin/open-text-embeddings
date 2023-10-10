gzip -c text.json | curl -H "Content-Encoding: gzip" -H "Content-Type: application/json" -X POST --data-binary @- $1
