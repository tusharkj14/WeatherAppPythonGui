from kivy_deps import sdl2, glew

# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['WeatherApp.py'],
             pathex=['C:\\Users\\91836\\Desktop\\Studi\\PythonGUI\\kivyApp\\kivy1'],
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

a.datas += [('Code\KVDesign.kv', 'C:\\Users\\91836\\Desktop\\Studi\\PythonGUI\\kivyApp\\kivy1\KVDesign.kv', 'DATA')]

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='WeatherApp',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               Tree('C:\\Users\\91836\\Desktop\\Studi\\PythonGUI\\kivyApp\\kivy1'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               upx_exclude=[],
               name='WeatherApp')
