#!/bin/bash

set -e

echo "getting latest code..."
git pull

echo "building..."
docker compose build

echo "deploying..."
docker compose up -d