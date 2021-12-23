from setuptools import setup
APP =["tkinter_time.py"]
OPTIONS={
      'argv_emulation':True,
      }
      
setup(
    app = APP,
    options = {'py2app':OPTIONS},
    setup_requires = ['py2app']
)
