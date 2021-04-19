# ByteLocations in ROM
bl_starting_location = 0x168080
bl_text_firstplay = 0x16C0DC

# Lowercase letters
ll_a = (0x41)
ll_b = (0x42)
ll_c = (0x43)
ll_d = (0x44)
ll_e = (0x45)
ll_f = (0x46)
ll_g = (0x47)
ll_h = (0x48)
ll_i = (0x49)
ll_j = (0x4A)
ll_k = (0x4B)
ll_l = (0x4C)
ll_m = (0x4D)
ll_n = (0x4E)
ll_o = (0x4F)
ll_p = (0x50)
ll_q = (0x51)
ll_r = (0x52)
ll_s = (0x53)
ll_t = (0x54)
ll_u = (0x55)
ll_v = (0x56)
ll_w = (0x57)
ll_x = (0x58)
ll_y = (0x59)
ll_z = (0x5A)

# Capital letters
cl_a = (0x21)
cl_b = (0x22)
cl_c = (0x23)
cl_d = (0x24)
cl_e = (0x25)
cl_f = (0x26)
cl_g = (0x27)
cl_h = (0x28)
cl_i = (0x29)
cl_j = (0x2A)
cl_k = (0x2B)
cl_l = (0x2C)
cl_m = (0x2D)
cl_n = (0x2E)
cl_o = (0x2F)
cl_p = (0x30)
cl_q = (0x31)
cl_r = (0x32)
cl_s = (0x33)
cl_t = (0x34)
cl_u = (0x35)
cl_v = (0x36)
cl_w = (0x37)
cl_x = (0x38)
cl_y = (0x39)
cl_z = (0x3A)
cl_space = (0xF7)

# ByteValues to write into ROM
byte_text_randomizer_1 = (0x32414E44).to_bytes(4,'big') # Rand
byte_text_randomizer_2 = (0x4F4D495A).to_bytes(4,'big') # omiz
byte_text_randomizer_3 = (0x4544FD00).to_bytes(4,'big') # ed

byte_locations = {
    "kmr_00":{"bytes":(0x24020000).to_bytes(4,"big"),
              "nickname":"Goomba Region: Forest Clearing"},
    "kmr_02":{"bytes":(0x24020001).to_bytes(4,"big"),
              "nickname":"Goomba Region: Goomba Village"},
    "kmr_04":{"bytes":(0x24020002).to_bytes(4,"big"),
              "nickname":"Goomba Region: Jr. Troopa's Playground"},
    "kmr_03":{"bytes":(0x24020003).to_bytes(4,"big"),
              "nickname":"Goomba Region: Bottom of the Cliff"},
    "kmr_05":{"bytes":(0x24020004).to_bytes(4,"big"),
              "nickname":"Goomba Region: Behind the Village"},
    "kmr_06":{"bytes":(0x24020005).to_bytes(4,"big"),
              "nickname":"Goomba Region: Goomba Road 2"},
    "kmr_07":{"bytes":(0x24020006).to_bytes(4,"big"),
              "nickname":"Goomba Region: Goomba Road 3"},
    "kmr_09":{"bytes":(0x24020007).to_bytes(4,"big"),
              "nickname":"Goomba Region: Goomba Road 1"},
    "kmr_10":{"bytes":(0x24020008).to_bytes(4,"big"),
              "nickname":"Goomba Region: Toad Town Entrance"},
    "kmr_11":{"bytes":(0x24020009).to_bytes(4,"big"),
              "nickname":"Goomba Region: Goomba King's Castle"},
    "kmr_12":{"bytes":(0x2402000A).to_bytes(4,"big"),
              "nickname":"Goomba Region: Goomba Road 4"},
    "kmr_20":{"bytes":(0x2402000B).to_bytes(4,"big"),
              "nickname":"Goomba Region: Mario's House"},
    "kmr_21":{"bytes":(0x2402000C).to_bytes(4,"big"),
              "nickname":"Goomba Region: Title Screen"},
    "kmr_22":{"bytes":(0x2402000D).to_bytes(4,"big"),
              "nickname":"Goomba Region: Chapter Start"},
    "kmr_23":{"bytes":(0x2402000E).to_bytes(4,"big"),
              "nickname":"Goomba Region: Chapter End"},
    "kmr_24":{"bytes":(0x2402000F).to_bytes(4,"big"),
              "nickname":"Goomba Region: Save and Continue"},
    "kmr_30":{"bytes":(0x24020010).to_bytes(4,"big"),
              "nickname":"Goomba Region: Mario's House (Ending)"},
#    "crash001":{"bytes":(0x24020011).to_bytes(4,"big"),
#              "nickname":"Crash"},
#    "crash002":{"bytes":(0x24020012).to_bytes(4,"big"),
#              "nickname":"Crash"},
#    "crash003":{"bytes":(0x24020013).to_bytes(4,"big"),
#              "nickname":"Blackscreen?"},
    "iwa_00":{"bytes":(0x24020014).to_bytes(4,"big"),
              "nickname":"Mt Rugged: Mt Rugged 1"},
#    "crash004":{"bytes":(0x24020015).to_bytes(4,"big"),
#              "nickname":"Crash"},
#    "crash005":{"bytes":(0x24020016).to_bytes(4,"big"),
#              "nickname":"Crash"},
    "iwa_11":{"bytes":(0x24020017).to_bytes(4,"big"),
              "nickname":"Mt Rugged: Train Ride Scene"}, # going east?
    "dro_01":{"bytes":(0x24020018).to_bytes(4,"big"),
              "nickname":"Dry Dry Outpost: Outpost 1"},
    "dro_02":{"bytes":(0x24020019).to_bytes(4,"big"),
              "nickname":"Dry Dry Outpost: Outpost 2"},
    "sbk_00":{"bytes":(0x2402001A).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N3W3"}, # Mario runs in from non-existing entrance?
    "sbk_01":{"bytes":(0x2402001B).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N3W2"},
    "sbk_02":{"bytes":(0x2402001C).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N3W1 Ruins Entrance"},
    "sbk_03":{"bytes":(0x2402001D).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N3"},
    "sbk_04":{"bytes":(0x2402001E).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N3E1"},
    "sbk_05":{"bytes":(0x2402001F).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N3E2 Pokey Army"},
    "sbk_06":{"bytes":(0x24020020).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N3E3"},
    "sbk_10":{"bytes":(0x24020021).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N2W3"}, # Mario runs in from non-existing entrance?
    "sbk_11":{"bytes":(0x24020022).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N2W2"},
    "sbk_12":{"bytes":(0x24020023).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N2W1"},
    "sbk_13":{"bytes":(0x24020024).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N2"},
#    "crash006":{"bytes":(0x24020025).to_bytes(4,"big"),
#              "nickname":"Crash"}, # sbk_14? Tweester
    "sbk_15":{"bytes":(0x24020026).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N2E2"},
    "sbk_16":{"bytes":(0x24020027).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N2E3"},
    "sbk_20":{"bytes":(0x24020028).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N1W3 Special Block"}, # Mario runs in from non-existing entrance?
    "sbk_21":{"bytes":(0x24020029).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N1W2"},
    "sbk_22":{"bytes":(0x2402002A).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N1W1"},
#    "crash007":{"bytes":(0x2402002B).to_bytes(4,"big"),
#              "nickname":"Crash"}, # sbk_23? Tweester
    "sbk_24":{"bytes":(0x2402002C).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N1E1 Palm Trio"},
    "sbk_25":{"bytes":(0x2402002D).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N1E2"},
    "sbk_26":{"bytes":(0x2402002E).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: N1E3"},
    "sbk_30":{"bytes":(0x2402002F).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: W3 Kolorado's Camp"},
    "sbk_31":{"bytes":(0x24020030).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: W2"},
    "sbk_32":{"bytes":(0x24020031).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: W1"},
#    "crash008":{"bytes":(0x24020032).to_bytes(4,"big"),
#              "nickname":"Crash"}, # sbk_33? Tweester
    "sbk_34":{"bytes":(0x24020033).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: E1 Nomadimouse"},
    "sbk_35":{"bytes":(0x24020034).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: E2"},
    "sbk_36":{"bytes":(0x24020035).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: E3 Outside Outpost"},
    "sbk_40":{"bytes":(0x24020036).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S1W3"},
#    "crash009":{"bytes":(0x24020037).to_bytes(4,"big"),
#              "nickname":"Crash"}, # sbk_41? Tweester
    "sbk_42":{"bytes":(0x24020038).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S1W1"},
    "sbk_43":{"bytes":(0x24020039).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S1"},
    "sbk_44":{"bytes":(0x2402003A).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S1E1"},
    "sbk_45":{"bytes":(0x2402003B).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S1E2 Small Bluffs"},
    "sbk_46":{"bytes":(0x2402003C).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S1E3 North of Oasis"},
    "sbk_50":{"bytes":(0x2402003D).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S2W3"},
    "sbk_51":{"bytes":(0x2402003E).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S2W2"},
    "sbk_52":{"bytes":(0x2402003F).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S2W1"},
    "sbk_53":{"bytes":(0x24020040).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S2"},
#    "crash010":{"bytes":(0x24020041).to_bytes(4,"big"),
#              "nickname":"Crash"}, # sbk_54? Tweester
    "sbk_55":{"bytes":(0x24020042).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S2E2 West of Oasis"},
    "sbk_56":{"bytes":(0x24020043).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S2E3 Oasis"},
    "sbk_60":{"bytes":(0x24020044).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S3W3"},
    "sbk_61":{"bytes":(0x24020045).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S3W2 Hidden AttackFX"},
    "sbk_62":{"bytes":(0x24020046).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S3W1"},
    "sbk_63":{"bytes":(0x24020047).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S3"},
    "sbk_64":{"bytes":(0x24020048).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S3E1"},
    "sbk_65":{"bytes":(0x24020049).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S3E2"},
    "sbk_66":{"bytes":(0x2402004A).to_bytes(4,"big"),
              "nickname":"Dry Dry Desert: S3E3 South of Oasis"}, # displaced camera on load?
    "iwa_03":{"bytes":(0x2402004B).to_bytes(4,"big"),
              "nickname":"Mt Rugged: Mt Rugged 4"}, # spawn under ground on load
    "isk_01":{"bytes":(0x2402004C).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Entrance"},
    "isk_02":{"bytes":(0x2402004D).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Sarcophagus Hall 1"},
    "isk_03":{"bytes":(0x2402004E).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Sand Drainage Room 1"}, # button crashes if no partner?
    "isk_04":{"bytes":(0x2402004F).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Descending Stairs 1"},
    "isk_05":{"bytes":(0x24020050).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Pyramid Stone Room"},
    "isk_06":{"bytes":(0x24020051).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Sand Drainage Room 2"},
    "isk_07":{"bytes":(0x24020052).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Sarcophagus Hall 2"},
    "isk_08":{"bytes":(0x24020053).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Descending Stairs 2"},
    "isk_09":{"bytes":(0x24020054).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Super Hammer Room"},
    "isk_10":{"bytes":(0x24020055).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Vertical Shaft"},
    "isk_11":{"bytes":(0x24020056).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Stone Puzzle Room"},
    "isk_12":{"bytes":(0x24020057).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Sand Drainage Room 3"},
    "isk_13":{"bytes":(0x24020058).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Lunar Stone Room"},
    "isk_14":{"bytes":(0x24020059).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Diamond Stone Room"},
    "isk_16":{"bytes":(0x2402005A).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Tutankoopa Room"},
    "isk_18":{"bytes":(0x2402005B).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Deep Tunnel"},
    "isk_19":{"bytes":(0x2402005C).to_bytes(4,"big"),
              "nickname":"Dry Dry Ruins: Boss Antechamber"},
    "trd_00":{"bytes":(0x2402005D).to_bytes(4,"big"),
              "nickname":"Koopa Bros Fortress: Fortress Exterior"}, # displaced camera on load?
    "trd_01":{"bytes":(0x2402005E).to_bytes(4,"big"),
              "nickname":"Koopa Bros Fortress: Left Tower"},
    "trd_02":{"bytes":(0x2402005F).to_bytes(4,"big"),
              "nickname":"Koopa Bros Fortress: Left Stairway"},
    "trd_03":{"bytes":(0x24020060).to_bytes(4,"big"),
              "nickname":"Koopa Bros Fortress: Central Hall"},
    "trd_04":{"bytes":(0x24020061).to_bytes(4,"big"),
              "nickname":"Koopa Bros Fortress: Right Starway"},
    "trd_05":{"bytes":(0x24020062).to_bytes(4,"big"),
              "nickname":"Koopa Bros Fortress: Right Tower"}, # crashes on load if without partners
    "trd_06":{"bytes":(0x24020063).to_bytes(4,"big"),
              "nickname":"Koopa Bros Fortress: Jail"}, # softlocks if without partners
    "trd_07":{"bytes":(0x24020064).to_bytes(4,"big"),
              "nickname":"Koopa Bros Fortress: Dungeon Trap"}, # enters from the right on load
#    "crash011":{"bytes":(0x24020065).to_bytes(4,"big"),
#              "nickname":"Blackscreen"}, # trd_08?
    "trd_09":{"bytes":(0x24020066).to_bytes(4,"big"),
              "nickname":"Koopa Bros Fortress: Battlement"},
    "trd_10":{"bytes":(0x24020067).to_bytes(4,"big"),
              "nickname":"Koopa Bros Fortress: Boss Battle Room"},
    "nok_01":{"bytes":(0x24020068).to_bytes(4,"big"),
              "nickname":"Koopa Region: Koopa Village 1"},
    "nok_02":{"bytes":(0x24020069).to_bytes(4,"big"),
              "nickname":"Koopa Region: Koopa Village 2"},
    "nok_03":{"bytes":(0x2402006A).to_bytes(4,"big"),
              "nickname":"Koopa Region: Behind Koopa Village"},
    "nok_04":{"bytes":(0x2402006B).to_bytes(4,"big"),
              "nickname":"Koopa Region: Fuzzy Forest"},
    "nok_11":{"bytes":(0x2402006C).to_bytes(4,"big"),
              "nickname":"Koopa Region: Pleasant Path Entry"},
    "nok_12":{"bytes":(0x2402006D).to_bytes(4,"big"),
              "nickname":"Koopa Region: Pleasant Path Bridge"},
    "nok_13":{"bytes":(0x2402006E).to_bytes(4,"big"),
              "nickname":"Koopa Region: Pleasant Crossroads"},
    "nok_14":{"bytes":(0x2402006F).to_bytes(4,"big"),
              "nickname":"Koopa Region: Path to Fortress 1"},
    "nok_15":{"bytes":(0x24020070).to_bytes(4,"big"),
              "nickname":"Koopa Region: Path to Fortress 2"},
    "hos_00":{"bytes":(0x24020071).to_bytes(4,"big"),
              "nickname":"Shooting Star Summit: Shooting Star Path"},
    "hos_01":{"bytes":(0x24020072).to_bytes(4,"big"),
              "nickname":"Shooting Star Summit: Shooting Star Summit"},
    "hos_02":{"bytes":(0x24020073).to_bytes(4,"big"),
              "nickname":"Shooting Star Summit: Star Way"}, # crashes quickly if without partners
    "hos_03":{"bytes":(0x24020074).to_bytes(4,"big"),
              "nickname":"Shooting Star Summit: Star Haven"}, # weird spawnlocation?
    "hos_04":{"bytes":(0x24020075).to_bytes(4,"big"),
              "nickname":"Shooting Star Summit: Outside the Sanctuary"}, # crashes on load if without partners
    "hos_05":{"bytes":(0x24020076).to_bytes(4,"big"),
              "nickname":"Shooting Star Summit: Star Sanctuary"},
    "hos_06":{"bytes":(0x24020077).to_bytes(4,"big"),
              "nickname":"Shooting Star Summit: Merluvlee's House"},
    "hos_10":{"bytes":(0x24020078).to_bytes(4,"big"),
              "nickname":"Shooting Star Summit: Ending Descent Scene"}, # pretty useless for init spawn
    "hos_20":{"bytes":(0x24020079).to_bytes(4,"big"),
              "nickname":"Shooting Star Summit: Riding Star Ship Scene"},
    "kpa_01":{"bytes":(0x2402007A).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Dark Cave 1"},
    "kpa_03":{"bytes":(0x2402007B).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Dark Cave 2"},
    "kpa_04":{"bytes":(0x2402007C).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Cave Exit"},
    "kpa_08":{"bytes":(0x2402007D).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Castle Key Timing Puzzle"},
    "kpa_09":{"bytes":(0x2402007E).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Ultra Shroom Timing Puzzle"}, # spawn on puzzle solved side
    "kpa_10":{"bytes":(0x2402007F).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Outside Lower Jail (No Lava)"},
    "kpa_11":{"bytes":(0x24020080).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Outside Lower Jail (Lava)"},
    "kpa_12":{"bytes":(0x24020081).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Lava Channel 1"},
    "kpa_13":{"bytes":(0x24020082).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Lava Channel 2"},
    "kpa_14":{"bytes":(0x24020083).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Lava Channel 3"},
    "kpa_15":{"bytes":(0x24020084).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Lava Key Room"}, # pretty useless for init spawn
    "kpa_16":{"bytes":(0x24020085).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Lava Control Room"}, # pretty useless for init spawn
    "kpa_17":{"bytes":(0x24020086).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Lower Jail"},
    "kpa_32":{"bytes":(0x24020087).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Lower Grand Hall"},
    "kpa_33":{"bytes":(0x24020088).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Upper Grand Hall"},
    "kpa_40":{"bytes":(0x24020089).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Maze Guide Room"},
    "kpa_41":{"bytes":(0x2402008A).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Maze Room"},
    "kpa_50":{"bytes":(0x2402008B).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Hall to Guard Door 1"},
    "kpa_51":{"bytes":(0x2402008C).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Hall to Water Puzzle"},
    "kpa_52":{"bytes":(0x2402008D).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Split Level Hall"},
    "kpa_53":{"bytes":(0x2402008E).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Fake Peach Hallway"},
    "kpa_60":{"bytes":(0x2402008F).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Ship Enter/Exit Scenes"},
    "kpa_61":{"bytes":(0x24020090).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Battlement"},
    "kpa_62":{"bytes":(0x24020091).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Front Door Exterior"}, # similar to kpa_60 ?
    "kpa_63":{"bytes":(0x24020092).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Hanger"}, # default spawnlocation traps Mario
    "kpa_70":{"bytes":(0x24020093).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Entry Lava Hall"},
    "kpa_81":{"bytes":(0x24020094).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Guard Door 1"},
    "kpa_82":{"bytes":(0x24020095).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Guard Door 2"},
    "kpa_83":{"bytes":(0x24020096).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Guard Door 3"},
    "kpa_90":{"bytes":(0x24020097).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Stairs to East Upper Jail"},
    "kpa_91":{"bytes":(0x24020098).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: East Upper Jail"},
    "kpa_94":{"bytes":(0x24020099).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Stairs to West Upper Jail"},
    "kpa_95":{"bytes":(0x2402009A).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: West Upper Jail"},
    "kpa_96":{"bytes":(0x2402009B).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Item Shop"},
    "kpa_100":{"bytes":(0x2402009C).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Castle Key Room"},
    "kpa_101":{"bytes":(0x2402009D).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Ultra Shroom Room"},
    "kpa_102":{"bytes":(0x2402009E).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Blue Fire Bridge"},
    "kpa_111":{"bytes":(0x2402009F).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Room with Hidden Door 1"},
    "kpa_112":{"bytes":(0x240200A0).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Hidden Passage 1"},
    "kpa_113":{"bytes":(0x240200A1).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Room with Hidden Door 2"},
    "kpa_114":{"bytes":(0x240200A2).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Hidden Passage 2"}, # spawn under ground on load
    "kpa_115":{"bytes":(0x240200A3).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Room with Hidden Door 3"},
    "kpa_116":{"bytes":(0x240200A4).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Dead End Passage"},
    "kpa_117":{"bytes":(0x240200A5).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Dead End Room"},
    "kpa_118":{"bytes":(0x240200A6).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Hidden Passage 3"},
    "kpa_119":{"bytes":(0x240200A7).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Hidden Key Room"},
    "kpa_121":{"bytes":(0x240200A8).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Exit to Peach's Castle"},
    "kpa_130":{"bytes":(0x240200A9).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Bill Blaster Hall"},
    "kpa_133":{"bytes":(0x240200AA).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Left Water Puzzle"},
    "kpa_134":{"bytes":(0x240200AB).to_bytes(4,"big"),
              "nickname":"Bowser's Castle: Right Water Puzzle"},
    "osr_00":{"bytes":(0x240200AC).to_bytes(4,"big"),
              "nickname":"Peach's Castle Grounds: Intro Castle Grounds"},
    "osr_01":{"bytes":(0x240200AD).to_bytes(4,"big"),
              "nickname":"Peach's Castle Grounds: Ruined Castle Grounds"},
    "osr_02":{"bytes":(0x240200AE).to_bytes(4,"big"),
              "nickname":"Peach's Castle Grounds: Hijacked Castle Entrance"},
    "osr_03":{"bytes":(0x240200AF).to_bytes(4,"big"),
              "nickname":"Peach's Castle Grounds: Outside Hijacked Castle"}, # ???
    "osr_04":{"bytes":(0x240200B0).to_bytes(4,"big"),
              "nickname":"Peach's Castle Grounds: Castle Hijacking Scene"},
    "kkj_00":{"bytes":(0x240200B1).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Intro Entry Hall (1F)"},
    "kkj_01":{"bytes":(0x240200B2).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Intro Upper Hall (2F)"},
    "kkj_02":{"bytes":(0x240200B3).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Intro Stairs Hallway (3F)"},
    "kkj_03":{"bytes":(0x240200B4).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Intro Window Hallway (4F)"},
    "kkj_10":{"bytes":(0x240200B5).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Entry Hall (1F)"},
    "kkj_11":{"bytes":(0x240200B6).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Upper Hall (2F)"},
    "kkj_12":{"bytes":(0x240200B7).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Stairs Hallway (3F)"},
    "kkj_13":{"bytes":(0x240200B8).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Window Hallway (4F)"},
    "kkj_14":{"bytes":(0x240200B9).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Peach's Room (2F)"},
    "kkj_15":{"bytes":(0x240200BA).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Passage Outlet (2F)"},
    "kkj_16":{"bytes":(0x240200BB).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Library (2F)"},
    "kkj_17":{"bytes":(0x240200BC).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Storeroom (2F)"},
    "kkj_18":{"bytes":(0x240200BD).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Dining Room (2F)"},
    "kkj_19":{"bytes":(0x240200BE).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Kitchen (1F)"},
    "kkj_20":{"bytes":(0x240200BF).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Guest Room (1F)"},
    "kkj_21":{"bytes":(0x240200C0).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Inactive Quiz-Off (1F)"},
    "kkj_22":{"bytes":(0x240200C1).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Double Staircase (4F)"},
    "kkj_23":{"bytes":(0x240200C2).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Rooftop (5F)"},
    "kkj_24":{"bytes":(0x240200C3).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Tower Staircase (5F)"},
    "kkj_25":{"bytes":(0x240200C4).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Final Boss Arena (6F)"}, # crashes on load if without partners
    "kkj_26":{"bytes":(0x240200C5).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Balcony (2F)"},
#    "kkj_26.5":{"bytes":(0x240200C6).to_bytes(4,"big"),
#              "nickname":"Peach's Castle: Balcony ???"}, # kkj_26 w/ weird background ??
    "kkj_27":{"bytes":(0x240200C7).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Secret Passage (2F)"},
    "kkj_28":{"bytes":(0x240200C8).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Darkened Quiz-Off (1F)"},
    "kkj_29":{"bytes":(0x240200C9).to_bytes(4,"big"),
              "nickname":"Peach's Castle: Quiz-Off Room (1F)"},
#    "crash012":{"bytes":(0x240200CA).to_bytes(4,"big"),
#              "nickname":"Blackscreen"}, # jan_00 ?
#    "crash013":{"bytes":(0x240200CB).to_bytes(4,"big"),
#              "nickname":"Blackscreen"}, # jan_01 ?
    "jan_02":{"bytes":(0x240200CC).to_bytes(4,"big"),
              "nickname":"Jade Jungle: Village Cove"},
}