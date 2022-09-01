from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'Console'

executables = [
    Executable('notes50.py', base=base)
]

setup(name='Notes50',
      version = '1.0',
      description = 'CS50 Notes And Psets Reader',
      options = {'build_exe': build_options},
      executables = executables)
