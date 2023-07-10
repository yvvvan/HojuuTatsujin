from game.table import Table
from utils.logger import set_up_logging
from mahjong.tile import Tile, TilesConverter
from mahjong.constants import FIVE_RED_MAN, FIVE_RED_PIN, FIVE_RED_SOU
from mahjong.meld import Meld

# ROUND AND SEAT WIND
EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3
# PLAYER
SELF = 0
SHIMO = 1
TOIMEN = 2
KAMI = 3

def make_signal(signal, player_seat, tile="", meld_type=None, meld_tiles="", from_who=-1, opened=True):
    if tile:
        tile = TilesConverter.one_line_string_to_136_array(tile,has_aka_dora=True)[0]
    if meld_tiles:
        meld_tiles = TilesConverter.one_line_string_to_136_array(meld_tiles,has_aka_dora=True)
    if signal == Game.OTHER_DISCARD:
        return {
                "signal": signal, 
                "player_seat": player_seat, 
                "discard_tile": tile, 
                "drawn_tile": -1, 
                "meld": Meld(), 
                "new_dora_tile": -1
            }
    elif signal == Game.OTHER_CALL:
        return {
                "signal": signal, 
                "player_seat": player_seat, 
                "discard_tile": -1, 
                "drawn_tile": -1, 
                "meld": Meld(meld_type=meld_type, 
                            tiles=meld_tiles, opened=opened, called_tile=tile, who=player_seat, from_who=from_who), 
                "new_dora_tile": -1
            }
    elif signal == Game.OTHER_RIICHI:
        return {
                "signal": signal, 
                "player_seat": player_seat, 
                "discard_tile": -1, 
                "drawn_tile": -1, 
                "meld": Meld(), 
                "new_dora_tile": -1
            }
    elif signal == Game.OTHER_WIN:
            return {
                "signal": signal, 
                "player_seat": player_seat, 
                "discard_tile": -1, 
                "drawn_tile": -1, 
                "meld": Meld(), 
                "new_dora_tile": -1
            }
    elif signal == Game.NEW_DORA:
            return {
                "signal": signal, 
                "player_seat": player_seat, 
                "discard_tile": -1, 
                "drawn_tile": -1, 
                "meld": Meld(), 
                "new_dora_tile": tile
            }
    elif signal == Game.SELF_TURN:
            return {
                "signal": signal, 
                "player_seat": 0, 
                "discard_tile": -1, 
                "drawn_tile": tile, 
                "meld": Meld(), 
                "new_dora_tile": -1
            }
    
class Game:
    OTHER_DISCARD = "other_discard"
    OTHER_RIICHI = "other_riichi"
    OTHER_CALL = "other_call"
    OTHER_WIN = "other_win"
    NEW_DORA = "new_dora"
    SELF_TURN = "self_turn"

    def __init__(self):
        self.table = Table()
        self.logger = set_up_logging(save_to_file=False)
        for i in range(4):
            self.table.players[i].init_logger(self.logger)
        self.mainplayer = self.table.players[0]
        self.table.count_of_remaining_tiles -= 1

    def initialize_round(self, round_wind=EAST, seat_wind=EAST, initial_tiles="", dora_indicator="", honba_sticks=0, riichi_sticks=0):
        values_p = [{"name": "自家", "rank": "1"},     # main player, not east player
                    {"name": "下家", "rank": "1"},     # Shimocha 下家
                    {"name": "对家", "rank": "1"},     # Toimen   対面
                    {"name": "上家", "rank": "1"}]     # Kamicha  上家
        values = {  "round_wind_number": round_wind,      # 0 - east, 1 - south, 2 - west, 3 - north
                    "count_of_honba_sticks": honba_sticks,           # number of honba sticks
                    "count_of_riichi_sticks": riichi_sticks,          # number of riichi sticks
                    "dora_indicator": TilesConverter.one_line_string_to_136_array(dora_indicator,has_aka_dora=True)[0],  # 136 format tile
                    "dealer": (4-seat_wind)%4,          # 0 - Self, 1 - Shimocha, 2 - Toimen, 3 - Kamicha
                                                            #  └ so, self wind: 0 - east, 1 - north, 
                                                            #                   2 - west, 3 - south
                    "scores": [300, 300, 300, 300]}       # main player is 0
        tiles = TilesConverter.one_line_string_to_136_array(initial_tiles,has_aka_dora=True)
        self.set_table(values_p, values)
        self.mainplayer_init_hand(tiles)
        

    def set_table(self, values_p, values):
        self.table.set_players_names_and_ranks(values_p)
        self.table.init_round( values["round_wind_number"],
                               values["count_of_honba_sticks"],
                               values["count_of_riichi_sticks"],
                               values["dora_indicator"],
                               values["dealer"],
                               values["scores"],
                             )

    def mainplayer_init_hand(self, tiles):
        self.mainplayer.init_hand(tiles)

    def run(self, signals):

        signal = signals["signal"]
        player_seat = signals["player_seat"]     # who did the action ?
        discard_tile = signals["discard_tile"]   # is tile discarded ?
        drawn_tile = signals["drawn_tile"]       # is tile drawn ? (mainplayer only)
        meld = signals["meld"]                   # is meld called ? (other players only)
        meld.who = player_seat
        new_dora_tile = signals["new_dora_tile"] # is new dora tile revealed ?

        if signal == "other_discard":
            # 1 别家弃牌
            tile = discard_tile                                                 # 打的牌
            is_kamicha_discard = True if player_seat == 3 else False            # 是否是上家
            self.table.add_discarded_tile(player_seat, tile, is_tsumogiri=False)     # 打牌
            self.logger.info("{} discards {}".format(self.table.get_player(player_seat).name, TilesConverter.to_one_line_string([tile])))
            
            # 2 检查是否荣胡
            # TODO: 检查是否抢杠
            win = self.mainplayer.should_call_win(tile, is_tsumo=False, enemy_seat=player_seat)
            if win:
                self.logger.info("{} WIN by RON from {}!".format(self.mainplayer.name, self.table.get_player(player_seat).name))
                return "RON"

            # TODO：3 检查是否大明杠
            
            # 4 检查是否吃碰
            for i in range(4):
                if tile+i not in self.mainplayer.tiles:
                    tile = tile+i
                    break
            meld, tile_to_discard = self.mainplayer.try_to_call_meld(tile, is_kamicha_discard)
            if meld:
                # 副露
                meld.called_tile = tile
                self.table.add_called_meld(0, meld)
                # 添加副露获得的牌
                self.mainplayer.tiles.append(tile)
                # 打出一张牌
                tile_to_discard, with_riichi = self.mainplayer.discard_tile()
                self.table.count_of_remaining_tiles -= 1 #because of the interreuption of other's discard
        
        elif signal == "other_riichi":
            self.table.add_called_riichi_step_one(player_seat)
            self.table.add_called_riichi_step_two(player_seat)
        
        elif signal == "other_call":
            # 别家吃碰杠
            self.table.add_called_meld(player_seat, meld)
            self.logger.info("{} Meld: {}".format(self.table.get_player(player_seat).name, meld))
        
        elif signal == "other_win":
            self.logger.info("{} WIN!".format(self.table.get_player(player_seat).name))
            return "OTHER_WIN"
        
        elif signal == "new_dora":
            tile = new_dora_tile
            self.table.add_dora_indicator(tile)
            self.logger.info(
                "New dora indicator: {}".format(
                    TilesConverter.to_one_line_string([tile], print_aka_dora=self.table.has_aka_dora)
                )
            )
        
        elif signal == "self_turn":
            tile = drawn_tile
            # 1 检查是否自摸
            win = self.mainplayer.should_call_win(tile, is_tsumo=True)
            if win:
                self.logger.info("{} WIN by TSUMO!".format(self.mainplayer.name))
                return "TSUMO"
            # 2 摸牌
            self.mainplayer.draw_tile(tile)
            self.table.count_of_remaining_tiles -= 1
            # 3 TODO: 检查是否加杠/暗杠
            # 4 是否为立直状态
            if self.mainplayer.in_riichi:
                self.mainplayer.discard_tile(tile, force_tsumogiri=True)
                self.logger.info( "Discard: {}".format(TilesConverter.to_one_line_string(
                    [tile], print_aka_dora=self.table.has_aka_dora)))
            # 5 非立直打牌
            else:
                tile_to_discard, with_riichi = self.mainplayer.discard_tile()
                if with_riichi:
                    self.mainplayer.in_riichi = True
                    self.logger.info( "{} declares riichi!".format(self.mainplayer.name))
                self.logger.info( "Discard: {}".format(TilesConverter.to_one_line_string(
                    [tile_to_discard], print_aka_dora=self.table.has_aka_dora)))
        return