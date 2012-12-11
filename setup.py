from distutils.core import setup

setup(
    name = "wmd",
    version = "",
    description = "Linux Driver for the Nintendo Wii Remote",
    url = "http://forthewiin.org",
    scripts = [
      'WMD.py'
    ],
    packages = [
      'wmd',
      'wmd.EventBridges',
      'wmd.Gestures',
      'wmd.UI',
      'wmd.Wiimote',
      'wmd.Wiimote.Backends',
    ],
)
