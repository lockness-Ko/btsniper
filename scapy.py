from scapy import *

bt = BluetoothHCISocket(0)

bt.sr(
  HCI_Hdr()/
  HCI_Command_Hdr()/
  HCI_Cmd_LE_Set_Scan_Parameters(type=1))

bt.sr(
  HCI_Hdr()/
  HCI_Command_Hdr()/
  HCI_Cmd_LE_Set_Scan_Enable(
    enable=True,
    filter_dups=False))

adverts = bt.sniff(lfilter=lambda p: HCI_LE_Meta_Advertising_Reports in p)

bt.sr(
  HCI_Hdr()/
  HCI_Command_Hdr()/
  HCI_Cmd_LE_Set_Scan_Enable(
    enable=False))

