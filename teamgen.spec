# -*- mode: python ; coding: utf-8 -*-

import sys
from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

# Include all Python modules automatically detected
hiddenimports = collect_submodules('')

# Add data folders: (source, target) tuples
datas = [
    ('config', 'config'),
    ('data', 'data'),
]

a = Analysis(
    ['main.py'],                # your entry script
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
    name='teamgen',             # output EXE name
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True                # shows console window
)
