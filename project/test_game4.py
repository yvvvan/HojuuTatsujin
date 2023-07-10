from test_signal import TEST_SIGNAL
from yvanbot import Game
from yvanbot import make_signal
from yvanbot import EAST, SOUTH, WEST, NORTH, KAMI, SHIMO, TOIMEN, SELF
from mahjong.tile import Tile, TilesConverter
from mahjong.meld import Meld

def get_signals(game):
    return [
        # make_signal(signal, player, tile, meld_type, meld_tiles, from_who)
        # example:
        #   make_signal(Game.OTHER_DISCARD, KAMI, '1m'),
        #   make_signal(Game.OTHER_CALL, KAMI, '1m', Meld.PON, '111m', SELF),
        #   make_signal(Game.OTHER_WIN, KAMI),
        #   make_signal(Game.OTHER_RIICHI, KAMI),
        #   make_signal(Game.NEW_DORA, None, '1m'),
        #   make_signal(Game.SELF_TURN, SELF, '1m'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '3p'),
        make_signal(Game.OTHER_DISCARD, KAMI, '9m'),
        make_signal(Game.SELF_TURN, SELF, '2z'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '8p'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '4s'),
        make_signal(Game.OTHER_DISCARD, KAMI, '2s'),
        make_signal(Game.SELF_TURN, SELF, '3z'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '2p'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '9m'),
        make_signal(Game.OTHER_DISCARD, KAMI, '1s'),
        make_signal(Game.SELF_TURN, SELF, '1m'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '5p'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '7p'),
        make_signal(Game.OTHER_RIICHI, TOIMEN),
        make_signal(Game.OTHER_DISCARD, KAMI, '1m'),
        make_signal(Game.SELF_TURN, SELF, '2s'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '2z'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '1p'),
        make_signal(Game.OTHER_DISCARD, KAMI, '5s'),
        make_signal(Game.SELF_TURN, SELF, '6p'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '1p'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '4p'),
        make_signal(Game.OTHER_DISCARD, KAMI, '1s'),
        make_signal(Game.SELF_TURN, SELF, '3z'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '9p'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '5z'),
        make_signal(Game.OTHER_DISCARD, KAMI, '3s'),
        make_signal(Game.SELF_TURN, SELF, '6m'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '7s'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '2m'),
        make_signal(Game.OTHER_DISCARD, KAMI, '9p'),
        make_signal(Game.SELF_TURN, SELF, '2z'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '4s'),
        make_signal(Game.OTHER_RIICHI, SHIMO),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '6s'),
        make_signal(Game.OTHER_DISCARD, KAMI, '3s'),
        make_signal(Game.SELF_TURN, SELF, '9s'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '3z'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '6s'),
        make_signal(Game.OTHER_DISCARD, KAMI, '2p'),
        make_signal(Game.SELF_TURN, SELF, '7s'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '4m'),
        make_signal(Game.OTHER_WIN, TOIMEN),


        ]

if __name__ == "__main__":
    game = Game()

    round_wind = EAST
    seat_wind = WEST
    initial_tiles = "3669s3779m13p114z"
    dora_indicator = "2p"
    honba_sticks = 0
    riichi_sticks = 0

    game.initialize_round(round_wind=round_wind, seat_wind=seat_wind, initial_tiles=initial_tiles, dora_indicator=dora_indicator, honba_sticks=honba_sticks, riichi_sticks=riichi_sticks)
    game.table.has_aka_dora = False
    print("***********")

    signals = get_signals(game)

    for s in signals:
        game.run(s)
        context = [
            f"Step: {game.mainplayer.round_step}",
            f"Remaining tiles: {game.table.count_of_remaining_tiles}",
            f"Hand: {game.mainplayer.format_hand_for_print()}",
        ]
        game.mainplayer.logger.debug("current state", context)
        game.logger.debug("====================================")