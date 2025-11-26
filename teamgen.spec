# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT

block_cipher = None

# --------------------------
# Include data at top-level
# --------------------------
# The second element in each tuple is the target folder inside the dist folder
datas = [
    ('config', '.'),   # put config/ at top-level
    ('data', '.')      # optional, top-level
]

# --------------------------
# Analysis
# --------------------------
a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],          # binaries handled by COLLECT
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
    exclude_binaries=True,   # binaries handled by COLLECT
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
    a.datas,       # config/ and data/ go where we specified ('.')
    strip=False,
    upx=True,
    name='teamgen'
)

