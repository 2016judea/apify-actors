#!/bin/bash
# Flip tested, priced actors in ledger.tsv to public in the Apify Store, highest-demand first.
# Apify allows 5 publications per day; this stops at the limit, so it runs daily from launchd
# (~/Library/LaunchAgents/local.apify-publish.plist). launchd runs it from a clone at
# ~/.local/share/apify-actors, NOT ~/Desktop: macOS privacy blocks launchd from Desktop (exit 127). until nothing is left, then unloads itself.
cd "$(dirname "$0")/.."
git pull -q --rebase || true
T=$(security find-generic-password -s com.apify.cli -a token -w)
# Broad, recurring buyer demand first (compliance, finance, healthcare, Reddit); Twin Cities last.
FIRST="sec-insider-trades sec-edgar-full-text-search ofac-sanctions-screening oig-exclusions-screening npi-registry sec-company-financials sec-edgar-filings reddit-subreddit-posts reddit-post-comments usaspending-awards socrata-dataset-query fdic-banks openfda-recalls openfda-device-clearances grants-gov-opportunities"
pending=$(awk -F'\t' 'NR>1 && $8 == "priced-awaiting-store-terms" {print $1}' ledger.tsv)
order=$( { for a in $FIRST; do echo "$pending" | grep -qx "$a" && echo "$a"; done; echo "$pending"; } | awk '!seen[$0]++' )
[ -z "$order" ] && { echo "nothing left to publish"; launchctl unload ~/Library/LaunchAgents/local.apify-publish.plist 2>/dev/null; exit 0; }
for a in $order; do
  r=$(curl -s -X PUT "https://api.apify.com/v2/acts/cheerful_term~$a" -H "Authorization: Bearer $T" \
      -H 'content-type: application/json' -d '{"isPublic":true}')
  if echo "$r" | python3 -c "import json,sys;sys.exit(0 if json.load(sys.stdin).get('data',{}).get('isPublic') else 1)"; then
    echo "$(date '+%F %T') PUBLIC $a"
    sed -i '' "s#^\($a	.*	\)priced-awaiting-store-terms\$#\1public-priced#" ledger.tsv
  elif echo "$r" | grep -q daily-publication-limit-exceeded; then
    echo "$(date '+%F %T') daily limit reached; $(echo "$order" | wc -l | tr -d ' ') were pending"; break
  elif echo "$r" | grep -q more-public-actors-require-verified-owner; then
    echo "$(date '+%F %T') BLOCKED: Apify needs owner identity verification (console.apify.com)"; break
  else
    echo "$(date '+%F %T') FAILED $a $(echo "$r" | tr -d '\n' | head -c 200)"
  fi
done
git add ledger.tsv && git commit -qm "Publish batch $(date +%F)" && git push -q
