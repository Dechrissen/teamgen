# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.utils.hooks import collect_submodules
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
    binaries=[],          # keep binaries separate
    datas=datas,
    hiddenimports=hiddenimports,
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
# Keep runtime binaries hidden in '_internal' folder
# --------------------------
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='teamgen',
    # move all binaries to _internal subfolder
    # datas like config/ stay at top level
)

