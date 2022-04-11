

class Coords:

    coords = {
        "GOOMBA_1": (0, -1, 18, 18),
        "GOOMBA_2": (0, 18, 18, 18),
        "GOOMBA_3": (0, 38, 18, 18),
        "GOOMBA_4": (0, 58, 18, 8),
        "KOOPA_1": (18, -1, 20, 24),
        "KOOPA_2": (18, 28, 20, 24),
        "KOOPA_3": (18, 58, 20, 24),
        "KOOPA_4": (18, 88, 20, 24),
        "KOOPA_SHELL": (18, 120, 20, 24),
        "PLANT_1": (36, -1, 20, 24),
        "PLANT_2": (36, 28, 20, 24),

        # Little Mario
        "L_M_FSTAND": (57, -1, 18, 18),
        "L_M_F2": (58, 18, 18, 18),
        "L_M_F3": (58, 38, 18, 18),
        "L_M_F4": (58, 58, 18, 18),
        "L_M_F5": (58, 78, 18, 18),
        "L_M_FJUMP": (58, 98, 18, 18),
        "L_M_BSTAND": (57, 118, 16, 20),
        "L_M_B2": (57, 138, 19, 20),
        "L_M_B3": (57, 158, 16, 20),
        "L_M_B4": (57, 178, 16, 20),
        "L_M_B5": (57, 198, 18, 20),
        "L_M_BJUMP": (57, 218, 18, 18),
        "L_M_DIE": (57, 238, 18, 18),
        "M_FLAG": (57, 258, 18, 18),

        "L_M_FSTAND_W": (79, -1, 20, 16),
        "L_M_F2_W": (79, 18, 24, 16),
        "L_M_F3_W": (79, 38, 24, 16),
        "L_M_F4_W": (79, 58, 15, 17),
        "L_M_F5_W": (79, 78, 15, 18),
        "L_M_FJUMP_W": (79, 98, 18, 18),
        "L_M_BSTAND_W": (79, 118, 14, 18),
        "L_M_B2_W": (79, 138, 17, 18),
        "L_M_B3_W": (79, 158, 14, 18),
        "L_M_B4_W": (79, 178, 14, 18),
        "L_M_B5_W": (79, 198, 16, 18),
        "L_M_BJUMP_W": (79, 218, 18, 18),
        "L_M_DIE_W": (79, 238, 18, 18),

        "L_M_FSTAND_B": (99, -1, 20, 16),
        "L_M_F2_B": (99, 18, 24, 16),
        "L_M_F3_B": (99, 38, 24, 16),
        "L_M_F4_B": (99, 58, 15, 17),
        "L_M_F5_B": (99, 78, 15, 18),
        "L_M_FJUMP_B": (99, 98, 18, 18),
        "L_M_BSTAND_B": (99, 118, 14, 18),
        "L_M_B2_B": (99, 138, 17, 18),
        "L_M_B3_B": (99, 158, 14, 18),
        "L_M_B4_B": (99, 178, 14, 18),
        "L_M_B5_B": (99, 198, 16, 18),
        "L_M_BJUMP_B": (99, 218, 18, 18),

        #Big Mario
        "B_M_FSTAND": (119, -1, 18, 32),
        "B_M_F2": (119, 39, 18, 32),
        "B_M_F3": (119, 79, 16, 33),
        "B_M_F4": (119, 119, 18, 34),
        "B_M_F5": (119, 159, 18, 34),
        "B_M_FJUMP": (119, 199, 18, 33),
        "B_M_BSTAND": (119, 239, 18, 34),
        "B_M_B2": (119, 279, 18, 32),
        "B_M_B3": (119, 319, 16, 33),
        "B_M_B4": (119, 359, 18, 34),
        "B_M_B5": (119, 399, 18, 34),
        "B_M_BJUMP": (119, 439, 18, 33),

        "B_M_FSTAND_W": (139, -1, 18, 32),
        "B_M_F2_W": (139, 39, 18, 32),
        "B_M_F3_W": (139, 79, 16, 33),
        "B_M_F4_W": (139, 119, 18, 34),
        "B_M_F5_W": (139, 159, 18, 34),
        "B_M_FJUMP_W": (139, 199, 18, 33),
        "B_M_BSTAND_W": (139, 239, 18, 34),
        "B_M_B2_W": (139, 279, 18, 32),
        "B_M_B3_W": (139, 319, 16, 33),
        "B_M_B4_W": (139, 359, 18, 34),
        "B_M_B5_W": (139, 399, 18, 34),
        "B_M_BJUMP_W": (139, 439, 18, 33),

        "B_M_FSTAND_B": (159, -1, 18, 32),
        "B_M_F2_B": (159, 39, 18, 32),
        "B_M_F3_B": (159, 79, 16, 33),
        "B_M_F4_B": (159, 119, 18, 34),
        "B_M_F5_B": (159, 159, 18, 34),
        "B_M_FJUMP_B": (159, 199, 18, 33),
        "B_M_BSTAND_B": (159, 239, 18, 34),
        "B_M_B2_B": (159, 279, 18, 32),
        "B_M_B3_B": (159, 319, 16, 33),
        "B_M_B4_B": (159, 359, 18, 34),
        "B_M_B5_B": (159, 399, 18, 34),
        "B_M_BJUMP_B": (159, 439, 18, 33),

        #Items

        "COIN": (179, -1, 12, 16),
        "MUSHROOM": (179, 19, 18, 18),
        "1UP": (179, 39, 18, 18),
        "STAR_1": (179, 59, 16, 18),
        "STAR_2": (179, 79, 16, 18),
        "FLOWER": (179, 99, 19, 17),
        "FIREBALL": (179, 279, 10, 10),

        #Blocks

        "?_1": (179, 119, 18, 18),
        "?_2": (179, 139, 18, 18),
        "?_3": (179, 159, 18, 18),
        "BRICK": (179, 179, 18, 18),
        "BLUE_BRICK": (179, 199, 18, 18),
        "USED_BLOCK": (179, 219, 18, 18),
        "BLOCK": (179, 239, 18, 18),
        "BROKEN_BRICK": (179, 259, 18, 18),

        #Pipes

        "SHORT_PIPE": (199, -1, 34, 34),
        "MED_PIPE": (199, 39, 34, 49),
        "LONG_PIPE": (199, 89, 34, 66),
        "L_PIPE": (239, -1, 64, 178),

        #Flag

        "FLAG_POLE": (317, -1, 18, 170),
        "FLAG": (349, -1, 18, 19)

    }