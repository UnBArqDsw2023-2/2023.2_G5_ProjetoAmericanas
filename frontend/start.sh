#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

npm run build
# tsc
# vite build
# vite optimize
