#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

export VITE_APP_BACKEND_URL=$BACKEND_URL

npm run build
# tsc
# vite build
# vite optimize
