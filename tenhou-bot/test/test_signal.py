from mahjong.meld import Meld
from yvanbot import Game

TEST_SIGNAL = [
    ########## 第一巡
    {
        # 上家打出白板 / 庄
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 124, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸到1p 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 36
        "drawn_tile": 36, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打出发财
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 128, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打出3p
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 44, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第二巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 37, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 108
        "drawn_tile": 93, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 48, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 28, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第三巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 89, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 4 
        "drawn_tile": 32, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 77, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 102, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第四巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 78, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 104 
        "drawn_tile": 20, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 73, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 125, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第五巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 5, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 32 
        "drawn_tile": 21, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 38, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 100, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第六巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 84, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 0
        "drawn_tile": 0, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 121, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 105, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第七巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 40, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 1
        "drawn_tile": 1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 41, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 45, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第八巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 118, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 129
        "drawn_tile": 129, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 68, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 42, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第九巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 109, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 46
        "drawn_tile": 46, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 90, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 106, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第十巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 130, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 20
        "drawn_tile": 94, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 107, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 112, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第十一巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 131, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 72
        "drawn_tile": 85, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 97, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 33, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第十一巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 110, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 34
        "drawn_tile": 34, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 98, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 18, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第十二巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 80, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 116
        "drawn_tile": 99, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 69, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 119, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第十三巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 8, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 自家摸牌 并打牌
        "signal": Game.SELF_TURN,
        "player_seat": 0, 
        "discard_tile": -1, # 117
        "drawn_tile": 47, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 53, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 132, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 鸣牌
    {
        # 下家鸣牌
        "signal": Game.OTHER_CALL, 
        "player_seat": 1, 
        "discard_tile": -1, 
        "drawn_tile": -1, 
        "meld": Meld(meld_type=Meld.PON, 
                     tiles=[132,133,134], opened=True, called_tile=132, who=1, from_who=2), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 126, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 122, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    ########## 第十四巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 29, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
     ########## 鸣牌
    {
        # 下家鸣牌
        "signal": Game.OTHER_CALL, 
        "player_seat": 1, 
        "discard_tile": -1, 
        "drawn_tile": -1, 
        "meld": Meld(meld_type=Meld.PON, 
                     tiles=[29,30,31], opened=True, called_tile=29, who=1, from_who=3), 
        "new_dora_tile": -1
    },{
        # 下家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 1, 
        "discard_tile": 35, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },{
        # 对家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 2, 
        "discard_tile": 113, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
     ########## 鸣牌
    {
        # 上家鸣牌
        "signal": Game.OTHER_CALL, 
        "player_seat": 1, 
        "discard_tile": -1, 
        "drawn_tile": -1, 
        "meld": Meld(meld_type=Meld.PON, 
                     tiles=[113,114,115], opened=True, called_tile=113, who=3, from_who=2), 
        "new_dora_tile": -1
    },
    ########## 第十五巡
    {
        # 上家打牌
        "signal": Game.OTHER_DISCARD, 
        "player_seat": 3, 
        "discard_tile": 25, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
    {
        # 下家和了
        "signal": Game.OTHER_WIN, 
        "player_seat": 1, 
        "discard_tile": -1, 
        "drawn_tile": -1, 
        "meld": Meld(), 
        "new_dora_tile": -1
    },
]