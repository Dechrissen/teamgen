#!/bin/bash
set -e

# 1. Extract version from version.py
VERSION=$(grep "__version__" teamgen/version.py | sed 's/.*"\(.*\)".*/\1/')
echo "Detected version: $VERSION"

# 2. Update spec file
echo "Injecting version into teamgen.spec..."
sed -i "s/VERSION_PLACEHOLDER/$VERSION/" teamgen.spec

# 3. Commit spec file change (optional)
git add teamgen.spec
git commit -m "Update spec file for version $VERSION"

# 4. Create a Git tag
TAG="v$VERSION"
git tag $TAG

# 5. Push commits and tag
echo "Pushing tag $TAG..."
git push
git push origin $TAG

echo "Done. GitHub Action will now build your EXE."
