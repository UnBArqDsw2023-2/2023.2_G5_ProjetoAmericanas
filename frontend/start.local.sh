#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

export VITE_APP_BACKEND_URL=$BACKEND_URL

# npm run dev
vite --port 3000 --host 0.0.0.0
