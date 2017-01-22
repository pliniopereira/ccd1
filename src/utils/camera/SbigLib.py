from enum import IntEnum


class PAR_COMMAND(IntEnum):

    """
    Camera Commands. From the sbigudrv.h
    These are the commands supported by the driver. They are prefixed by CC_ to designate them as camera commands and
    avoid conflicts with other enums.
    """
    CC_NULL = 0

    # 1 - 10
    CC_START_EXPOSURE = 1
    CC_END_EXPOSURE = 2
    CC_READOUT_LINE = 3
    CC_DUMP_LINES = 4
    CC_SET_TEMPERATURE_REGULATION = 5
    CC_QUERY_TEMPERATURE_STATUS = 6
    CC_ACTIVATE_RELAY = 7
    CC_PULSE_OUT = 8
    CC_ESTABLISH_LINK = 9
    CC_GET_DRIVER_INFO = 10

    # 11 - 20
    CC_GET_CCD_INFO = 11
    CC_QUERY_COMMAND_STATUS = 12
    CC_MISCELLANEOUS_CONTROL = 13
    CC_READ_SUBTRACT_LINE = 14
    CC_UPDATE_CLOCK = 15
    CC_READ_OFFSET = 16
    CC_OPEN_DRIVER = 17
    CC_CLOSE_DRIVER = 18
    CC_TX_SERIAL_BYTES = 19
    CC_GET_SERIAL_STATUS = 20

    # 21 - 30
    CC_AO_TIP_TILT = 21
    CC_AO_SET_FOCUS = 22
    CC_AO_DELAY = 23
    CC_GET_TURBO_STATUS = 24
    CC_END_READOUT = 25
    CC_GET_US_TIMER = 26
    CC_OPEN_DEVICE = 27
    CC_CLOSE_DEVICE = 28
    CC_SET_IRQL = 29
    CC_GET_IRQL = 30

    # 31 - 40
    CC_GET_LINE = 31
    CC_GET_LINK_STATUS = 32
    CC_GET_DRIVER_HANDLE = 33
    CC_SET_DRIVER_HANDLE = 34
    CC_START_READOUT = 35
    CC_GET_ERROR_STRING = 36
    CC_SET_DRIVER_CONTROL = 37
    CC_GET_DRIVER_CONTROL = 38
    CC_USB_AD_CONTROL = 39
    CC_QUERY_USB = 40

    # 41 - 50
    CC_GET_PENTIUM_CYCLE_COUNT = 41
    CC_RW_USB_I2C = 42
    CC_CFW = 43
    CC_BIT_IO = 44
    CC_USER_EEPROM = 45
    CC_AO_CENTER = 46
    CC_BTDI_SETUP = 47
    CC_MOTOR_FOCUS = 48
    CC_QUERY_ETHERNET = 49
    CC_START_EXPOSURE2 = 50

    '''
    CC_SET_TEMPERATURE_REGULATION2 is not documented!
    '''
    CC_SET_TEMPERATURE_REGULATION2 = 51


class PAR_ERROR(IntEnum):

    """
    Return Error Codes. From the sbigudrv.h

    These are the error codes returned by the driver function.  They are prefixed with CE_ to designate them as camera
    errors.
    """

    # 0 - 10
    CE_NO_ERROR = 0
    CE_CAMERA_NOT_FOUND = 1  # CE_ERROR_BASE
    CE_EXPOSURE_IN_PROGRESS = 2
    CE_NO_EXPOSURE_IN_PROGRESS = 3
    CE_UNKNOWN_COMMAND = 4
    CE_BAD_CAMERA_COMMAND = 5
    CE_BAD_PARAMETER = 6
    CE_TX_TIMEOUT = 7
    CE_RX_TIMEOUT = 8
    CE_NAK_RECEIVED = 9
    CE_CAN_RECEIVED = 10

    # 11 - 20
    CE_UNKNOWN_RESPONSE = 11
    CE_BAD_LENGTH = 12
    CE_AD_TIMEOUT = 13
    CE_KBD_ESC = 14
    CE_CHECKSUM_ERROR = 15
    CE_EEPROM_ERROR = 16
    CE_SHUTTER_ERROR = 17
    CE_UNKNOWN_CAMERA = 18
    CE_DRIVER_NOT_FOUND = 19
    CE_DRIVER_NOT_OPEN = 20

    # 21 - 30
    CE_DRIVER_NOT_CLOSED = 21
    CE_SHARE_ERROR = 22
    CE_TCE_NOT_FOUND = 23
    CE_AO_ERROR = 24
    CE_ECP_ERROR = 25
    CE_MEMORY_ERROR = 26
    CE_DEVICE_NOT_FOUND = 27
    CE_DEVICE_NOT_OPEN = 28
    CE_DEVICE_NOT_CLOSED = 29
    CE_DEVICE_NOT_IMPLEMENTED = 30

    # 31 - 40
    CE_DEVICE_DISABLED = 31
    CE_OS_ERROR = 32
    CE_SOCK_ERROR = 33
    CE_SERVER_NOT_FOUND = 34
    CE_CFW_ERROR = 35
    CE_MF_ERROR = 36
    CE_FIRMWARE_ERROR = 37
    CE_DIFF_GUIDER_ERROR = 38
    CE_RIPPLE_CORRECTION_ERROR = 39
    CE_EZUSB_RESET = 40
    CE_NEXT_ERROR0 = 41


class PAR_COMMAND_STATUS(IntEnum):

    """
    Command State Codes. From the sbigudrv.h

    These are the return status codes for the Query Command Status command.  They are prefixed with CS_ to designate
    them as camera status.
    """

    CS_IDLE = 0
    CS_IN_PROGRESS = 1
    CS_INTEGRATING = 2
    CS_INTEGRATION_COMPLETE = 3


CS_PULSE_IN_ACTIVE = 0x8000
CS_WAITING_FOR_TRIGGER = 0x8000

"""
Miscellaneous constants. From sbigudrv.h

QUERY_TEMP_STATUS_REQUEST - Used with the Query Temperature Status command.
ABG_STATE7 - Passed to Start Exposure Command
MY_LOGICAL - General purpose type
DRIVER_REQUEST - Used with Get Driver Info command
CCD_REQUEST - Used with Imaging commands to specify CCD
CCD_INFO_REQUEST - Used with Get CCD Info Command
PORT - Used with Establish Link Command
CAMERA_TYPE - Returned by Establish Link and Get CCD Info commands
SHUTTER_COMMAND =  SHUTTER_STATE7 - Used with Start Exposure and Miscellaneous Control Commands
TEMPERATURE_REGULATION - Used with Enable Temperature Regulation
LED_STATE - Used with the Miscellaneous Control Command
FILTER_COMMAND =  FILTER_STATE - Used with the Miscellaneous Control Command
AD_SIZE =  FILTER_TYPE - Used with the GetCCDInfo3 Command
AO_FOCUS_COMMAND - Used with the AO Set Focus Command
SBIG_DEVICE_TYPE - Used with Open Device Command
DRIVER_CONTROL_PARAM - Used with Get/SetDriverControl Command
USB_AD_CONTROL_COMMAND - Used with UsbADControl Command
CFW_MODEL_SELECT =  CFW_STATUS =  CFW_ERROR - Used with CFW command
CFW_POSITION =  CFW_GET_INFO_SELECT - Used with CFW Command
BIT_IO_OPERATION =  BIT_IO_NMAE - Used with BitIO command
MF_MODEL_SELECT =  MF_STATUS =  MF_ERROR =  MF_GET_INFO_SELECT - Used with Motor Focus Command
DIFF_GUIDER_COMMAND =  DIFF_GUIDER_STATE =  DIFF_GUIDER_ERROR -     Used with the Diff Guider Command
"""


class QUERY_TEMP_STATUS_REQUEST(IntEnum):
    TEMP_STATUS_STANDARD = 0
    TEMP_STATUS_ADVANCED = 1
    TEMP_STATUS_ADVANCED2 = 2


class ABG_STATE7(IntEnum):
    ABG_LOW7 = 0
    ABG_CLK_LOW7 = 1
    ABG_CLK_MED7 = 2
    ABG_CLK_HI7 = 3


class DRIVER_REQUEST(IntEnum):
    DRIVER_STD = 0
    DRIVER_EXTEND = 1
    DRIVER_USB_LOADER = 2


class CCD_REQUEST(IntEnum):
    CCD_IMAGING = 0
    CCD_TRACKING = 1
    CCD_EXT_TRACKING = 2


class READOUT_BINNING_MODE(IntEnum):
    RM_1X1 = 0
    RM_2X2 = 1
    RM_3X3 = 2
    RM_NX1 = 3
    RM_NX2 = 4
    RM_NX3 = 5
    RM_1X1_VOFFCHIP = 6
    RM_2X2_VOFFCHIP = 7
    RM_3X3_VOFFCHIP = 8
    RM_9X9 = 9
    RM_NXN = 10


class CCD_INFO_REQUEST(IntEnum):
    CCD_INFO_IMAGING = 0
    CCD_INFO_TRACKING = 1
    CCD_INFO_EXTENDED = 2
    CCD_INFO_EXTENDED_5C = 3
    CCD_INFO_EXTENDED2_IMAGING = 4
    CCD_INFO_EXTENDED2_TRACKING = 5
    CCD_INFO_EXTENDED3 = 6


class IMAGING_ABG(IntEnum):
    ABG_NOT_PRESENT = 1
    ABG_PRESENT = 2


class PORT_RATE(IntEnum):
    BR_AUTO = 0
    BR_9600 = 1
    BR_19K = 2
    BR_38K = 3
    BR_57K = 4
    BR_115K = 5


class CAMERA_TYPE(IntEnum):
    ST7_CAMERA = 4
    ST8_CAMERA = 5
    ST5C_CAMERA = 6
    TCE_CONTROLLER = 7
    ST237_CAMERA = 8
    STK_CAMERA = 9
    ST9_CAMERA = 10
    STV_CAMERA = 11
    ST10_CAMERA = 12
    ST1K_CAMERA = 13
    ST2K_CAMERA = 14
    STL_CAMERA = 15
    ST402_CAMERA = 16
    STX_CAMERA = 17
    ST4K_CAMERA = 18
    STT_CAMERA = 19
    STI_CAMERA = 20
    STF_CAMERA = 21
    NEXT_CAMERA = 22
    NO_CAMERA = 0xFFFF


class SHUTTER_COMMAND(IntEnum):
    SC_LEAVE_SHUTTER = 0
    SC_OPEN_SHUTTER = 1
    SC_CLOSE_SHUTTER = 2
    SC_INITIALIZE_SHUTTER = 3
    SC_OPEN_EXT_SHUTTER = 4
    SC_CLOSE_EXT_SHUTTER = 5


class SHUTTER_STATE7(IntEnum):
    SS_OPEN = 0
    SS_CLOSED = 1
    SS_OPENING = 2
    SS_CLOSING = 3


class TEMPERATURE_REGULATION(IntEnum):
    REGULATION_OFF = 0
    REGULATION_ON = 1
    REGULATION_OVERRIDE = 2
    REGULATION_FREEZE = 3
    REGULATION_UNFREEZE = 4
    REGULATION_ENABLE_AUTOFREEZE = 5
    REGULATION_DISABLE_AUTOFREEZE = 6


REGULATION_FROZEN_MASK = 0x8000


class LED_STATE(IntEnum):
    LED_OFF = 0
    LED_ON = 1
    LED_BLINK_LOW = 2
    LED_BLINK_HIGH = 3


class FILTER_COMMAND(IntEnum):
    FILTER_LEAVE = 0
    FILTER_SET_1 = 1
    FILTER_SET_2 = 2
    FILTER_SET_3 = 3
    FILTER_SET_4 = 4
    FILTER_SET_5 = 5
    FILTER_STOP = 6
    FILTER_INIT = 7


class FILTER_STATE(IntEnum):
    FS_MOVING = 0
    FS_AT_1 = 1
    FS_AT_2 = 2
    FS_AT_3 = 3
    FS_AT_4 = 4
    FS_AT_5 = 5
    FS_UNKNOWN = 6


class AD_SIZE(IntEnum):
    AD_UNKNOWN = 0
    AD_12_BITS = 1
    AD_16_BITS = 2


class FILTER_TYPE(IntEnum):
    FW_UNKNOWN = 0
    FW_EXTERNAL = 1
    FW_VANE = 2
    FW_FILTER_WHEEL = 3


class AO_FOCUS_COMMAND(IntEnum):
    AOF_HARD_CENTER = 0
    AOF_SOFT_CENTER = 1
    AOF_STEP_IN = 2
    AOF_STEP_OUT = 3

# Ethernet stuff
SRV_SERVICE_PORT = 5000
BROADCAST_PORT = 5001


class SBIG_DEVICE_TYPE(IntEnum):
    DEV_NONE = 0
    DEV_LPT1 = 1
    DEV_LPT2 = 2
    DEV_LPT3 = 3
    DEV_USB = 0x7F00
    DEV_ETH = 0x7F01
    DEV_USB1 = 0x7F02
    DEV_USB2 = 0x7F03
    DEV_USB3 = 0x7F04
    DEV_USB4 = 0x7F05
    DEV_USB5 = 0x7F06
    DEV_USB6 = 0x7F07
    DEV_USB7 = 0x7F08
    DEV_USB8 = 0x7F09


class DRIVER_CONTROL_PARAM(IntEnum):
    DCP_USB_FIFO_ENABLE = 0
    DCP_CALL_JOURNAL_ENABLE = 1
    DCP_IVTOH_RATIO = 2
    DCP_USB_FIFO_SIZE = 3
    DCP_USB_DRIVER = 4
    DCP_KAI_RELGAIN = 5
    DCP_USB_PIXEL_DL_ENABLE = 6
    DCP_HIGH_THROUGHPUT = 7
    DCP_VDD_OPTIMIZED = 8
    DCP_AUTO_AD_GAIN = 9
    DCP_NO_HCLKS_FOR_INTEGRATION = 10
    DCP_TDI_MODE_ENABLE = 11
    DCP_VERT_FLUSH_CONTROL_ENABLE = 12
    DCP_ETHERNET_PIPELINE_ENABLE = 13
    DCP_FAST_LINK = 14
    DCP_OVERSCAN_ROWSCOLS = 15
    DCP_PIXEL_PIPELINE_ENABLE = 16
    DCP_COLUMN_REPAIR_ENABLE = 17
    DCP_WARM_PIXEL_REPAIR_ENABLE = 18
    DCP_WARM_PIXEL_REPAIR_COUNT = 19
    DCP_LAST = 20


class USB_AD_CONTROL_COMMAND(IntEnum):
    USB_AD_IMAGING_GAIN = 0
    USB_AD_IMAGING_OFFSET = 1

    USB_AD_TRACKING_GAIN = 2
    USB_AD_TRACKING_OFFSET = 3

    USB_AD_EXTTRACKING_GAIN = 4
    USB_AD_EXTTRACKING_OFFSET = 5

    USB_AD_IMAGING2_GAIN = 6
    USB_AD_IMAGING2_OFFSET = 7

    USB_AD_IMAGING_GAIN_RIGHT = 8
    USB_AD_IMAGING_OFFSET_RIGHT = 9


class ENUM_USB_DRIVER(IntEnum):
    USBD_SBIGE = 0
    USBD_SBIGI = 1
    USBD_SBIGM = 2
    USBD_NEXT = 3


class CFW_MODEL_SELECT(IntEnum):
    CFWSEL_UNKNOWN = 0
    CFWSEL_CFW2 = 1
    CFWSEL_CFW5 = 2
    CFWSEL_CFW8 = 3
    CFWSEL_CFWL = 4
    CFWSEL_CFW402 = 5
    CFWSEL_AUTO = 6
    CFWSEL_CFW6A = 7
    CFWSEL_CFW10 = 8
    CFWSEL_CFW10_SERIAL = 9
    CFWSEL_CFW9 = 10
    CFWSEL_CFWL8 = 11
    CFWSEL_CFWL8G = 12
    CFWSEL_CFW1603 = 13
    CFWSEL_FW5_STX = 14
    CFWSEL_FW5_8300 = 15
    CFWSEL_FW8_8300 = 16
    CFWSEL_FW7_STX = 17
    CFWSEL_FW8_STT = 18


class CFW_COMMAND(IntEnum):
    CFWC_QUERY = 0
    CFWC_GOTO = 1
    CFWC_INIT = 2
    CFWC_GET_INFO = 3
    CFWC_OPEN_DEVICE = 4
    CFWC_CLOSE_DEVICE = 5


class CFW_STATUS(IntEnum):
    CFWS_UNKNOWN = 0
    CFWS_IDLE = 1
    CFWS_BUSY = 2


class CFW_ERROR(IntEnum):
    CFWE_NONE = 0
    CFWE_BUSY = 1
    CFWE_BAD_COMMAND = 2
    CFWE_CAL_ERROR = 3
    CFWE_MOTOR_TIMEOUT = 4
    CFWE_BAD_MODEL = 5
    CFWE_DEVICE_NOT_CLOSED = 6
    CFWE_DEVICE_NOT_OPEN = 7
    CFWE_I2C_ERROR = 8


class CFW_POSITION(IntEnum):
    CFWP_UNKNOWN = 0
    CFWP_1 = 1
    CFWP_2 = 2
    CFWP_3 = 3
    CFWP_4 = 4
    CFWP_5 = 5
    CFWP_6 = 6
    CFWP_7 = 7
    CFWP_8 = 8
    CFWP_9 = 9
    CFWP_10 = 10


class CFW_COM_PORT(IntEnum):
    CFWPORT_COM1 = 1
    CFWPORT_COM2 = 2
    CFWPORT_COM3 = 3
    CFWPORT_COM4 = 4


class CFW_GETINFO_SELECT(IntEnum):
    CFWG_FIRMWARE_VERSION = 0
    CFWG_CAL_DATA = 1
    CFWG_DATA_REGISTERS = 2


class BITIO_OPERATION(IntEnum):
    BITIO_WRITE = 0
    BITIO_READ = 1


class BITIO_NAME(IntEnum):
    BITI_PS_LOW = 0
    BITO_IO1 = 1
    BITO_IO2 = 2
    BITI_IO3 = 3
    BITO_FPGA_WE = 4


class BTDI_ERROR(IntEnum):
    BTDI_SCHEDULE_ERROR = 1
    BTDI_OVERRUN_ERROR = 2


class MF_MODEL_SELECT(IntEnum):
    MFSEL_UNKNOWN = 0
    MFSEL_AUTO = 1
    MFSEL_STF = 2


class MF_COMMAND(IntEnum):
    MFC_QUERY = 0
    MFC_GOTO = 1
    MFC_INIT = 2
    MFC_GET_INFO = 3
    MFC_ABORT = 4


class MF_STATUS(IntEnum):
    MFS_UNKNOWN = 0
    MFS_IDLE = 1
    MFS_BUSY = 2


class MF_ERROR(IntEnum):
    MFE_NONE = 0
    MFE_BUSY = 1
    MFE_BAD_COMMAND = 2
    MFE_CAL_ERROR = 3
    MFE_MOTOR_TIMEOUT = 4
    MFE_BAD_MODEL = 5
    MFE_I2C_ERROR = 6
    MFE_NOT_FOUND = 7


class MF_GETINFO_SELECT(IntEnum):
    MFG_FIRMWARE_VERSION = 0
    MFG_DATA_REGISTERS = 1


class DIFF_GUIDER_COMMAND(IntEnum):
    DGC_DETECT = 0
    DGC_GET_BRIGHTNESS = 1
    DGC_SET_BRIGHTNESS = 2


class DIFF_GUIDER_ERROR(IntEnum):
    DGE_NO_ERROR = 0
    DGE_NOT_FOUND = 1
    DGE_BAD_COMMAND = 2
    DGE_BAD_PARAMETER = 3


class DIFF_GUIDER_STATUS(IntEnum):
    DGS_UNKNOWN = 0
    DGS_IDLE = 1
    DGS_BUSY = 2


class FAN_STATE(IntEnum):
    FS_OFF = 0
    FS_ON = 1
    FS_AUTOCONTROL = 2


class BULK_IO_COMMAND(IntEnum):
    BIO_READ = 0
    BIO_WRITE = 1
    BIO_FLUSH = 2


class PIXEL_CHANNEL_MODE(IntEnum):
    PIXEL_CHANNEL_MODE_A = 0
    PIXEL_CHANNEL_MODE_B = 1
    PIXEL_CHANNEL_MODE_AB = 2


class ACTIVE_PIXEL_CHANNEL(IntEnum):
    PIXEL_CHANNEL_A = 0
    PIXEL_CHANNEL_B = 1

# General Purpose Flags

END_SKIP_DELAY = 0x8000  # set in ccd parameter of EndExposure
# command to skip synchronization
# delay - Use this to increase the
# rep rate when taking darks to later
# be subtracted from SC_LEAVE_SHUTTER
# exposures such as when tracking and
# imaging

#
START_SKIP_VDD = 0x8000
#        set in ccd parameter of StartExposure
# command to skip lowering Imaging CCD
# Vdd during integration. - Use this to
# increase the rep rate when you don't
# care about glow in the upper-left
# corner of the imaging CCD
#

START_MOTOR_ALWAYS_ON = 0x4000
#
#        set in ccd parameter of StartExposure
# and EndExposure commands to force shutter
# motor to stay on all the time which reduces
# delays in Start and End Exposure timing and
# yields higher image throughput.  Don't
# do this too often or camera head will
# heat up
#
#
ABORT_DONT_END = 0x2000
#
#        set in ccd parameter of EndExposure
# command to abort the exposure completely
# instead of just ending the integration phase
# for cameras with internal frame buffers
# like the STX

# set in exposureTime to wait for trigger in pulse
EXP_WAIT_FOR_TRIGGER_IN = 0x80000000
EXP_SEND_TRIGGER_OUT = 0x40000000  # set in exposureTime to send trigger out Y-
EXP_LIGHT_CLEAR = 0x20000000  # set to do light clear of the CCD
EXP_MS_EXPOSURE = 0x10000000  # set to interpret exposure time as milliseconds
# activate the fast readout mode of the STF-8300, etc.
EXP_FAST_READOUT = 0x08000000
# activate the dual channel CCD readout mode of the STF-8050
EXP_DUAL_CHANNEL_MODE = 0x04000000
EXP_TIME_MASK = 0x00FFFFFF  # mask with exposure time to remove flags

# Capabilities Bits - Bit Field Definitions for the capabilitiesBits in
# the GetCCDInfoResults4 struct.


CB_CCD_TYPE_MASK = 0x0001  # mask for CCD type
CB_CCD_TYPE_FULL_FRAME = 0x0000  # b0=0 is full frame CCD
CB_CCD_TYPE_FRAME_TRANSFER = 0x0001  # b0=1 is frame transfer CCD
CB_CCD_ESHUTTER_MASK = 0x0002  # mask for electronic shutter type
CB_CCD_ESHUTTER_NO = 0x0000  # b1=0 indicates no electronic shutter
CB_CCD_ESHUTTER_YES = 0x0002  # b1=1 indicates electronic shutter
CB_CCD_EXT_TRACKER_MASK = 0x0004  # mask for external tracker support
CB_CCD_EXT_TRACKER_NO = 0x0000  # b2=0 indicates no external tracker support
CB_CCD_EXT_TRACKER_YES = 0x0004  # b2=1 indicates external tracker support
CB_CCD_BTDI_MASK = 0x0008  # mask for BTDI support
CB_CCD_BTDI_NO = 0x0000  # b3=0 indicates no BTDI support
CB_CCD_BTDI_YES = 0x0008  # b3=1 indicates BTDI support
CB_AO8_MASK = 0x0010  # mask for AO-8 detected
CB_AO8_NO = 0x0000  # b4=0 indicates no AO-8 detected
CB_AO8_YES = 0x0010  # b4=1 indicates AO-8 detected
CB_FRAME_BUFFER_MASK = 0x0020  # mask for camera with frame buffer
CB_FRAME_BUFFER_NO = 0x0000  # b5=0 indicates camera without Frame Buffer
CB_FRAME_BUFFER_YES = 0x0020  # b5=1 indicates camera with Frame Buffer
# mask for camera that requires StartExposure2
CB_REQUIRES_STARTEXP2_MASK = 0x0040
# b6=0 indicates camera works with StartExposure
CB_REQUIRES_STARTEXP2_NO = 0x0000
# b6=1 indicates camera Requires StartExposure2
CB_REQUIRES_STARTEXP2_YES = 0x0040

# Defines

MIN_ST7_EXPOSURE = 12  # Minimum exposure in 1/100ths second
MIN_ST402_EXPOSURE = 4  # Minimum exposure in 1/100ths second
MIN_ST3200_EXPOSURE = 9  # Minimum exposure in 1/100ths second

MIN_STF8300_EXPOSURE = 9  # Minimum exposure in 1/100ths second
# Minimum exposure in 1/1000ths second since has E Shutter
MIN_STF8050_EXPOSURE = 1
# Minimum exposure in 1/1000ths second since has E Shutter
MIN_STF4070_EXPOSURE = 1

MIN_STX_EXPOSURE = 18  # Minimum exposure in 1/100ths second
MIN_STT_EXPOSURE = 12  # Minimum exposure in 1/100ths second
# Minimum exposure in 1/1000ths second since ST-i has E Shutter
MIN_STU_EXPOSURE = 1
