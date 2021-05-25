# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['Bat_and_Ball_May_2021_Update.py'],
             pathex=['D:\\Coding Series\\Python Family\\In-book\\Graphics Series\\Bat and Ball May 2021 Update and Minesweeper May 2021 Update US - VN version'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Bat_and_Ball_May_2021_Update',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
