#!/bin/bash
set -e

# ----------------------------
# Read version from version.py
# ----------------------------
VERSION=$(grep "__version__" version.py | sed 's/.*"\(.*\)".*/\1/')
echo "Detected version: $VERSION"

# ----------------------------
# Commit version.py if needed
# ----------------------------
git add version.py
git commit -m "Bump version to $VERSION" || echo "No changes to commit"

# ----------------------------
# Create git tag
# ----------------------------
TAG="v$VERSION"
git tag $TAG

# ----------------------------
# Push commit and tag
# ----------------------------
git push
git push origin $TAG
echo "Pushed tag $TAG"

echo "Done. GitHub Action will now build EXE for $TAG."
