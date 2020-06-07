from uiautomator3D.TDtotal import login_to_game3d

# 初始化游戏登录
ltg = login_to_game3d()

# 3d游戏-3星玩法系列
ltg.game_3d_basic()
ltg.game_3d_3star_direct_selection_single()
ltg.game_3d_3star_direct_selection_sum()
ltg.game_3d_3star_group_selection_3snigle()
ltg.game_3d_3star_group_selection_3duplex()
ltg.game_3d_3star_group_selection_6snigle()
ltg.game_3d_3star_group_selection_6duplex()
ltg.game_3d_3star_group_selection_mix_duplex()
ltg.game_3d_3star_group_selection_sum_duplex()

# 3d游戏-2星玩法系列
# ltg.game_3d_2star_top2_direct_duplex()
# ltg.game_3d_2star_top2_direct_single()
# ltg.game_3d_2star_last2_direct_duplex()
# ltg.game_3d_2star_last2_direct_single()
# ltg.game_3d_2star_top2_group_single()
# ltg.game_3d_2star_top2_group_duplex()
# ltg.game_3d_2star_last2_group_single()
# ltg.game_3d_2star_last2_group_duplex()

##定位胆
# ltg.position()
#不定位
# ltg.random_postion_1()
# ltg.random_postion_2()
#大小单双
# ltg.dxds_top2()
# ltg.dxds_last2()

#娱乐城
# ltg.gametown_3D_position_1()
# ltg.gametown_3d_duplex_1()
# ltg.gametown_3d_positon_2()
# ltg.gametown_3d_duplex_2()
# ltg.gametown_3d_sum_2()
# ltg.gametown_3d_position_3()
# ltg.gametown_3d_deplex_3()
# ltg.gametown_3d_sum_3()
