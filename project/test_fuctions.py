from game.table import Table
from utils.logger import set_up_logging
from mahjong.tile import Tile, TilesConverter
from mahjong.constants import FIVE_RED_MAN, FIVE_RED_PIN, FIVE_RED_SOU
from utils.decisions_logger import MeldPrint
from mahjong.meld import Meld

def print_tiles(tiles):
    if isinstance(tiles, list): 
        tiles = TilesConverter.to_one_line_string(tiles, print_aka_dora=True)
    else:
        tiles = TilesConverter.to_one_line_string([tiles], print_aka_dora=True)
    print(tiles)



logger = set_up_logging(save_to_file=False)


table = Table()
for i in range(4):
    table.players[i].init_logger(logger)

values = [{"name": "Player1", "rank": "1"},     # main player, not east player
          {"name": "Player2", "rank": "1"},     # Shimocha 下家
          {"name": "Player3", "rank": "1"},     # Toimen   対面
          {"name": "Player4", "rank": "1"}]     # Kamicha  上家
table.set_players_names_and_ranks(values)

values = {"round_wind_number": 2,               # 0 - east, 1 - south, 2 - west, 3 - north
          "count_of_honba_sticks": 0,           # number of honba sticks
          "count_of_riichi_sticks": 0,          # number of riichi sticks
          "dora_indicator": 25,                 # 136 format tile
          "dealer": 2,                          # 0 - Self, 1 - Shimocha, 2 - Toimen, 3 - Kamicha
                                                #  └ so, self wind: 0 - east, 1 - north, 
                                                #                   2 - west, 3 - south
          "scores": [300, 300, 300, 300]}
table.init_round( values["round_wind_number"],
                  values["count_of_honba_sticks"],
                  values["count_of_riichi_sticks"],
                  values["dora_indicator"],
                  values["dealer"],
                  values["scores"],
                )

#tiles = [6, 11, 16, 45, 47, 60, 65, 80, 83, 92, 114, 117, 122]
tiles = [16, 20, 24, 36, 37, 38, 44, 48, 52, 72, 76, 132, 133]
table.player.init_hand(tiles)

logger.info(table)
logger.info("Players: {}".format(table.get_players_sorted_by_scores()))
logger.info("Dealer: {}".format(table.get_player(values["dealer"])))

# print(table.count_of_remaining_tiles) # 70 = 136 - 13 * 4 - 14
table.count_of_remaining_tiles -= 1
# for i in range(4):
#     player_seat = (i + table.dealer_seat) % 4
#     if player_seat == 0:
#         # main player
#         break


#######################
# 行为：别的玩家打牌+自己副露
player_seat = 2                                                     # 打牌的人
meld = MeldPrint()
meld.type = "chi"
meld.tiles = [1, 5, 9]
meld.called_tile = 9
meld.opened = True
meld.who = 2

table.add_called_meld(player_seat, meld)
logger.info("Meld: {} by {}".format(meld, table.get_player(player_seat).name))

tile = 122                                                           # 打的牌
is_kamicha_discard = True if player_seat == 3 else False            # 是否是上家
table.add_discarded_tile(player_seat, tile, is_tsumogiri=False)     # 打牌
logger.info("{} discards {}".format(table.get_player(player_seat).name, TilesConverter.to_one_line_string([tile])))
# table.add_called_riichi_step_one(player_seat)
# table.add_called_riichi_step_two(player_seat)
# 检查是否可以副露


# #######################
# # 行为：别的玩家打牌
# player_seat = 1                                                     # 打牌的人
# tile = 114                                                          # 打的牌
# is_kamicha_discard = True if player_seat == 3 else False            # 是否是上家
# table.add_discarded_tile(player_seat, tile, is_tsumogiri=False)     # 打牌
# logger.info("{} discards {}".format(table.get_player(player_seat).name, TilesConverter.to_one_line_string([tile])))

# # 检查是否可以副露
# meld, tile_to_discard = table.player.try_to_call_meld(tile, is_kamicha_discard)
# # 如果可以副露
# if meld:
#     # 副露
#     table.add_called_meld(0, meld)
#     # 添加副露获得的牌
#     table.player.tiles.append(tile)
#     # 打出一张牌
#     tile_to_discard, with_riichi = table.player.discard_tile()
#     print("***************")
#     print("Meld:", end=" ")
#     print(meld.type, end=" ")
#     print("Get:", end=" ")
#     print_tiles(tile)
#     print("discard:", end=" ")
#     print_tiles(tile_to_discard)
#     print("Tiles:", end=" ")
#     print_tiles(table.player.tiles)
#     print("Hand:", end=" ")
#     print_tiles(table.player.closed_hand)
#     print(table.count_of_remaining_tiles)
#     print("***************")

# #######################
# # 行为：别的玩家打牌
# player_seat = 2                                                     # 打牌的人
# tile = 115                                                          # 打的牌
# is_kamicha_discard = True if player_seat == 3 else False            # 是否是上家
# table.add_discarded_tile(player_seat, tile, is_tsumogiri=False)     # 打牌
# logger.info("{} discards {}".format(table.get_player(player_seat).name, TilesConverter.to_one_line_string([tile])))

# # 检查是否可以副露
# meld, tile_to_discard = table.player.try_to_call_meld(tile, is_kamicha_discard)
# # 如果可以副露
# if meld:
#     # 副露
#     table.add_called_meld(0, meld)
#     # 添加副露获得的牌
#     table.player.tiles.append(tile)
#     # 打出一张牌
#     tile_to_discard, with_riichi = table.player.discard_tile()
#     print("***************")
#     print("Meld:", end=" ")
#     print(meld.type, end=" ")
#     print("Get:", end=" ")
#     print_tiles(tile)
#     print("discard:", end=" ")
#     print_tiles(tile_to_discard)
#     print("Tiles:", end=" ")
#     print_tiles(table.player.tiles)
#     print("Hand:", end=" ")
#     print_tiles(table.player.closed_hand)
#     print(table.count_of_remaining_tiles)
#     print("***************")

# #######################
# # 行为：别的玩家打牌
# player_seat = 3                                                     # 打牌的人
# tile = 68                                                          # 打的牌
# is_kamicha_discard = True if player_seat == 3 else False            # 是否是上家
# table.add_discarded_tile(player_seat, tile, is_tsumogiri=False)     # 打牌
# logger.info("{} discards {}".format(table.get_player(player_seat).name, TilesConverter.to_one_line_string([tile])))

# # 检查是否可以副露
# meld, tile_to_discard = table.player.try_to_call_meld(tile, is_kamicha_discard)
# # 如果可以副露
# if meld:
#     # 副露
#     table.add_called_meld(0, meld)
#     # 添加副露获得的牌
#     table.player.tiles.append(tile)
#     # 打出一张牌
#     tile_to_discard, with_riichi = table.player.discard_tile()
#     print("***************")
#     print("Meld:", end=" ")
#     print(meld.type, end=" ")
#     print("Get:", end=" ")
#     print_tiles(tile)
#     print("discard:", end=" ")
#     print_tiles(tile_to_discard)
#     print("Tiles:", end=" ")
#     print_tiles(table.player.tiles)
#     print("Hand:", end=" ")
#     print_tiles(table.player.closed_hand)
#     print(table.count_of_remaining_tiles)
#     print("***************")

# #######################
# # 行为：别的玩家打牌
# player_seat = 1                                                     # 打牌的人
# tile = 116                                                          # 打的牌
# is_kamicha_discard = True if player_seat == 3 else False            # 是否是上家
# table.add_discarded_tile(player_seat, tile, is_tsumogiri=False)     # 打牌
# logger.info("{} discards {}".format(table.get_player(player_seat).name, TilesConverter.to_one_line_string([tile])))

# # 检查是否可以副露
# meld, tile_to_discard = table.player.try_to_call_meld(tile, is_kamicha_discard)
# # 如果可以副露
# if meld:
#     # 副露
#     table.add_called_meld(0, meld)
#     # 添加副露获得的牌
#     table.player.tiles.append(tile)
#     # 打出一张牌
#     tile_to_discard, with_riichi = table.player.discard_tile()
#     print("***************")
#     print("Meld:", end=" ")
#     print(meld.type, end=" ")
#     print("Get:", end=" ")
#     print_tiles(tile)
#     print("discard:", end=" ")
#     print_tiles(tile_to_discard)
#     print("Tiles:", end=" ")
#     print_tiles(table.player.tiles)
#     print("Hand:", end=" ")
#     print_tiles(table.player.closed_hand)
#     print(table.count_of_remaining_tiles)
#     print("***************")

# #######################
# # 行为：别的玩家打牌
# player_seat = 2                                                     # 打牌的人
# tile = 117                                                          # 打的牌
# is_kamicha_discard = True if player_seat == 3 else False            # 是否是上家
# table.add_discarded_tile(player_seat, tile, is_tsumogiri=False)     # 打牌
# logger.info("{} discards {}".format(table.get_player(player_seat).name, TilesConverter.to_one_line_string([tile])))

# # 检查是否可以副露
# meld, tile_to_discard = table.player.try_to_call_meld(tile, is_kamicha_discard)
# # 如果可以副露
# if meld:
#     # 副露
#     table.add_called_meld(0, meld)
#     # 添加副露获得的牌
#     table.player.tiles.append(tile)
#     # 打出一张牌
#     tile_to_discard, with_riichi = table.player.discard_tile()
#     print("***************")
#     print("Meld:", end=" ")
#     print(meld.type, end=" ")
#     print("Get:", end=" ")
#     print_tiles(tile)
#     print("discard:", end=" ")
#     print_tiles(tile_to_discard)
#     print("Tiles:", end=" ")
#     print_tiles(table.player.tiles)
#     print("Hand:", end=" ")
#     print_tiles(table.player.closed_hand)
#     print(table.count_of_remaining_tiles)
#     print("***************")

# #######################
# # 行为：别的玩家打牌
# player_seat = 3                                                     # 打牌的人
# tile = 118                                                          # 打的牌
# is_kamicha_discard = True if player_seat == 3 else False            # 是否是上家
# table.add_discarded_tile(player_seat, tile, is_tsumogiri=False)     # 打牌
# logger.info("{} discards {}".format(table.get_player(player_seat).name, TilesConverter.to_one_line_string([tile])))

# # 检查是否可以副露
# meld, tile_to_discard = table.player.try_to_call_meld(tile, is_kamicha_discard)
# # 如果可以副露
# if meld:
#     # 副露
#     table.add_called_meld(0, meld)
#     # 添加副露获得的牌
#     table.player.tiles.append(tile)
#     # 打出一张牌
#     tile_to_discard, with_riichi = table.player.discard_tile()
#     print("***************")
#     print("Meld:", end=" ")
#     print(meld.type, end=" ")
#     print("Get:", end=" ")
#     print_tiles(tile)
#     print("discard:", end=" ")
#     print_tiles(tile_to_discard)
#     print("Tiles:", end=" ")
#     print_tiles(table.player.tiles)
#     print("Hand:", end=" ")
#     print_tiles(table.player.closed_hand)
#     print(table.count_of_remaining_tiles)
#     print("***************")

# #######################
# # 行为：自己摸牌
# tile = 42
# # 摸牌
# table.player.draw_tile(tile)
# # 打牌
# tile_to_discard, with_riichi = table.player.discard_tile()
# table.count_of_remaining_tiles -= 1

# print("***************")
# print("Get:", end=" ")
# print_tiles(tile)
# print("discard:", end=" ")
# print_tiles(tile_to_discard)
# print("Tiles:", end=" ")
# print_tiles(table.player.tiles)
# print("Hand:", end=" ")
# print_tiles(table.player.closed_hand)
# print(table.count_of_remaining_tiles)
# print("***************")

# #######################
# # 行为：别的玩家打牌
# player_seat = 1                                                     # 打牌的人
# tile = 49                                                          # 打的牌
# is_kamicha_discard = True if player_seat == 3 else False            # 是否是上家
# table.add_discarded_tile(player_seat, tile, is_tsumogiri=False)     # 打牌
# logger.info("{} discards {}".format(table.get_player(player_seat).name, TilesConverter.to_one_line_string([tile])))

# # 检查是否可以副露
# meld, tile_to_discard = table.player.try_to_call_meld(tile, is_kamicha_discard)
# # 如果可以副露
# if meld:
#     # 副露
#     table.add_called_meld(0, meld)
#     # 添加副露获得的牌
#     table.player.tiles.append(tile)
#     # 打出一张牌
#     tile_to_discard, with_riichi = table.player.discard_tile()
#     print("***************")
#     print("Meld:", end=" ")
#     print(meld.type, end=" ")
#     print("Get:", end=" ")
#     print_tiles(tile)
#     print("discard:", end=" ")
#     print_tiles(tile_to_discard)
#     print("Tiles:", end=" ")
#     print_tiles(table.player.tiles)
#     print("Hand:", end=" ")
#     print_tiles(table.player.closed_hand)
#     print(table.count_of_remaining_tiles)
#     print("***************")
# win = table.player.should_call_win(tile, is_tsumo=False, enemy_seat=player_seat)
# if win:
#     print("***************")
#     print("win:", end=" ")
#     print_tiles(tile)
#     print("***************")

tile = 114
# 1 检查是否自摸
win = table.player.should_call_win(tile, is_tsumo=True)
if win:
    print("TSUMO!!!")
    exit()
# 2 摸牌
table.player.draw_tile(tile)
table.count_of_remaining_tiles -= 1
# 3 TODO: 检查是否加杠/暗杠
# 4 是否为立直状态
if table.player.in_riichi:
    table.player.discard_tile(tile, force_tsumogiri=True)
    logger.info( "Discard: {}".format(TilesConverter.to_one_line_string(
            [tile], print_aka_dora=table.has_aka_dora)))
# 5 非立直打牌
else:
    tile_to_discard, with_riichi = table.player.discard_tile()
    if with_riichi:
        table.player.in_riichi = True
        logger.info( "{} declares riichi!".format(table.player.name))
    logger.info( "Discard: {}".format(TilesConverter.to_one_line_string(
        [tile_to_discard], print_aka_dora=table.has_aka_dora)))
    

TEST_SIGNAL = [
    {
    "signal": "other_discard", 
    "player_seat": 2, 
    "discard_tile": 134, 
    "drawn_tile": 0, 
    "meld": Meld(meld_type=Meld.CHI, tiles=[1, 5, 9], opened=True, called_tile=9, who=None, from_who=None), 
    "new_dora_tile": 0
    },{
    "signal": "other_discard", 
    "player_seat": 2, 
    "discard_tile": 134, 
    "drawn_tile": 0, 
    "meld": Meld(meld_type=Meld.CHI, tiles=[1, 5, 9], opened=True, called_tile=9, who=None, from_who=None), 
    "new_dora_tile": 0
    },{
    "signal": "other_discard", 
    "player_seat": 2, 
    "discard_tile": 134, 
    "drawn_tile": 0, 
    "meld": Meld(meld_type=Meld.CHI, tiles=[1, 5, 9], opened=True, called_tile=9, who=None, from_who=None), 
    "new_dora_tile": 0
    },{
    "signal": "other_discard", 
    "player_seat": 2, 
    "discard_tile": 134, 
    "drawn_tile": 0, 
    "meld": Meld(meld_type=Meld.CHI, tiles=[1, 5, 9], opened=True, called_tile=9, who=None, from_who=None), 
    "new_dora_tile": 0
    },{
    "signal": "other_discard", 
    "player_seat": 2, 
    "discard_tile": 134, 
    "drawn_tile": 0, 
    "meld": Meld(meld_type=Meld.CHI, tiles=[1, 5, 9], opened=True, called_tile=9, who=None, from_who=None), 
    "new_dora_tile": 0
    },
]