[app]

# (str) Title of your application
title = Frontenis Score

# (str) Package name
package.name = frontenis

# (str) Package domain (needed for android/ios packaging)
package.domain = org.frontenis

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
# AQUÍ ESTÁ LA CLAVE: Agregamos json y ttf
source.include_exts = py,png,jpg,kv,atlas,json,ttf

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
# AQUÍ AGREGAMOS PLYER PARA LA VIBRACIÓN
requirements = python3,kivy==2.3.0,plyer,android
android.accept_sdk_license = True

# (str) Presplash of the application (Pantalla de carga con tu logo)
presplash.filename = %(source.dir)s/icon.png

# (str) Icon of the application
icon.filename = %(source.dir)s/icon.png

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# AQUÍ ESTÁN LOS PERMISOS PARA VIBRAR Y GUARDAR IMAGENES
android.permissions = INTERNET,VIBRATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (list) The Android archs to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
# Esto asegura que funcione en celulares nuevos y viejos
android.archs = arm64-v8a, armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) The format used to package the app for debug mode (apk or aar).
android.debug_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
