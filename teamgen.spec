# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

block_cipher = None

# --------------------------
# Include only necessary data
# --------------------------
datas = [
    ('config', 'config'),  # source folder, destination folder in dist
    ('data', 'data')       # optional
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
# Build the EXE
# --------------------------
exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,   # binaries will go in COLLECT
    name='teamgen',
    debug=False,
    strip=False,
    upx=True,
    console=True
)

# --------------------------
# Collect everything into dist/teamgen/
# config/ and data/ at top-level, runtime binaries in internal folder
# --------------------------
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='teamgen'
)

