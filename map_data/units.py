from triggers.enums.builtin_names import BuiltinUnit
from triggers.bases.enums import QuotedEnum


class Unit(QuotedEnum):
    ANY_UNIT = "AnyUnit"
    MEN = "Men"
    FACTORIES = "Factories"
    BUILDINGS = "Buildings"
    TERRAN_GHOST = "Terran Ghost"
    TERRAN_VULTURE = "Terran Vulture"
    TERRAN_GOLIATH = "Terran Goliath"
    GOLIATH_TURRET = "Goliath Turret"
    TERRAN_SIEGE_TANK_TANK_MODE = "Terran Siege Tank (Tank Mode)"
    TANK_TURRETTANK_MODE = "Tank Turret(Tank Mode)"
    TERRAN_SCV = "Terran SCV"
    TERRAN_WRAITH = "Terran Wraith"
    TERRAN_SCIENCE_VESSEL = "Terran Science Vessel"
    TERRAN_MARINE = "Terran Marine"
    GUI_MONTAG_FIREBAT = "Gui Montag (Firebat)"
    TERRAN_DROPSHIP = "Terran Dropship"
    TERRAN_BATTLECRUISER = "Terran Battlecruiser"
    VULTURE_SPIDER_MINE = "Vulture Spider Mine"
    NUCLEAR_MISSILE = "Nuclear Missile"
    TERRAN_CIVILIAN = "Terran Civilian"
    SARAH_KERRIGAN_GHOST = "Sarah Kerrigan (Ghost)"
    ALAN_SCHEZAR_GOLIATH = "Alan Schezar (Goliath)"
    ALAN_SCHEZAR_TURRET = "Alan Schezar Turret"
    JIM_RAYNOR_VULTURE = "Jim Raynor (Vulture)"
    JIM_RAYNOR_MARINE = "Jim Raynor (Marine)"
    TOM_KAZANSKY_WRAITH = "Tom Kazansky (Wraith)"
    MAGELLAN_SCIENCE_VESSEL = "Magellan (Science Vessel)"
    EDMUND_DUKE_SIEGE_TANK = "Edmund Duke (Siege Tank)"
    EDMUND_DUKE_TURRET = "Edmund Duke Turret"
    EDMUND_DUKE_SIEGE_MODE = "Edmund Duke (Siege Mode)"
    ARCTURUS_MENGSK_BATTLECRUISER = "Arcturus Mengsk (Battlecruiser)"
    HYPERION_BATTLECRUISER = "Hyperion (Battlecruiser)"
    NORAD_II_BATTLECRUISER = "Norad II (Battlecruiser)"
    TERRAN_SIEGE_TANK_SIEGE_MODE = "Terran Siege Tank (Siege Mode)"
    TANK_TURRET_SIEGE_MODE = "Tank Turret (Siege Mode)"
    FIREBAT = "Firebat"
    SCANNER_SWEEP = "Scanner Sweep"
    TERRAN_MEDIC = "Terran Medic"
    ZERG_LARVA = "Zerg Larva"
    ZERG_EGG = "Zerg Egg"
    ZERG_ZERGLING = "Zerg Zergling"
    ZERG_HYDRALISK = "Zerg Hydralisk"
    ZERG_ULTRALISK = "Zerg Ultralisk"
    ZERG_BROODLING = "Zerg Broodling"
    ZERG_DRONE = "Zerg Drone"
    ZERG_OVERLORD = "Zerg Overlord"
    ZERG_MUTALISK = "Zerg Mutalisk"
    ZERG_GUARDIAN = "Zerg Guardian"
    ZERG_QUEEN = "Zerg Queen"
    ZERG_DEFILER = "Zerg Defiler"
    ZERG_SCOURGE = "Zerg Scourge"
    TORRARSQUE_ULTRALISK = "Torrarsque (Ultralisk)"
    MATRIARCH_QUEEN = "Matriarch (Queen)"
    INFESTED_TERRAN = "Infested Terran"
    INFESTED_KERRIGAN = "Infested Kerrigan"
    UNCLEAN_ONE_DEFILER = "Unclean One (Defiler)"
    HUNTER_KILLER_HYDRALISK = "Hunter Killer (Hydralisk)"
    DEVOURING_ONE_ZERGLING = "Devouring One (Zergling)"
    KUKULZA_MUTALISK = "Kukulza (Mutalisk)"
    KUKULZA_GUARDIAN = "Kukulza (Guardian)"
    YGGDRASILL_OVERLORD = "Yggdrasill (Overlord)"
    TERRAN_VALKYRIE_FRIGATE = "Terran Valkyrie Frigate"
    MUTALISK_GUARDIAN_COCOON = "Mutalisk/Guardian Cocoon"
    PROTOSS_CORSAIR = "Protoss Corsair"
    PROTOSS_DARK_TEMPLARUNIT = "Protoss Dark Templar(Unit)"
    ZERG_DEVOURER = "Zerg Devourer"
    PROTOSS_DARK_ARCHON = "Protoss Dark Archon"
    PROTOSS_PROBE = "Protoss Probe"
    PROTOSS_ZEALOT = "Protoss Zealot"
    PROTOSS_DRAGOON = "Protoss Dragoon"
    PROTOSS_HIGH_TEMPLAR = "Protoss High Templar"
    PROTOSS_ARCHON = "Protoss Archon"
    PROTOSS_SHUTTLE = "Protoss Shuttle"
    PROTOSS_SCOUT = "Protoss Scout"
    PROTOSS_ARBITER = "Protoss Arbiter"
    PROTOSS_CARRIER = "Protoss Carrier"
    PROTOSS_INTERCEPTOR = "Protoss Interceptor"
    DARK_TEMPLARHERO = "Dark Templar(Hero)"
    ZERATUL_DARK_TEMPLAR = "Zeratul (Dark Templar)"
    TASSADAR_ZERATUL_ARCHON = "Tassadar/Zeratul (Archon)"
    FENIX_ZEALOT = "Fenix (Zealot)"
    FENIX_DRAGOON = "Fenix (Dragoon)"
    TASSADAR_TEMPLAR = "Tassadar (Templar)"
    MOJO_SCOUT = "Mojo (Scout)"
    WARBRINGER_REAVER = "Warbringer (Reaver)"
    GANTRITHOR_CARRIER = "Gantrithor (Carrier)"
    PROTOSS_REAVER = "Protoss Reaver"
    PROTOSS_OBSERVER = "Protoss Observer"
    PROTOSS_SCARAB = "Protoss Scarab"
    DANIMOTH_ARBITER = "Danimoth (Arbiter)"
    ALDARIS_TEMPLAR = "Aldaris (Templar)"
    ARTANIS_SCOUT = "Artanis (Scout)"
    RHYNADON_BADLANDS_CRITTER = "Rhynadon (Badlands Critter)"
    BENGALAAS_JUNGLE_CRITTER = "Bengalaas (Jungle Critter)"
    SCANTID_DESERT_CRITTER = "Scantid (Desert Critter)"
    KAKARU_TWILIGHT_CRITTER = "Kakaru (Twilight Critter)"
    RAGNASAUR_ASHWORLD_CRITTER = "Ragnasaur (Ashworld Critter)"
    URSADON_ICE_WORLD_CRITTER = "Ursadon (Ice World Critter)"
    LURKER_EGG = "Lurker Egg"
    RASZAGAL_CORSAIR = "Raszagal (Corsair)"
    SAMIR_DURAN_GHOST = "Samir Duran (Ghost)"
    ALEXEI_STUKOV_GHOST = "Alexei Stukov (Ghost)"
    MAP_REVEALER = "Map Revealer"
    GERARD_DUGALLE_BATTLECRUISER = "Gerard DuGalle (Battlecruiser)"
    ZERG_LURKER = "Zerg Lurker"
    INFESTED_DURAN = "Infested Duran"
    DISRUPTION_WEB = "Disruption Web"
    TERRAN_COMMAND_CENTER = "Terran Command Center"
    TERRAN_COMSAT_STATION = "Terran Comsat Station"
    TERRAN_NUCLEAR_SILO = "Terran Nuclear Silo"
    TERRAN_SUPPLY_DEPOT = "Terran Supply Depot"
    TERRAN_REFINERY = "Terran Refinery"
    TERRAN_BARRACKS = "Terran Barracks"
    TERRAN_ACADEMY = "Terran Academy"
    TERRAN_FACTORY = "Terran Factory"
    TERRAN_STARPORT = "Terran Starport"
    TERRAN_CONTROL_TOWER = "Terran Control Tower"
    TERRAN_SCIENCE_FACILITY = "Terran Science Facility"
    TERRAN_COVERT_OPS = "Terran Covert Ops"
    TERRAN_PHYSICS_LAB = "Terran Physics Lab"
    TERRAN_MACHINE_SHOP = "Terran Machine Shop"
    TERRAN_ENGINEERING_BAY = "Terran Engineering Bay"
    TERRAN_ARMORY = "Terran Armory"
    TERRAN_MISSILE_TURRET = "Terran Missile Turret"
    TERRAN_BUNKER = "Terran Bunker"
    NORAD_II = "Norad II"
    ION_CANNON = "Ion Cannon"
    URAJ_CRYSTAL = "Uraj Crystal"
    KHALIS_CRYSTAL = "Khalis Crystal"
    INFESTED_COMMAND_CENTER = "Infested Command Center"
    ZERG_HATCHERY = "Zerg Hatchery"
    ZERG_LAIR = "Zerg Lair"
    ZERG_HIVE = "Zerg Hive"
    ZERG_NYDUS_CANAL = "Zerg Nydus Canal"
    ZERG_HYDRALISK_DEN = "Zerg Hydralisk Den"
    ZERG_DEFILER_MOUND = "Zerg Defiler Mound"
    ZERG_GREATER_SPIRE = "Zerg Greater Spire"
    ZERG_QUEENS_NEST = "Zerg Queen's Nest"
    ZERG_EVOLUTION_CHAMBER = "Zerg Evolution Chamber"
    ZERG_ULTRALISK_CAVERN = "Zerg Ultralisk Cavern"
    ZERG_SPIRE = "Zerg Spire"
    ZERG_SPAWNING_POOL = "Zerg Spawning Pool"
    ZERG_CREEP_COLONY = "Zerg Creep Colony"
    ZERG_SPORE_COLONY = "Zerg Spore Colony"
    UNUSED_ZERG_BUILDING = "Unused Zerg Building"
    ZERG_SUNKEN_COLONY = "Zerg Sunken Colony"
    ZERG_OVERMIND_WITH_SHELL = "Zerg Overmind (With Shell)"
    ZERG_OVERMIND = "Zerg Overmind"
    ZERG_EXTRACTOR = "Zerg Extractor"
    MATURE_CHRYSALIS = "Mature Chrysalis"
    ZERG_CEREBRATE = "Zerg Cerebrate"
    ZERG_CEREBRATE_DAGGOTH = "Zerg Cerebrate Daggoth"
    UNUSED_ZERG_BUILDING_5 = "Unused Zerg Building 5"
    PROTOSS_NEXUS = "Protoss Nexus"
    PROTOSS_ROBOTICS_FACILITY = "Protoss Robotics Facility"
    PROTOSS_PYLON = "Protoss Pylon"
    PROTOSS_ASSIMILATOR = "Protoss Assimilator"
    UNUSED_PROTOSS_BUILDING = "Unused Protoss Building"
    PROTOSS_OBSERVATORY = "Protoss Observatory"
    PROTOSS_GATEWAY = "Protoss Gateway"
    PROTOSS_PHOTON_CANNON = "Protoss Photon Cannon"
    PROTOSS_CITADEL_OF_ADUN = "Protoss Citadel of Adun"
    PROTOSS_CYBERNETICS_CORE = "Protoss Cybernetics Core"
    PROTOSS_TEMPLAR_ARCHIVES = "Protoss Templar Archives"
    PROTOSS_FORGE = "Protoss Forge"
    PROTOSS_STARGATE = "Protoss Stargate"
    STASIS_CELL_PRISON = "Stasis Cell/Prison"
    PROTOSS_FLEET_BEACON = "Protoss Fleet Beacon"
    PROTOSS_ARBITER_TRIBUNAL = "Protoss Arbiter Tribunal"
    PROTOSS_ROBOTICS_SUPPORT_BAY = "Protoss Robotics Support Bay"
    PROTOSS_SHIELD_BATTERY = "Protoss Shield Battery"
    KHAYDARIN_CRYSTAL_FORMATION = "Khaydarin Crystal Formation"
    PROTOSS_TEMPLE = "Protoss Temple"
    XELNAGA_TEMPLE = "Xel'Naga Temple"
    MINERAL_FIELD_TYPE_1 = "Mineral Field (Type 1)"
    MINERAL_FIELD_TYPE_2 = "Mineral Field (Type 2)"
    MINERAL_FIELD_TYPE_3 = "Mineral Field (Type 3)"
    CAVE = "Cave"
    CAVE_IN = "Cave-in"
    CANTINA = "Cantina"
    MINING_PLATFORM = "Mining Platform"
    INDEPENDANT_COMMAND_CENTER = "Independant Command Center"
    INDEPENDANT_STARPORT = "Independant Starport"
    JUMP_GATE = "Jump Gate"
    RUINS = "Ruins"
    KYADARIN_CRYSTAL_FORMATION = "Kyadarin Crystal Formation"
    VESPENE_GEYSER = "Vespene Geyser"
    WARP_GATE = "Warp Gate"
    PSI_DISRUPTOR = "PSI Disruptor"
    ZERG_MARKER = "Zerg Marker"
    TERRAN_MARKER = "Terran Marker"
    PROTOSS_MARKER = "Protoss Marker"
    ZERG_BEACON = "Zerg Beacon"
    TERRAN_BEACON = "Terran Beacon"
    PROTOSS_BEACON = "Protoss Beacon"
    ZERG_FLAG_BEACON = "Zerg Flag Beacon"
    TERRAN_FLAG_BEACON = "Terran Flag Beacon"
    PROTOSS_FLAG_BEACON = "Protoss Flag Beacon"
    POWER_GENERATOR = "Power Generator"
    OVERMIND_COCOON = "Overmind Cocoon"
    DARK_SWARM = "Dark Swarm"
    FLOOR_MISSILE_TRAP = "Floor Missile Trap"
    FLOOR_HATCH = "Floor Hatch"
    LEFT_UPPER_LEVEL_DOOR = "Left Upper Level Door"
    RIGHT_UPPER_LEVEL_DOOR = "Right Upper Level Door"
    LEFT_PIT_DOOR = "Left Pit Door"
    RIGHT_PIT_DOOR = "Right Pit Door"
    FLOOR_GUN_TRAP = "Floor Gun Trap"
    LEFT_WALL_MISSILE_TRAP = "Left Wall Missile Trap"
    LEFT_WALL_FLAME_TRAP = "Left Wall Flame Trap"
    RIGHT_WALL_MISSILE_TRAP = "Right Wall Missile Trap"
    RIGHT_WALL_FLAME_TRAP = "Right Wall Flame Trap"
    START_LOCATION = "Start Location"
    FLAG = "Flag"
    YOUNG_CHRYSALIS = "Young Chrysalis"
    PSI_EMITTER = "Psi Emitter"
    DATA_DISC = "Data Disc"
    KHAYDARIN_CRYSTAL = "Khaydarin Crystal"
    MINERAL_CLUSTER_TYPE_1 = "Mineral Cluster Type 1"
    MINERAL_CLUSTER_TYPE_2 = "Mineral Cluster Type 2"
    PROTOSS_VESPENE_GAS_ORB_TYPE_1 = "Vespene Orb (Protoss Type 1)"
    PROTOSS_VESPENE_GAS_ORB_TYPE_2 = "Vespene Orb (Protoss Type 2)"
    ZERG_VESPENE_GAS_SAC_TYPE_1 = "Vespene Sac (Zerg Type 1)"
    ZERG_VESPENE_GAS_SAC_TYPE_2 = "Vespene Sac (Zerg Type 2)"
    TERRAN_VESPENE_GAS_TANK_TYPE_1 = "Vespene Tank (Terran Type 1)"
    TERRAN_VESPENE_GAS_TANK_TYPE_2 = "Vespene Tank (Terran Type 2)"


class DeathCounters(QuotedEnum):
    EVERY_12DC = Unit.START_LOCATION.value
    EVERY_1200DC = Unit.MAP_REVEALER.value
    TAX_MINERAL_DC = Unit.TERRAN_VESPENE_GAS_TANK_TYPE_1.value
    ENEMY_TECH_LEVEL = Unit.TERRAN_VESPENE_GAS_TANK_TYPE_2.value
    SPAWN_UNIT_RANDOM_VALUE = Unit.ZERG_VESPENE_GAS_SAC_TYPE_1.value
    SPAWN_LOCATION_RANDOM_VALUE = Unit.ZERG_VESPENE_GAS_SAC_TYPE_2.value
