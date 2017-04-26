import ctypes
import os
import sys
import time
from ctypes import c_ushort, POINTER, byref
from datetime import datetime

import numpy as np
import pyfits as fits

from src.utils.camera import Image_Processing
from src.utils.camera import SbigLib
from src.utils.camera import SbigStructures
from src.utils.camera.Julian_Day import jd_to_date, date_to_jd

'''
Faz a comunicação do software com a camera sbig, os comandos vem da classe camera.main.
'''

# Load Driver (DLL)
try:
    if sys.platform.startswith("linux"):
        # Linux driver
        udrv = ctypes.CDLL("libsbigudrv.so")
    elif sys.platform.startswith("win"):
        # Win Driver
        udrv = ctypes.windll.LoadLibrary("sbigudrv.dll")
except Exception as e:
    print(e)
    # ConsoleThreadOutput().raise_text("Não foi possível carregar o Driver.", 3)
    import platform

    try:
        bits, linkage = platform.architecture()
        if bits.startswith("32"):
            udrv = ctypes.windll.LoadLibrary("sbigudrv.dll")
        else:
            print("Invalid Python distribution Should be 32bits")
    except Exception as e:
        print(e)


def cmd(ccc, cin, cout):
    '''
    :param ccc:
    :param cin:
    :param cout:
    :return:
    '''
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]

    if cin is not None:
        cin = cin()
        cin = byref(cin)

    if cout is not None:
        cout = cout()
        cout = byref(cout)

    err = udrv.SBIGUnivDrvCommand(ccc, cin, cout)
    # print("Error: ", err)

    if err == 0:
        return True
    if ccc == SbigLib.PAR_COMMAND.CC_OPEN_DRIVER.value and err == SbigLib.PAR_ERROR.CE_DRIVER_NOT_CLOSED.value:
        # print("Driver already open!")
        return True
    elif ccc == SbigLib.PAR_COMMAND.CC_OPEN_DEVICE.value and err == SbigLib.PAR_ERROR.CE_DEVICE_NOT_CLOSED.value:
        # print("Device already open!")
        return True
    elif err:
        cin = SbigStructures.GetErrorStringParams
        cout = SbigStructures.GetErrorStringResults
        udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]

        cin = cin(errorNo=err)
        cout = cout()
        ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_GET_ERROR_STRING.value, byref(cin), byref(cout))
        print(ret, cout.errorString)
        return False


# Beginning Functions
# Open Driver
def open_driver():
    '''
    :return: usa o valor do drive instalado
    '''
    a = cmd(SbigLib.PAR_COMMAND.CC_OPEN_DRIVER.value, None, None)
    return a


# Open Device USB
def open_deviceusb():
    '''
    :return: conecta o manager com a camera via usb
    '''
    cin = SbigStructures.OpenDeviceParams
    cout = None
    try:
        udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
        cin = cin(deviceType=SbigLib.SBIG_DEVICE_TYPE.DEV_USB.value)
        ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_OPEN_DEVICE.value, byref(cin), cout)
        return ret == 0
    except Exception as e:
        return False, e


def close_driver():
    cdp = None
    cdr = None
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cdp), POINTER(cdr)]

    try:
        ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_CLOSE_DRIVER, None, None)

        if ret == SbigLib.PAR_ERROR.CE_NO_ERROR:
            return True
        else:
            return False

    except Exception as e:
        return False, e


def close_device():
    cdp = None
    cdr = None
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cdp), POINTER(cdr)]

    try:
        ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_CLOSE_DEVICE, None, None)

        if ret == SbigLib.PAR_ERROR.CE_NO_ERROR:
            return True
        else:
            return False
    except Exception as e:
        return False, e

'''
# Open Device Eth
def openDevice(ip):
    cin = SbigStructures.OpenDeviceParams
    cout = None
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
    ip.split(".")
    ip_hex = hex(int(ip[0])).split('x')[1].rjust(2, '0') + hex(int(ip[1])).split('x')[1].rjust(2, '0') +\
             hex(int(ip[2])).split('x')[1].rjust(2, '0') + hex(int(ip[3])).split('x')[1].rjust(2, '0')
    cin = cin(deviceType=SbigLib.SBIG_DEVICE_TYPE.DEV_ETH.value, ipAddress=long(ip_hex, 16))
    ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_OPEN_DEVICE.value, byref(cin), cout)
    print(ret)
'''


# Establishing Link
def establishinglink():
    '''
    :return: estabelece conexao do manager com a camera
    '''
    try:
        cin = SbigStructures.EstablishLinkParams
        cout = SbigStructures.EstablishLinkResults
        udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
        cin = cin(sbigUseOnly=0)
        cout = cout()
        ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_ESTABLISH_LINK.value, byref(cin), byref(cout))
        return ret == 0
    except Exception as e:
        return False, e


# Getting link status
def getlinkstatus():
    cin = None
    cout = SbigStructures.GetLinkStatusResults
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
    cout = cout()
    ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_GET_LINK_STATUS.value, cin, byref(cout))
    #print(ret, cout.linkEstablished, cout.baseAddress, cout.cameraType, cout.comTotal, cout.comFailed)
    return cout.linkEstablished == 1


def set_temperature(regulation, setpoint, autofreeze=True):
    '''
    pega os valores setados na classe Camera e manda para camera
    '''
    if regulation is True:
        temp_regulation = SbigLib.TEMPERATURE_REGULATION.REGULATION_ON
    else:
        temp_regulation = SbigLib.TEMPERATURE_REGULATION.REGULATION_OFF

    strp = SbigStructures.SetTemperatureRegulationParams2
    strr = None
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(strp), POINTER(strr)]

    strp = strp(regulation=temp_regulation, ccdSetpoint=setpoint)

    # First call must set temperature parameters
    ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_SET_TEMPERATURE_REGULATION2, byref(strp), None)

    if ret == SbigLib.PAR_ERROR.CE_NO_ERROR and autofreeze is False:
        return True
    elif ret == SbigLib.PAR_ERROR.CE_NO_ERROR and autofreeze is True:
        strp = SbigStructures.SetTemperatureRegulationParams2
        strr = None
        udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(strp), POINTER(strr)]
        strp = strp(regulation=SbigLib.TEMPERATURE_REGULATION.REGULATION_ENABLE_AUTOFREEZE)

        # Second call sets the Freezing
        ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_SET_TEMPERATURE_REGULATION2, byref(strp), None)
        if ret == SbigLib.PAR_ERROR.CE_NO_ERROR:
            return True
        else:
            return False

    else:
        raise False


# Getting Temperature
def get_temperature():
    '''
    :return: temperatura da camera
    '''
    qsp = SbigStructures.QueryTemperatureStatusParams
    qtsr = SbigStructures.QueryTemperatureStatusResults2

    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(qsp), POINTER(qtsr)]

    qsp = qsp(request=SbigLib.QUERY_TEMP_STATUS_REQUEST.TEMP_STATUS_ADVANCED2)

    qtsr = qtsr()

    ret = udrv.SBIGUnivDrvCommand(
        SbigLib.PAR_COMMAND.CC_QUERY_TEMPERATURE_STATUS, byref(qsp), byref(qtsr))

    if ret == SbigLib.PAR_ERROR.CE_NO_ERROR:
        return (qtsr.coolingEnabled,
                (qtsr.fanPower / 255.0) * 100.0,
                qtsr.ccdSetpoint,
                qtsr.imagingCCDTemperature)
    else:
        pass
        # print(ret)


# Getting the filter info
def get_filterinfo():
    cfwp = SbigStructures.CFWParams
    cfwr = SbigStructures.CFWResults

    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cfwp), POINTER(cfwr)]

    cfwp = cfwp(cfwModel=SbigLib.CFW_MODEL_SELECT.CFWSEL_CFW8,
                cfwCommand=SbigLib.CFW_COMMAND.CFWC_GET_INFO,
                cfwParam1=SbigLib.CFW_GETINFO_SELECT.CFWG_FIRMWARE_VERSION)

    cfwr = cfwr()

    ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_CFW, byref(cfwp), byref(cfwr))

    if ret == SbigLib.PAR_ERROR.CE_NO_ERROR:
        return cfwr.cfwResult1, cfwr.cfwResult2
    else:
        return None, None


# Setting the filter Position
def set_filterposition(position):
    cfwp = SbigStructures.CFWParams
    cfwr = SbigStructures.CFWResults

    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cfwp), POINTER(cfwr)]

    cfwp = cfwp(cfwModel=SbigLib.CFW_MODEL_SELECT.CFWSEL_CFW8,
                cfwCommand=SbigLib.CFW_COMMAND.CFWC_GOTO,
                cfwParam1=position, inPtr=None, inLength=0, outPtr=None)

    cfwr = cfwr()

    ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_CFW, byref(cfwp), byref(cfwr))

    if ret == SbigLib.PAR_ERROR.CE_NO_ERROR:
        return True
    else:
        return False


# Getting the filter Status
def get_filterstatus():
    cfwp = SbigStructures.CFWParams
    cfwr = SbigStructures.CFWResults
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cfwp), POINTER(cfwr)]

    cfwp = cfwp(cfwModel=SbigLib.CFW_MODEL_SELECT.CFWSEL_CFW8,
                cfwCommand=SbigLib.CFW_COMMAND.CFWC_QUERY)
    cfwr = cfwr()

    ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_CFW, byref(cfwp), byref(cfwr))

    if ret == SbigLib.PAR_ERROR.CE_NO_ERROR:
        return cfwr.cfwStatus
    else:
        return False


# Getting Filter Position
def get_filterposition():
    cfwp = SbigStructures.CFWParams
    cfwr = SbigStructures.CFWResults

    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cfwp), POINTER(cfwr)]

    cfwp = cfwp(cfwModel=SbigLib.CFW_MODEL_SELECT.CFWSEL_CFW8,
                cfwCommand=SbigLib.CFW_COMMAND.CFWC_QUERY)
    cfwr = cfwr()

    ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_CFW, byref(cfwp), byref(cfwr))

    if ret == SbigLib.PAR_ERROR.CE_NO_ERROR:
        return cfwr.cfwStatus
    else:
        return False


# Starting Fan
def start_fan():
    mcp = SbigStructures.MiscellaneousControlParams
    mcr = None
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(mcp), POINTER(mcr)]

    mcp = mcp(fanEnable=True)
    ret = udrv.SBIGUnivDrvCommand(
        SbigLib.PAR_COMMAND.CC_MISCELLANEOUS_CONTROL, byref(mcp), None)

    if ret == SbigLib.PAR_ERROR.CE_NO_ERROR:
        return True
    else:
        return False


# Stopping Fan
def stop_fan():
    mcp = SbigStructures.MiscellaneousControlParams
    mcr = None
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(mcp), POINTER(mcr)]
    mcp = mcp(fanEnable=False)

    ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_MISCELLANEOUS_CONTROL, byref(mcp), None)
    if ret == SbigLib.PAR_ERROR.CE_NO_ERROR:
        return True
    else:
        return False


# Checking if is Fanning
def is_fanning():
    qsp = SbigStructures.QueryTemperatureStatusParams
    qtsr = SbigStructures.QueryTemperatureStatusResults2

    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(qsp), POINTER(qtsr)]
    qsp = qsp(request=SbigLib.QUERY_TEMP_STATUS_REQUEST.TEMP_STATUS_ADVANCED2)
    qtsr = qtsr()

    ret = udrv.SBIGUnivDrvCommand(
        SbigLib.PAR_COMMAND.CC_QUERY_TEMPERATURE_STATUS, byref(qsp), byref(qtsr))

    if ret == SbigLib.PAR_ERROR.CE_NO_ERROR:
        return True if qtsr.fanEnabled == 1 else False
    else:
        return False


def ccdinfo():
    '''
    :return:
    '''
    for ccd in SbigLib.CCD_INFO_REQUEST.CCD_INFO_IMAGING.value, SbigLib.CCD_INFO_REQUEST.CCD_INFO_TRACKING.value:

        cin = SbigStructures.ReadOutInfo
        cout = SbigStructures.GetCCDInfoResults0
        udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
        cin = cin(request=ccd)
        cout = cout()
        udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_GET_CCD_INFO.value, byref(cin), byref(cout))

        for i_mode in range(cout.readoutModes):
            if ccd == SbigLib.CCD_INFO_REQUEST.CCD_INFO_IMAGING.value and i_mode == 0:
                readout_mode = [
                    cout.readoutInfo[i_mode].mode, cout.readoutInfo[i_mode].width, cout.readoutInfo[i_mode].height,
                    cout.readoutInfo[i_mode].width, cout.readoutInfo[i_mode].gain, cout.readoutInfo[i_mode].pixel_width,
                    cout.readoutInfo[i_mode].pixel_height]

    return cout.firmwareVersion, cout.cameraType, cout.name, readout_mode[1],  readout_mode[2]


def set_path(pre):
    '''
    :param pre:
    :return: gera nome da pasta e consequente do arquivo fit e png.
    '''
    tempo = datetime.utcnow().strftime('%Y%m%d_%H%M%S')

    data = tempo[0:4] + "_" + tempo[4:6] + tempo[6:8]

    from src.business.configuration.configSystem import ConfigSystem
    cs = ConfigSystem()
    path = str(cs.get_image_path()) + "/"

    from src.business.configuration.configProject import ConfigProject
    ci = ConfigProject()
    name_observatory = str(ci.get_site_settings())
    name_observatory = Image_Processing.get_observatory(name_observatory)

    if int(tempo[9:11]) > 12:
        path = path + name_observatory + "_" + data + "/"

    else:
        tempo = datetime.utcnow().strftime('%Y%m%d_%H%M%S')
        ano = tempo[0:4]
        mes = tempo[4:6]
        dia = tempo[6:8]
        abs_julian_day = jd_to_date(date_to_jd(ano, mes, int(dia)) - 1)

        aux_month = "%.2d" % abs_julian_day[1]

        aux_day = "%.2d" % abs_julian_day[2]

        path = path + name_observatory + "_" + str(abs_julian_day[0]) + "_" + aux_month + aux_day + "/"

    return path, tempo


def get_observatory(name):
    name_aux = str(name).split(',')[1]
    name_aux = name_aux.replace("\'", "")
    name_aux = name_aux.replace(" ", "")

    return name_aux


def photoshoot(etime, pre, binning, dark_photo, get_level1, get_level2,
               get_axis_xi, get_axis_xf, get_axis_yi, get_axis_yf, ignore_crop,
               image_tif, image_fit):
    '''
    print("\n\n")
    print(etime)
    print(pre)
    print(binning)
    print(dark_photo)
    print(get_level1)
    print(get_level2)
    print(get_axis_xi)
    print(get_axis_xf)
    print(get_axis_yi)
    print(get_axis_yf)
    print(ignore_crop)
    print("\n\n")
    :param etime: tempo de exposição
    :param pre: prefixo do nome do arquivo
    :param binning: redução da imagem
    :param dark_photo: shooter fechado = 1 ou aberto = 0
    :param get_level1: limite inferior para auto contraste
    :param get_level2: limite superior para auto contraste
    x = width
    y = height
    :param get_axis_xi:
    :param get_axis_xf:
    :param get_axis_yi:
    :param get_axis_yf:
    :param ignore_crop:
    :return:
    '''
    # open_driver()
    # open_deviceusb()
    # establishinglink()
    if 0.0 < float(get_level1) < 1.0:
        get_level1 = float(get_level1)
    else:
        get_level1 = 0.1

    if 0.0 < float(get_level2) < 1.0:
        get_level2 = float(get_level2)
    else:
        get_level2 = 0.99

    for ccd in SbigLib.CCD_INFO_REQUEST.CCD_INFO_IMAGING.value, SbigLib.CCD_INFO_REQUEST.CCD_INFO_TRACKING.value:

        cin = SbigStructures.ReadOutInfo
        cout = SbigStructures.GetCCDInfoResults0
        udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
        cin = cin(request=ccd)
        cout = cout()
        udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_GET_CCD_INFO.value, byref(cin), byref(cout))
        # print("Ret: ", ret, "\nFV: ", cout.firmwareVersion, "\nCt:",
        #       cout.cameraType, "\nname", cout.name, "\nReadoutModes: ", cout.readoutModes)

        for i_mode in range(cout.readoutModes):
            if ccd == SbigLib.CCD_INFO_REQUEST.CCD_INFO_IMAGING.value and i_mode == 0:
                readout_mode = [
                    cout.readoutInfo[i_mode].mode, cout.readoutInfo[i_mode].width, cout.readoutInfo[i_mode].height,
                    cout.readoutInfo[i_mode].width, cout.readoutInfo[i_mode].gain, cout.readoutInfo[i_mode].pixel_width,
                    cout.readoutInfo[i_mode].pixel_height]  # STORE FIRST MODE OF IMAGING CCD FOR EXPOSURE TEST

    # Setting the Gain and Bining with Width and Height
    # x = width
    # y = height
    v_read = 0
    v_h = readout_mode[2]
    v_w = readout_mode[1]
    if binning == 1:
        v_read = 1
        v_h = int(v_h / 2)
        v_w = int(v_w / 2)
    elif binning == 2:
        v_read = 2
        v_h = int(v_h / 3)
        v_w = int(v_w / 3)

    print("Binning = " + str(v_read))
    print("Height = " + str(v_h))
    print("Width = " + str(v_w))

    print("GRAB IMAGE - Start Exposure")
    cin = SbigStructures.StartExposureParams2
    cout = None
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]

    try:
        if dark_photo == 1:
            cin = cin(ccd=SbigLib.CCD_REQUEST.CCD_IMAGING.value, exposureTime=etime,
                      openShutter=SbigLib.SHUTTER_COMMAND.SC_CLOSE_SHUTTER.value, readoutMode=v_read, top=0, left=0,
                      height=v_h, width=v_w)
        else:
            cin = cin(ccd=SbigLib.CCD_REQUEST.CCD_IMAGING.value, exposureTime=etime,
                      openShutter=SbigLib.SHUTTER_COMMAND.SC_OPEN_SHUTTER.value, readoutMode=v_read, top=0, left=0,
                      height=v_h, width=v_w)
    except Exception:
        cin = cin(ccd=SbigLib.CCD_REQUEST.CCD_IMAGING.value, exposureTime=etime,
                  openShutter=SbigLib.SHUTTER_COMMAND.SC_OPEN_SHUTTER.value, readoutMode=v_read, top=0, left=0,
                  height=v_h, width=v_w)

    print("Readout Height: " + str(v_h))
    print("Readout Width: " + str(v_w))
    ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_START_EXPOSURE2.value, byref(cin), cout)
    print("Ret: ", ret)

    print("GRAB IMAGE - Query Command Status")

    t0 = time.time()
    status = 2
    while status == 2:
        cin = SbigStructures.QueryCommandStatusParams
        cout = SbigStructures.QueryCommandStatusResults
        udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
        cin = cin(command=SbigLib.PAR_COMMAND.CC_START_EXPOSURE2.value)
        cout = cout()
        udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_QUERY_COMMAND_STATUS.value, byref(cin), byref(cout))

        status = cout.status
        print("Status: %3.2f sec - %s" % (time.time() - t0, status))
        time.sleep(0.01)

    print("GRAB IMAGE - End Exposure")

    cin = SbigStructures.EndExposureParams
    cout = None
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
    cin = cin(ccd=SbigLib.CCD_REQUEST.CCD_IMAGING.value)
    udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_END_EXPOSURE.value, byref(cin), cout)

    print("GRAB IMAGE - Start Readout")

    cin = SbigStructures.StartReadoutParams
    cout = None
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]

    cin = cin(command=SbigLib.PAR_COMMAND.CC_START_EXPOSURE2.value, readoutMode=v_read, top=0, left=0,
              height=v_h, width=v_w)
    ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_START_READOUT.value, byref(cin), cout)
    print("ret: ", ret)
    print(SbigLib.PAR_COMMAND.CC_START_READOUT.value)

    print("GRAB IMAGE - Readout Lines")

    img = np.zeros((v_h, v_w))

    for i_line in range(v_h):
        cin = SbigStructures.ReadoutLineParams
        cout = c_ushort * v_w
        udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
        cin = cin(ccd=SbigLib.CCD_REQUEST.CCD_IMAGING.value, readoutMode=v_read, pixelStart=0,
                  pixelLength=v_w)
        cout = cout()
        udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_READOUT_LINE.value, byref(cin), byref(cout))
        img[i_line] = cout

    path, tempo = set_path(pre)

    # path, tempo = "/home/hiyoku/Imagens/images/", time.strftime('%Y%m%d_%H%M%S')

    if not os.path.isdir(path):
        os.makedirs(path)

    from src.business.configuration.configProject import ConfigProject
    ci = ConfigProject()
    site_id_name = str(ci.get_site_settings())

    site_id_name = Image_Processing.get_observatory(site_id_name)

    if dark_photo == 1:
        fn = pre + "-DARK" + "_" + site_id_name + "_" + tempo
        name = path + fn
        pngname = name + '.png'
        pngname_final = fn + '.png'
        tifname = name + '.tif'
        tifname_final = fn + '.tif'
        fitname = name + '.fit'
        fitname_final = fn + '.fit'
    else:
        fn = pre + "_" + site_id_name + "_" + tempo
        name = path + fn
        pngname = name + '.png'
        pngname_final = fn + '.png'
        tifname = name + '.tif'
        tifname_final = fn + '.tif'
        fitname = name + '.fit'
        fitname_final = fn + '.fit'

    try:
        os.unlink(tifname)
    except OSError:
        pass
    '''
    Create a new FITS file using the supplied data/header.
    Crop fit image
    '''
    try:
        if not ignore_crop:
            # x = width
            # y = height
            print("Cropping image.")
            print("Width: xi = " + str(get_axis_xi) + " xf = " + str(get_axis_xf))
            print("Height: yi = " + str(get_axis_yi) + " yf = " + str(get_axis_yf))
            img = img[get_axis_yi:get_axis_yf, get_axis_xi:get_axis_xf]  # cropping image
    except Exception as e:
        print("Not possible cropping image ->" + str(e))

    print("\nGRAB IMAGE - End Readout\n")

    cin = SbigStructures.EndReadoutParams
    cout = None
    udrv.SBIGUnivDrvCommand.argtypes = [c_ushort, POINTER(cin), POINTER(cout)]
    cin = cin(ccd=SbigLib.CCD_REQUEST.CCD_IMAGING.value)
    ret = udrv.SBIGUnivDrvCommand(SbigLib.PAR_COMMAND.CC_END_READOUT.value, byref(cin), cout)
    print("ret", ret)

    # cmd(SbigLib.PAR_COMMAND.CC_CLOSE_DEVICE.value, None, None)

    # cmd(SbigLib.PAR_COMMAND.CC_CLOSE_DRIVER.value, None, None)

    img_to_tif = img
    img_to_png = img
    img_to_fit = img

    try:
        if image_tif:
            print("Call set_tif")
            Image_Processing.save_tif(img_to_tif, tifname)
    except Exception as e:
        print("Image .tif ERROR -> {}".format(e))

    try:
        if image_fit:
            fits.writeto(fitname, img_to_fit)
            print("Call set_header")
            Image_Processing.set_header(fitname)
    except Exception as e:
        print("Image .fit ERROR -> {}".format(e))

    print("Call set_png")
    Image_Processing.save_png(img_to_png, pngname, get_level1, get_level2)

    data, hora = Image_Processing.get_date_hour(tempo)
    print("End of process")
    return path, pngname_final, tifname_final, fitname_final, data, hora
