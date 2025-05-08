# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['XCDE\\XCDE_Scripts\\XCDE_Randomizer.py'],
    pathex=[],
    binaries=[],
    datas=[('_internal/Images', 'Images'), ('XCDE/_internal/Images', 'Images'), ('XCDE/_internal/Toolset/bdat-toolset-win64.exe', 'Toolset'), ('scripts', 'scripts')],
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
    name='XCDE_Randomizer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['XCDE\\_internal\\Images\\XCDEIcon.ico'],
)
