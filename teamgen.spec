# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT
import os

block_cipher = None

# --------------------------
# Data folders (copy intact)
# --------------------------
datas = [
    ('config', 'config'),
    ('data', 'data')
]

# --------------------------
# Analysis
# --------------------------
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
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
    a.binaries,
    a.zipfiles,
    a.datas,     # datas go to the exact folder specified in the tuple
    strip=False,
    upx=True,
    name='teamgen'
)


