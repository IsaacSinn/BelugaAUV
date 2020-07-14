import can

def send_one(val):


    # Using specific buses works similar:
    bus = can.interface.Bus(bustype='socketcan', channel='can0', bitrate=250000)
    # bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
    # bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
    # bus = can.interface.Bus(bustype='vector', app_name='CANalyzer', channel=0, ˓→bitrate=250000)

    msg = can.Message(arbitration_id=0x0FF, data = [32, val>>8 & 0xff, val & 0xff], is_extended_id=False)

    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message NOT sent")
