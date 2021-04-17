# ByteLocations in ROM
bl_starting_location = 0x168080

# ByteValues to write into ROM
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
}