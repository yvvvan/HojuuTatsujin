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

        make_signal(Game.SELF_TURN, SELF, '5z'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '3z'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '3p'),
        make_signal(Game.OTHER_DISCARD, KAMI, '8m'),
        make_signal(Game.SELF_TURN, SELF, '3z'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '8s'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '6z'),
        make_signal(Game.OTHER_DISCARD, KAMI, '7z'),
        make_signal(Game.SELF_TURN, SELF, '4z'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '9s'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '9m'),
        make_signal(Game.OTHER_DISCARD, KAMI, '3m'),
        make_signal(Game.OTHER_CALL, SHIMO, '3m', Meld.PON, '333m', KAMI),
        make_signal(Game.OTHER_DISCARD, SHIMO, '6p'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '3s'),
        make_signal(Game.OTHER_DISCARD, KAMI, '2s'),
        make_signal(Game.SELF_TURN, SELF, '5z'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '5p'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '2p'),
        make_signal(Game.OTHER_DISCARD, KAMI, '4s'),
        make_signal(Game.OTHER_CALL, TOIMEN, '4s', Meld.PON, '444s', KAMI),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '5m'),
        make_signal(Game.OTHER_DISCARD, KAMI, '9m'),
        make_signal(Game.SELF_TURN, SELF, '6p'),
        make_signal(Game.OTHER_CALL, SHIMO, '1z', Meld.PON, '111z', SELF),
        make_signal(Game.OTHER_DISCARD, SHIMO, '5z'), # with our pon and discard
        make_signal(Game.OTHER_DISCARD, SHIMO, '1p'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '1s'),
        make_signal(Game.OTHER_DISCARD, KAMI, '2p'),
        make_signal(Game.SELF_TURN, SELF, '8p'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '5p'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '5p'),
        make_signal(Game.OTHER_DISCARD, KAMI, '4p'),
        make_signal(Game.OTHER_CALL, SHIMO, '7m', Meld.PON, '777m', SELF),
        make_signal(Game.OTHER_DISCARD, SHIMO, '6z'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '6s'),
        make_signal(Game.OTHER_DISCARD, KAMI, '7m'),
        make_signal(Game.SELF_TURN, SELF, '8m'),
        make_signal(Game.OTHER_CALL, SHIMO, '3s', Meld.CHI, '345s', SELF),
        make_signal(Game.OTHER_DISCARD, SHIMO, '9m'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '2z'),
        make_signal(Game.OTHER_DISCARD, KAMI, '5s'),
        make_signal(Game.SELF_TURN, SELF, '1m'),
        make_signal(Game.OTHER_CALL, TOIMEN, '8m', Meld.PON, '888m', SELF),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '3m'),
        make_signal(Game.OTHER_DISCARD, KAMI, '4p'),
        make_signal(Game.SELF_TURN, SELF, '2z'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '2z'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '4m'),
        make_signal(Game.OTHER_DISCARD, KAMI, '9p'),
        make_signal(Game.OTHER_CALL, TOIMEN, '9p', Meld.PON, '999p', KAMI),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '2p'),
        make_signal(Game.OTHER_DISCARD, KAMI, '3s'),
        make_signal(Game.SELF_TURN, SELF, '6p'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '1m'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '5m'),
        make_signal(Game.OTHER_DISCARD, KAMI, '3p'),
        make_signal(Game.SELF_TURN, SELF, '4z'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '6m'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '6p'),
        make_signal(Game.OTHER_DISCARD, KAMI, '2m'),
        make_signal(Game.SELF_TURN, SELF, '5s'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '1m'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '4p'),
        make_signal(Game.OTHER_DISCARD, KAMI, '8s'),
        make_signal(Game.SELF_TURN, SELF, '6z'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '6z'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '8p'),
        make_signal(Game.OTHER_DISCARD, KAMI, '6s'),
        make_signal(Game.SELF_TURN, SELF, '5m'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '2s'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '4m'),
        make_signal(Game.OTHER_CALL, KAMI, '7z', Meld.KAN, '7777z', KAMI, opened=False),
        make_signal(Game.NEW_DORA, None, '2m'),
        make_signal(Game.OTHER_DISCARD, KAMI, '4z'),
        make_signal(Game.SELF_TURN, SELF, '8s'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '7s'),
        make_signal(Game.OTHER_CALL, KAMI, '7s', Meld.PON, '777s', SHIMO),
        make_signal(Game.OTHER_DISCARD, KAMI, '1z'),
        make_signal(Game.SELF_TURN, SELF, '5m'),
        make_signal(Game.OTHER_DISCARD, SHIMO, '5p'),
        make_signal(Game.OTHER_DISCARD, TOIMEN, '8p'),
        make_signal(Game.OTHER_DISCARD, KAMI, '6m'),
        make_signal(Game.OTHER_WIN, SHIMO),
        ]

if __name__ == "__main__":
    game = Game()

    round_wind = EAST
    seat_wind = EAST
    initial_tiles = "1357s14667m23p13z"
    dora_indicator = "3p"
    honba_sticks = 0
    riichi_sticks = 0

    game.initialize_round(round_wind=round_wind, seat_wind=seat_wind, initial_tiles=initial_tiles, dora_indicator=dora_indicator, honba_sticks=honba_sticks, riichi_sticks=riichi_sticks)
    print("***********")

    signals = get_signals(game)

    for s in signals:
        game.run(s)
        context = [
            f"Step: {game.mainplayer.round_step}",
            f"Remaining tiles: {game.table.count_of_remaining_tiles}",
            f"Hand: {game.mainplayer.format_hand_for_print()}",
        ]
        if game.mainplayer.round_step == 5:
            ttttt = game
            print("***********")

        game.mainplayer.logger.debug("current state", context)
        game.logger.debug("====================================")