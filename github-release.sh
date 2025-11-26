#!/bin/bash
set -e

# ----------------------------
# 1. Read version from version.py
# ----------------------------
VERSION=$(grep "__version__" version.py | sed 's/.*"\(.*\)".*/\1/')
echo "Detected version: $VERSION"

# ----------------------------
# 2. (No need to modify spec file anymore)
# ----------------------------
echo "No spec modification needed for Windows-safe version=None"

# ----------------------------
# 3. Commit version.py if needed
# ----------------------------
git add version.py
git commit -m "Bump version to $VERSION" || echo "No changes to commit"

# ----------------------------
# 4. Create git tag
# ----------------------------
TAG="v$VERSION"
git tag $TAG

# ----------------------------
# 5. Push commit and tag
# ----------------------------
git push
git push origin $TAG
echo "Pushed tag $TAG"

echo "Done. GitHub Action will now build your EXE for $TAG."
