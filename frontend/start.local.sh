#!/bin/sh

set -o errexit
set -o pipefail
set -o nounset

# npm run dev
vite --port 3000 --host 0.0.0.0
