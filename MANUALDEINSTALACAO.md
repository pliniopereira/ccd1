Instalação testada no Linux Mint 18.1.

<!-- toc -->

## Used:
  * [python-sbigudrv 0.5](#python-sbigudrv0.5)
  * [Python 3.5](#python3.5)
  * [PyQt5](#pyqt5)
  * [Numpy](#numpy)
  * [PyFits](#pyfits)
  * [PyEphem](#pyephem)
  * [SciPy](#scipy)
  * [libusb-1.0-0-dev](#libusb-1.0-0-dev)
  * [libusb-dev](#libusb-dev)
  * [fxload](#fxload)
  * [msttcorefonts](#msttcorefonts)

<!-- toc stop -->

Instalação dos drivers da câmera:
<h1 id="python-sbigudrv0.5">python-sbigudrv 0.5</h1>
Descrição: Python wrappers for SBIG (tm) Universal Driver.

Author: [Paulo Henrique Silva](mailto:ph.silva@gmail.com), [Astrophysics Group](http://www.astro.ufsc.br/), 
[Universidade Federal de Santa Catarina](http://ufsc.br/).

Fonte: <https://pypi.python.org/pypi/python-sbigudrv/0.5>

Obs: Contatos da empresa fornecedora da Sbig: 

Web: ​ www.sbig.com​ E-mail: sbig@sbig.com

Resumo:
``` 
sudo apt-get install python3

sudo apt-get install python3-pyqt5 python3-numpy python3-pyfits python3-scipy python3-ephem libusb-1.0-0-dev libusb-dev fxload msttcorefonts
``` 
<h1 id="python3.5">Python 3.5</h1>

Instalação no terminal:
``` 
sudo apt-get install python3
``` 
#### Pacotes Python:
# PyQt5
Descrição: Qt is set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects of modern desktop and mobile systems. These include location and positioning services, multimedia, NFC and Bluetooth connectivity, a Chromium based web browser, as well as traditional UI development. PyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules and enables Python to be used as an alternative application development language to C++ on all supported platforms including iOS and Android.
PyQt5 may also be embedded in C++ based applications to allow users of those applications to configure or enhance the functionality of those applications.
Source: ​ https://pypi.python.org/pypi/PyQt5

Usado nas classes: main.py, business/logger.py, business/configuration/configProject.py ,
business/configuration/configSystem.py , business/configuration/settingsCamera.py,
business/configuration/schedulers/qthreadClock.py,
business/configuration/schedulers/qthreadSunMoon.py,
business/configuration/schedulers/qthreadTemperature.py,
business/configuration/Shooters/ContinuousShooterThread.py,
business/configuration/Shooters/EphemerisShooter.py,
business/configuration/Shooters/SThread.py, src/controler/cameraQThread.py,
ui/cameraSettingsWindow/main.py, ui/cameraSettingsWindow/settingsWindow.py,
ui/cameraSettingsWindow/tempRegulation.py, ui/commons/layout.py,
ui/commons/widgets.py, ui/continuousShooterWindow/continuousShooterWindow.py,
ui/continuousShooterWindow/main.py,
ui/ephemerisShooterWindow/ephemerisShooterWindow.py,
ui/ephemerisShooterWindow/main.py, ui/mainWindow/cameraInfo.py,
ui/mainWindow/ccdInfo.py, ui/mainWindow/clock.py, ui/mainWindow/configsInfo.py,
ui/mainWindow/consoleLogWidget.py, ui/mainWindow/ephemInfo.py,
ui/mainWindow/fanStatus.py, ui/mainWindow/main.py, ui/mainWindow/mainWindow.py,
ui/mainWindow/menubar.py, ui/mainWindow/shooter.py, ui/mainWindow/siteInfo.py,
ui/mainWindow/tempMonitor.py, ui/projectSettingsWindow/main.py,
ui/projectSettingsWindow/settingsWindow.py,
ui/projectSettingsWindow/widgetsGeography.py, ui/projectSettingsWindow/widgetsSite.py,ui/projectSettingsWindow/widgetsSun.py, ui/systemSettingsWindow/main.py,
ui/systemSettingsWindow/systemSettingsWindow.py,
ui/systemSettingsWindow/widgetsPath.py, ui/testWindow/main.py,
ui/testWindow/MainWindow.py, ui/testWindow/MainWindow2.py

Instalação no terminal:
``` 
sudo apt-get install python3-pyqt5
``` 
# numpy
Descrição: NumPy is a general-purpose array-processing package designed to efficiently manipulate large multi-dimensional arrays of arbitrary records without sacrificing too much speed for small multi-dimensional arrays. NumPy is built on the Numeric code base and adds features introduced by numarray as well as an extended C-API and the ability to create arrays of arbitrary type which also makes NumPy suitable for interfacing with general-purpose data-base applications.
There are also basic facilities for discrete fourier transform, basic linear algebra and random number generation.
Source: ​ https://pypi.python.org/pypi/numpy/1.12.0rc1

Usado na classe: [utils/camera/SbigDriver.py](https://github.com/pliniopereira/ccd10/blob/master/src/utils/camera/SbigDriver.py)

Instalação no terminal:
``` 
sudo apt-get install python3-numpy
``` 
# pyfits
Descrição: Reads FITS images and tables into numpy arrays and manipulates FITS headers.
Source: ​ https://pypi.python.org/pypi/pyfits/3.4

Usado na classe: [utils/camera/SbigDriver.py](https://github.com/pliniopereira/ccd10/blob/master/src/utils/camera/SbigDriver.py)

Instalação no terminal:
``` 
sudo apt-get install python3-pyfits
``` 
# scipy
Descrição: SciPy (pronounced “Sigh Pie”) is open-source software for mathematics, science, and engineering. The SciPy library depends on NumPy, which provides convenient and fast N-dimensional array manipulation. The SciPy library is built to work with NumPy arrays, and provides many user-friendly and efficient numerical routines such as routines for numerical integration and optimization. Together, they run on all popular operating systems, are quick to install, and are free of charge. NumPy and SciPy are easy to use, but powerful enough to be depended upon by some of the world’s leading scientists and engineers.
If you need to manipulate numbers on a computer and display or publish the results, give SciPy a try!
Source: ​ https://pypi.python.org/pypi/scipy/0.18.1Usado na classe: utils/camera/SbigDriver.py

Instalação no terminal:
``` 
sudo apt-get install python3-scipy
``` 
# PyEphem
Descrição: PyEphem provides an ephem Python package for performing high-precision astronomy computations. The underlying numeric routines are coded in C and are the same ones that drive the popular​ ​ XEphem​ astronomy application, whose author, Elwood Charles Downey, generously gave permission for their use in PyEphem. The name ephem is short for the word ​ ephemeris, which is the traditional term for a table giving the position of a planet, asteroid, or comet for a series of dates.
Source: ​ https://pypi.python.org/pypi/ephem/3.7.6.0

Usado nas classes: business/EphemObserverFactory.py,
business/schedulers/qthreadClock.py,
business/configuration/Shooters/EphemerisShooter.py, src/controller/camera.py,
controller/Ephemeris.py, ui/ephemerisShooterWindow/main.py,
ui/mainWindow/configsInfo.py

Instalação no terminal:
``` 
sudo apt-get install python3-ephem
``` 
--------------------------------------------------------------------------------------------------------------

<h1 id="libusb-1.0-0-dev">libusb-1.0-0-dev</h1>

Descrição: ​ libusb​ is a C library that provides generic access to USB devices. It is intended to be used by developers to facilitate the production of applications that communicate with USB hardware.
It is ​ portable​ : Using a single cross-platform API, it provides access to USB devices on Linux, OS X, Windows, Android, OpenBSD, etc.
It is ​ user-mode​ : No special privilege or elevation is required for the application to communicate with a device.
It is ​ version-agnostic​ : All versions of the USB protocol, from 1.0 to 3.0 (latest), are supported.
Source: ​ http://libusb.info/

Instalação no terminal:
``` 
sudo apt-get install libusb-1.0-0-dev
``` 
# libusb-dev
Descrição: Descrição: ​ libusb​ is a C library that provides generic access to USB devices. It is intended to be used by developers to facilitate the production of applications that communicate with USB hardware.
It is ​ portable​ : Using a single cross-platform API, it provides access to USB devices on Linux, OS X, Windows, Android, OpenBSD, etc.
It is ​ user-mode​ : No special privilege or elevation is required for the application to communicate with a device.
It is ​ version-agnostic​ : All versions of the USB protocol, from 1.0 to 3.0 (latest), are supported.
Source: ​ http://libusb.info/

Instalação no terminal:
``` 
sudo apt-get install libusb-dev
``` 
# fxload
Descrição: fxload is a program which downloads firmware to USB devices based onAnchorChips EZ-USB, Cypress EZ-USB FX, or Cypress EZ-USB FX2/FX2LPmicrocontrollers. These have 8-bit 8051 cores with special extensionsfor USB I/O. The FX2 supports high speed USB 2.0 transfers (480Mbit/sec) as well as full speed USB 1.1 transfers (12 Mbit/sec), whilethe earlier parts supports only full speed transfers. These con-trollers have several package options, and can be set up with externalmemory (on-chip memory is usually 8K or 16K), EEPROMs, and ROMs whendevice costs allow.
This uses "usbfs" (older name: "usbdevfs") to access devices, andissues vendor specific control requests to download and reset the EZ-USB devices. Normally, firmware will then "renumerate" by disconnect-ing from USB and then reconnecting as a new device. It then appearswith new device descriptors and functionality, as provided by thefirmware which has been downloaded.
To support some non-firmware applications, this can also set up sym-bolic links for those usbfs names. It can also change their accessmodes. Both of these can help simplify software applications that needto talk to USB devices using user mode drivers, don't want to run withprivileges or to examine all of the existing USB evices, and whichdon't need more kernel drivers.
See the Linux-Hotplug web site for information about how to use fxloadto download device firmware when hotplugging USB devices, using driver-specific scripts stored in the /etc/hotplug/usb directory.

Instalação no terminal:
``` 
sudo apt-get install fxload
``` 
# msttcorefonts
Descrição: The TrueType core fonts for the web that were once available from <http://www.microsoft.com> typography/fontpack/. The port is constructedso that theactual fonts are downloaded from Sourceforge's site atbuild time so this port does not 'redistribute' the fonts, it justmakes it easy to install them on an OpenBSD system.
Source: ​ http://ports.su/fonts/msttcorefonts

Usado na classe: [utils/camera/SbigDriver.py](https://github.com/pliniopereira/ccd10/blob/master/src/utils/camera/SbigDriver.py) para desenhar na imagem os dados.

Instalação no terminal:
``` 
sudo apt-get install msttcorefonts
``` 
