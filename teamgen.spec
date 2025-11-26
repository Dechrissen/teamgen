# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# Include all hidden imports (if needed)
hiddenimports = collect_submodules('')

# Add data folders: source → target
datas = [
    ('config', 'config'),
    ('data', 'data'),
]

a = Analysis(
    ['main.py'],          # entry point
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='teamgen',       # EXE name
    debug=False,
    strip=False,
    upx=True,
    console=True          # show console window
)

# No onefile, so this will produce a folder build (default)
