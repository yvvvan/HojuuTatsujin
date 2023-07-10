from test_signal import TEST_SIGNAL
from yvanbot import Game

if __name__ == "__main__":
    
    values_p = [{"name": "自家", "rank": "1"},     # main player, not east player
                {"name": "下家", "rank": "1"},     # Shimocha 下家
                {"name": "对家", "rank": "1"},     # Toimen   対面
                {"name": "上家", "rank": "1"}]     # Kamicha  上家

    values = {  "round_wind_number": 0,               # 0 - east, 1 - south, 2 - west, 3 - north
                "count_of_honba_sticks": 0,           # number of honba sticks
                "count_of_riichi_sticks": 0,          # number of riichi sticks
                "dora_indicator": 84,                 # 136 format tile
                "dealer": 3,                          # 0 - Self, 1 - Shimocha, 2 - Toimen, 3 - Kamicha
                                                        #  └ so, self wind: 0 - east, 1 - north, 
                                                        #                   2 - west, 3 - south
                "scores": [300, 300, 300, 300]}       # main player is 0

    tiles = [4, 17, 24, 56, 64, 72, 76, 92, 96, 104, 108, 116, 117]


    # get from cv
    
    # ron
    signals = TEST_SIGNAL
    
    game = Game()
    game.set_table(values_p, values)
    game.mainplayer_init_hand(tiles)
    print("***********")

    for s in signals:
        game.run(s)
        context = [
            f"Step: {game.mainplayer.round_step}",
            f"Remaining tiles: {game.table.count_of_remaining_tiles}",
            f"Hand: {game.mainplayer.format_hand_for_print()}",
        ]
        
        game.mainplayer.logger.debug("current state", context)
        game.logger.debug("====================================")