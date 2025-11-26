# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],          # your main entry point
    pathex=[],
    binaries=[],
    datas=[
        ('config/*.yaml', 'config'),
        ('data/*.yaml', 'data')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='teamgen',
    console=True,        # CLI app
    debug=False,
    strip=False,
    upx=False,
    version=None         # <-- safe for Windows
)

