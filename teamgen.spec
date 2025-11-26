# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_submodules
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT
from PyInstaller.utils.hooks import Tree

block_cipher = None

# --------------------------
# Include folders as trees
# --------------------------
datas = [
    Tree('config', prefix='config'),   # copies the entire config folder as-is
    Tree('data', prefix='data')        # optional
]

# --------------------------
# Analysis
# --------------------------
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],          # binaries go to COLLECT
    datas=datas,
    hiddenimports=[],     # none
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    cipher=block_cipher,
    noarchive=False
)

# --------------------------
# Build PYZ
# --------------------------
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# --------------------------
# Build EXE
# --------------------------
exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name='teamgen',
    debug=False,
    strip=False,
    upx=True,
    console=True
)

# --------------------------
# Collect into dist/teamgen/
# --------------------------
coll = COLLECT(
    exe,
    a.binaries,    # runtime .pyd/.dll files
    a.zipfiles,
    a.datas,       # Tree preserves folder structure
    strip=False,
    upx=True,
    name='teamgen'
)

