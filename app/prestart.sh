#!/usr/bin/env bash

set -e

echo "Run apply migrations"
alembic upgrade head
echo "Migration applied"

exec "$@"