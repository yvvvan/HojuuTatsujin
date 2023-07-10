from game.table import Table
from utils.logger import set_up_logging
from mahjong.tile import Tile, TilesConverter
from mahjong.constants import FIVE_RED_MAN, FIVE_RED_PIN, FIVE_RED_SOU
from mahjong.meld import Meld

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
            meld, tile_to_discard = self.mainplayer.try_to_call_meld(tile, is_kamicha_discard)
            if meld:
                # 副露
                self.table.add_called_meld(0, meld)
                # 添加副露获得的牌
                self.mainplayer.tiles.append(tile)
                # 打出一张牌
                tile_to_discard, with_riichi = self.mainplayer.discard_tile()
        
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