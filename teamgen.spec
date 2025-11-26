# teamgen.spec — minimal, works with local config/data

block_cipher = None

a = Analysis(
    ['main.py'],             # entry point in teamgen/
    pathex=[],
    binaries=[],
    datas=[
        ('config/', 'config'),   # include all files in config/
        ('data/', 'data'),       # include all files in data/
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='teamgen',
    console=True,                  # CLI UI
    debug=False,
    strip=False,
    upx=False,
    version='VERSION_PLACEHOLDER', # will be replaced by your bump_and_release.sh
)

