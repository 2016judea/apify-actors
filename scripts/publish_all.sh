#!/bin/bash
# Flip every tested, priced actor in ledger.tsv to public in the Apify Store.
# Run once after the account owner accepts the Store terms (console.apify.com -> any actor -> Publication).
cd "$(dirname "$0")/.."
T=$(security find-generic-password -s com.apify.cli -a token -w)
awk -F'\t' 'NR>1 && $8 ~ /priced/ {print $1}' ledger.tsv | while read -r a; do
  r=$(curl -s -X PUT "https://api.apify.com/v2/acts/cheerful_term~$a" -H "Authorization: Bearer $T" \
      -H 'content-type: application/json' -d '{"isPublic":true}')
  if echo "$r" | grep -q '"isPublic":true'; then
    echo "PUBLIC $a"
    sed -i '' "s#\(^$a\t.*\t\)priced-awaiting-store-terms\$#\1public-priced#" ledger.tsv
  else
    echo "FAILED $a $(echo "$r" | head -c 200)"
  fi
done
