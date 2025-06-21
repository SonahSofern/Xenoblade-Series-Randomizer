# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Randomizer.py'],
    pathex=[],
    binaries=[],
    datas=[('images', 'images'), ('XC2/Images', 'XC2/Images'), ('XCDE/Images', 'XCDE/Images'), ('XC3/Images', 'XC3/Images'), ('XCXDE/Images', 'XCXDE/Images'), ('Toolset', 'Toolset'), ('scripts', 'scripts')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Randomizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['images\\XCIcon.ico'],
)
