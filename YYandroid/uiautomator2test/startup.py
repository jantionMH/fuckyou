from UItest.runtest import choosefastthree
from Utility.emailreport import htmlemail
from Utility.ftpfile import new_dir_buid, upload_Mp4, upload_zipfile_ftp
from Utility.judge import get_emial_html
from Utility.zipsource import upgrade_zipfile
from uiautomator2test.TDtotal import login_to_game3d
from uiautomator2test.PK10luckyairship import Luckship
from uiautomator2test.elevenchoosefive11_5 import login_to_11c5
from uiautomator2test.fast3UI2 import Anhuifast3

from uiautomator2test.shicai import M65
from uiautomator2test.marksix import HongkongMarksix
import sys, time

r = '断点再执行\n'
r1 = '模块执行失败\n'


def write_logfile(s):
    print('30s后重启')
    time.sleep(30)

    with open('../data/result.csv', mode='a') as f:
        f.write(s)


def read_logfile():
    with open('../data/result.csv') as f:
        flines = f.readlines()
        for i in flines:
            defname = i.strip().split('.')[1]
            write_logfile(defname + '\n')


def excute3d_3star():
    # 3d游戏-3星玩法系列
    try:
        ltg = login_to_game3d()
        ltg.game_3d_basic()
    except:

        write_logfile('game_3d_basic' + r)
        ltg = login_to_game3d()

    try:
        ltg.game_3d_3star_direct_selection_single()
    except:

        write_logfile('game_3d_3star_direct_selection_single' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_3star_direct_selection_sum()
    except:

        write_logfile('game_3d_3star_direct_selection_sum' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_3star_group_selection_3snigle()
    except:

        write_logfile('game_3d_3star_group_selection_3snigle' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_3star_group_selection_3duplex()
    except:

        write_logfile('game_3d_3star_group_selection_3duplex' + r)


def excute3d_3star_half():
    try:
        time.sleep(30)
        ltg = login_to_game3d()
        ltg.game_3d_3star_group_selection_6snigle()
    except:

        write_logfile('game_3d_3star_group_selection_6snigle' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_3star_group_selection_6duplex()
    except:

        write_logfile('game_3d_3star_group_selection_6duplex' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_3star_group_selection_mix_duplex()
    except:

        write_logfile('game_3d_3star_group_selection_mix_duplex' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_3star_group_selection_sum_duplex()
    except:

        write_logfile('game_3d_3star_group_selection_sum_duplex' + r)



def excute3d_2star():
    # 3d游戏-2星玩法系列
    try:
        time.sleep(30)
        ltg = login_to_game3d()
        ltg.game_3d_2star_top2_direct_duplex()
    except:

        write_logfile('game_3d_2star_top2_direct_duplex' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_2star_top2_direct_single()
    except:

        write_logfile('game_3d_2star_top2_direct_single' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_2star_last2_direct_duplex()
    except:

        write_logfile('game_3d_2star_last2_direct_duplex' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_2star_last2_direct_single()
    except:

        write_logfile('game_3d_2star_last2_direct_single' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_2star_top2_group_single()
    except:

        write_logfile('game_3d_2star_top2_group_single' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_2star_top2_group_duplex()
    except:

        write_logfile('game_3d_2star_top2_group_duplex' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_2star_last2_group_single()
    except:

        write_logfile('game_3d_2star_last2_group_single' + r)
        ltg = login_to_game3d()

    try:

        ltg.game_3d_2star_last2_group_duplex()
    except:

        write_logfile('game_3d_2star_last2_group_duplex' + r)



def excute_3d_random():
    try:
        ##定位胆
        ltg = login_to_game3d()
        ltg.position()

    except:
        write_logfile('position' + r)
        ltg = login_to_game3d()

    try:

        # 不定位

        ltg.random_postion_1()
    except:
        write_logfile('random_postion_1' + r)
        ltg = login_to_game3d()

    try:

        ltg.random_postion_2()
    except:
        write_logfile('random_postion_2' + r)
        ltg = login_to_game3d()

    try:
        # 大小单双

        ltg.dxds_top2()
    except:
        write_logfile('dxds_top2' + r)
        ltg = login_to_game3d()

    try:

        ltg.dxds_last2()
    except:
        write_logfile('dxds_last2' + r)



def excute_3d_gametown():
    try:
        # 娱乐城
        ltg = login_to_game3d()
        ltg.gametown_3D_position_1()
    except:
        write_logfile('gametown_3D_position_1' + r)
        ltg = login_to_game3d()

    try:

        ltg.gametown_3d_duplex_1()
    except:
        write_logfile('gametown_3d_duplex_1' + r)
        ltg = login_to_game3d()

    try:

        ltg.gametown_3d_positon_2()
    except:
        write_logfile('gametown_3d_positon_2' + r)
        ltg = login_to_game3d()

    try:

        ltg.gametown_3d_duplex_2()
    except:
        write_logfile('gametown_3d_duplex_2' + r)
        ltg = login_to_game3d()

    try:

        ltg.gametown_3d_sum_2()
    except:
        write_logfile('gametown_3d_sum_2' + r)
        ltg = login_to_game3d()

    try:

        ltg.gametown_3d_position_3()
    except:
        write_logfile("gametown_3d_position_3" + r)
        ltg = login_to_game3d()

    try:

        ltg.gametown_3d_deplex_3()
    except:
        write_logfile('gametown_3d_deplex_3' + r)
        ltg = login_to_game3d()

    try:

        ltg.gametown_3d_sum_3()
    except:
        write_logfile('gametown_3d_sum_3' + r)



def excute_PK10():
    # PK10-幸运飞艇

    try:
        L = Luckship()
        L.top5_position()
    except:
        write_logfile("top5_position" + r)
        L = Luckship()
    try:
        L.top5_direct_duplex()
    except:
        write_logfile('top5_direct_duplex' + r)
        L = Luckship()

    try:
        L.last5_position()
    except:
        write_logfile('last5_position' + r)
        L = Luckship()

    try:
        L.top4_direct_duplex()
    except:
        write_logfile('top4_direct_duplex' + r)
        L = Luckship()

    try:
        L.top3_direct_duplex()
    except:
        write_logfile('top3_direct_duplex' + r)
        L = Luckship()

    try:
        L.top2_direct_duplex()
    except:
        write_logfile('top2_direct_duplex' + r)
        L = Luckship()

    try:
        L.top1_direct_duplex()
    except:
        write_logfile('top1_direct_duplex' + r)
        L = Luckship()

    try:
        L.dxds()
    except:
        write_logfile('dxds' + r)
        L = Luckship()

    try:
        L.TG_all()
    except:
        write_logfile('TG_all' + r)


def excute_pk10_gametown():
    try:
        time.sleep(30)
        L = Luckship()
        L.gametown_PK10_two_sides()
    except:
        write_logfile('gametown_PK10_two_sides' + r)
        L = Luckship()

    try:
        L.gametown_PK10_guess_sum()
    except:
        write_logfile('gametown_PK10_guess_sum' + r)
        L = Luckship()

    try:
        L.gametown_PK10_champion_tenth()
    except:
        write_logfile('gametown_PK10_champion_tenth' + r)
        L = Luckship()

    try:
        L.gametown_luckship_TG()
    except:
        write_logfile('gametown_luckship_TG' + r)


def excute_11c5():
    # 11-5

    try:
        lt_11c5 = login_to_11c5()
        lt_11c5.top3_direct_duplex()
    except:
        write_logfile("top3_direct_duplex" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.top3_direct_single()
    except:
        write_logfile("top3_direct_single" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.top3_direct_single()

    except:
        write_logfile("top3_direct_single" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.top3_group_duplex()

    except:
        write_logfile("top3_group_duplex" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.top3_group_single()


    except:
        write_logfile("top3_group_single" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.top2_direct_duplex()



    except:
        write_logfile("top2_direct_duplex" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.top2_direct_single()


    except:
        write_logfile("top2_direct_single" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.top2_group_duplex()

    except:
        write_logfile("top2_group_duplex" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.top2_group_single()


    except:
        write_logfile("top2_group_single" + r)
        lt_11c5 = login_to_11c5()

    try:

        lt_11c5.position_11c5()


    except:
        write_logfile("position_11c5" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.random_position_11c5()



    except:
        write_logfile("random_position_11c5" + r)


def excute_11c5_gametown():
    try:
        lt_11c5 = login_to_11c5()
        lt_11c5.gametown_11c5_two_sides()


    except:
        write_logfile("gametown_11c5_two_sides" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.gametown_11c5_ball_1()


    except:
        write_logfile("gametown_11c5_ball_1" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.gametown_11c5_ball_2()


    except:
        write_logfile("gametown_11c5_ball_2" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.gametown_11c5_ball_3()

    except:
        write_logfile("gametown_11c5_ball_3" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.gametown_11c5_ball_4()


    except:
        write_logfile("gametown_11c5_ball_4" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.gametown_11c5_ball_5()


    except:
        write_logfile("gametown_11c5_ball_5" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.gametown_11c5_ball_random()


    except:
        write_logfile("gametown_11c5_ball_random" + r)
        lt_11c5 = login_to_11c5()

    try:
        lt_11c5.gametown_11c5_ball_TG()



    except:
        write_logfile("gametown_11c5_ball_TG" + r)
        lt_11c5 = login_to_11c5()


def excute_M6_5_5star_4star():
    try:
        M = M65()
        M.star5_driect_duplex()

    except:
        write_logfile("star5_driect_duplex" + r)
        M = M65()

    try:
        M.star5_driect_selection()



    except:
        write_logfile("star5_driect_selection" + r)
        M = M65()

    try:
        M.star5_direct_single()


    except:
        write_logfile("star5_direct_single" + r)
        M = M65()

    try:

        M.star5_group_120()


    except:
        write_logfile("star5_group_120" + r)
        M = M65()

    try:
        M.star5_group_60()

    except:
        write_logfile("star5_group_60" + r)
        M = M65()

    try:
        M.star5_group_30()


    except:
        write_logfile("star5_group_30" + r)
        M = M65()

    try:
        M.star5_group_20()

    except:
        write_logfile("star5_group_20" + r)
        M = M65()

    try:
        M.star5_group_10()


    except:
        write_logfile("star5_group_10" + r)
        M = M65()

    try:
        M.star5_group_5()


    except:
        write_logfile("star5_group_5" + r)
        M = M65()

    try:
        M.star5_other_TGsum()


    except:
        write_logfile("star5_other_TGsum" + r)
        M = M65()

    try:
        M.star5_other_dxds()

    except:
        write_logfile("star5_other_dxds" + r)
        M = M65()

    try:
        M.top4_direct_duplex()


    except:
        write_logfile("top4_direct_duplex" + r)
        M = M65()

    try:
        M.top4_direct_single()


    except:
        write_logfile("top4_direct_single" + r)
        M = M65()

    try:
        M.top4_direct_selection()


    except:
        write_logfile("top4_direct_selection" + r)
        M = M65()

    try:
        M.top4_group_slection24()


    except:
        write_logfile("top4_group_slection24" + r)
        M = M65()

    try:
        M.top4_group_slection12()

    except:
        write_logfile("top4_group_slection12" + r)
        M = M65()

    try:
        M.top4_group_slection6()



    except:
        write_logfile("top4_group_slection6" + r)
        M = M65()

    try:

        M.top4_group_slection4()

    except:
        write_logfile("top4_group_slection4" + r)


def excute_M6_5_top3():
    try:
        M = M65()
        M.top3_direct_duplex()


    except:
        write_logfile("top3_direct_duplex" + r)
        M = M65()

    try:

        M.top3_direct_single()


    except:
        write_logfile("top3_direct_single" + r)
        M = M65()

    try:

        M.top3_direct_selection()


    except:
        write_logfile("top3_direct_selection" + r)
        M = M65()

    try:

        M.top3_direct_span()


    except:
        write_logfile("top3_direct_span" + r)
        M = M65()

    try:
        M.top3_group3_duplex()


    except:
        write_logfile("top3_group3_duplex" + r)
        M = M65()

    try:
        M.top3_group3_single()

    except:
        write_logfile("top3_group3_single" + r)
        M = M65()

    try:
        M.top3_group6_duplex()



    except:
        write_logfile("top3_group6_duplex" + r)
        M = M65()

    try:
        M.top3_group6_single()

    except:
        write_logfile("top3_group6_single" + r)
        M = M65()

    try:
        M.top3_group_mix()


    except:
        write_logfile("top3_group_mix" + r)
        M = M65()

    try:
        M.top3_group_sum()


    except:
        write_logfile("top3_group_sum" + r)

def excute_M6_5_mid3():
    try:
        M = M65()
        M.mid3_direct_duplex()


    except:
        write_logfile("mid3_direct_duplex" + r)
        M = M65()

    try:
        M.mid3_direct_single()


    except:
        write_logfile("mid3_direct_single" + r)
        M = M65()

    try:
        M.mid3_direct_selection()


    except:
        write_logfile("mid3_direct_selection" + r)
        M = M65()

    try:
        M.mid3_direct_span()

    except:
        write_logfile("mid3_direct_span" + r)
        M = M65()

    try:
        M.mid3_direct_sum()



    except:
        write_logfile("mid3_direct_sum" + r)
        M = M65()

    try:
        M.mid3_group3_duplex()



    except:
        write_logfile("mid3_group3_duplex" + r)
        M = M65()

    try:
        M.mid3_group3_single()



    except:
        write_logfile("mid3_group3_single" + r)
        M = M65()

    try:
        M.mid3_group6_duplex()



    except:
        write_logfile("mid3_group6_duplex" + r)
        M = M65()

    try:
        M.mid3_group6_single()


    except:
        write_logfile("mid3_group6_single" + r)
        M = M65()

    try:
        M.mid3_group_mix()




    except:
        write_logfile("mid3_group_mix" + r)
        M = M65()

    try:
        M.mid3_group_sum()




    except:
        write_logfile("mid3_group_sum" + r)

def excute_M6_5_last3():
    try:
        M = M65()
        M.last3_direct_duplex()


    except:
        write_logfile("last3_direct_duplex" + r)
        M = M65()

    try:
        M.last3_direct_single()



    except:
        write_logfile("last3_direct_single" + r)
        M = M65()

    try:
        M.last3_direct_selection()



    except:
        write_logfile("last3_direct_selection" + r)
        M = M65()

    try:
        M.last3_direct_span()



    except:
        write_logfile("last3_direct_span" + r)
        M = M65()

    try:
        M.mid3_direct_sum()



    except:
        write_logfile("mid3_direct_sum" + r)
        M = M65()

    try:
        M.last3_group3_duplex()




    except:
        write_logfile("last3_group3_duplex" + r)
        M = M65()

    try:
        M.last3_group3_single()



    except:
        write_logfile("last3_group3_single" + r)
        M = M65()

    try:
        M.last3_group6_duplex()


    except:
        write_logfile("last3_group6_duplex" + r)
        M = M65()

    try:
        M.last3_group6_single()



    except:
        write_logfile("last3_group6_single" + r)
        M = M65()

    try:
        M.last3_group_mix()




    except:
        write_logfile("last3_group_mix" + r)
        M = M65()

    try:
        M.last3_group_sum()


    except:
        write_logfile("last3_group_sum" + r)


def excute_M6_5_top2_last2():
    try:
        M = M65()
        M.top2_direct_duplex()



    except:
        write_logfile("top2_direct_duplex" + r)
        M = M65()

    try:
        M.top2_direct_single()



    except:
        write_logfile("top2_direct_single" + r)
        M = M65()

    try:
        M.top2_direct_sum()



    except:
        write_logfile("top2_direct_sum" + r)
        M = M65()

    try:
        M.top2_group_duplex()



    except:
        write_logfile("top2_group_duplex" + r)
        M = M65()

    try:
        M.top2_group_single()


    except:
        write_logfile("top2_group_single" + r)
        M = M65()

    try:
        M.top2_group_sum()




    except:
        write_logfile("top2_group_sum" + r)
        M = M65()

    try:

        M.last2_direct_duplex()


    except:
        write_logfile("last2_direct_duplex" + r)
        M = M65()

    try:
        M.last2_direct_single()




    except:
        write_logfile("last2_direct_single" + r)
        M = M65()

    try:
        M.last2_direct_sum()



    except:
        write_logfile("last2_direct_sum" + r)
        M = M65()

    try:
        M.last2_group_duplex()


    except:
        write_logfile("last2_group_duplex" + r)
        M = M65()

    try:
        M.last2_group_single()



    except:
        write_logfile("last2_group_single" + r)
        M = M65()

    try:
        M.last2_group_sum()




    except:
        write_logfile("last2_group_sum" + r)


def excute_M6_5_postion_random_5star_top4_last4():
    try:
        M = M65()
        M.M6_5_position()



    except:
        write_logfile("M6_5_position" + r)
        M = M65()

    try:
        M.random_position_5star_1()



    except:
        write_logfile("random_position_5star_1" + r)
        M = M65()

    try:
        M.random_position_5star_2()



    except:
        write_logfile("random_position_5star_2" + r)
        M = M65()

    try:
        M.random_position_5star_3()



    except:
        write_logfile("random_position_5star_3" + r)
        M = M65()

    try:
        M.random_position_top4_1()


    except:
        write_logfile("random_position_top4_1" + r)
        M = M65()

    try:
        M.random_position_last4_1()



    except:
        write_logfile("random_position_last4_1" + r)


def excute_M6_5_random_top3_mid3_last3():
    try:
        M = M65()
        M.random_position_top3_1()


    except:
        write_logfile("random_position_top3_1" + r)
        M = M65()

    try:
        M.random_position_top3_2()




    except:
        write_logfile("random_position_top3_2" + r)
        M = M65()

    try:
        M.random_position_last3_1()



    except:
        write_logfile("random_position_last3_1" + r)
        M = M65()

    try:
        M.random_position_last3_2()


    except:
        write_logfile("random_position_last3_2" + r)
        M = M65()

    try:
        M.random_position_mid3_1()



    except:
        write_logfile("random_position_mid3_1" + r)
        M = M65()

    try:
        M.random_position_mid3_2()



    except:
        write_logfile("random_position_mid3_2" + r)
        M = M65()


def random_choose2_3_4():
    try:
        M = M65()

        M.random2_direct_duplex()


    except:
        write_logfile("random2_direct_duplex" + r)
        M = M65()

    try:
        M.random2_dricet_sum()




    except:
        write_logfile("random2_dricet_sum" + r)
        M = M65()

    try:
        M.random2_group_duplex()


    except:
        write_logfile("random2_group_duplex" + r)
        M = M65()

    try:
        M.random2_group_sum()




    except:
        write_logfile("random2_group_sum" + r)
        M = M65()

    try:
        M.random2_group_single()


    except:
        write_logfile("random2_group_single" + r)
        M = M65()

    try:
        M.random3_direct_duplex()


    except:
        write_logfile("random3_direct_duplex" + r)
        M = M65()

    try:
        M.random3_dircet_sum()

    except:
        write_logfile("random3_dircet_sum" + r)
        M = M65()

    try:
        M.random3_group3_duplex()


    except:
        write_logfile("random3_group3_duplex" + r)
        M = M65()

    try:
        M.random3_group3_single()


    except:
        write_logfile("random3_group3_single" + r)
        M = M65()

    try:
        M.random3_group6_duplex()


    except:
        write_logfile("random3_group6_duplex" + r)
        M = M65()

    try:
        M.random3_group6_single()


    except:
        write_logfile("random3_group6_single" + r)
        M = M65()

    try:
        M.random3_group_mix()


    except:
        write_logfile("random3_group_mix" + r)
        M = M65()

    try:
        M.random3_group_sum()


    except:
        write_logfile("random3_group_sum" + r)
        M = M65()

    try:

        M.random4_driect_duplex()

    except:
        write_logfile("random4_driect_duplex" + r)


def excute_M6_5_gametown():
    try:
        M = M65()
        M.gametown_M6_5_Integration()


    except:
        write_logfile("gametown_M6_5_Integration" + r)
        M = M65()

    try:
        M.gametown_M6_5_TG()


    except:
        write_logfile("gametown_M6_5_TG" + r)
        M = M65()

    try:
        M.gametown_M6_5_ball1_ball5()

    except:
        write_logfile("gametown_M6_5_ball1_ball5" + r)
        M = M65()

    try:
        M.gametown_M6_5_one_in5()


    except:
        write_logfile("gametown_M6_5_one_in5" + r)
        M = M65()

    try:
        M.gametown_M6_5_niuniu()


    except:
        write_logfile("gametown_M6_5_niuniu" + r)


def excute_marksix():
    try:
        HK = HongkongMarksix()
        HK.specialnum()


    except:
        write_logfile("specialnum" + r)
        HK = HongkongMarksix()

    try:
        HK.twosides()


    except:
        write_logfile("twosides" + r)
        HK = HongkongMarksix()

    try:
        HK.colorwave()


    except:
        write_logfile("colorwave" + r)
        HK = HongkongMarksix()

    try:
        HK.special_animal()

    except:
        write_logfile("special_animal" + r)
        HK = HongkongMarksix()

    try:

        HK.head_tail_num()


    except:
        write_logfile("head_tail_num" + r)
        HK = HongkongMarksix()

    try:
        HK.hexiao()


    except:
        write_logfile("hexiao" + r)
        HK = HongkongMarksix()

    try:
        HK.zheng_code()


    except:
        write_logfile("zheng_code" + r)
        HK = HongkongMarksix()

    try:
        HK.zheng_code_te()


    except:
        write_logfile("zheng_code_te" + r)
        HK = HongkongMarksix()

    try:
        HK.zheng_code_1_6()

    except:
        write_logfile("zheng_code_1_6" + r)
        HK = HongkongMarksix()

    try:
        HK.continuou_animal()


    except:
        write_logfile("continuou_animal" + r)
        HK = HongkongMarksix()

    try:
        HK.ptxw()


    except:
        write_logfile("ptxw" + r)
        HK = HongkongMarksix()

    try:
        HK.choose_miss()


    except:
        write_logfile("choose_miss" + r)


def excute_fast3():
    try:
        A = Anhuifast3()
        A.fast3_sum()

    except:
        write_logfile("fast3_sum" + r)
        A = Anhuifast3()
    try:
        A.fast3_dxds()
    except:
        write_logfile("fast3_dxds" + r)
        A = Anhuifast3()

    try:
        A.fast3_same3_general()
    except:
        write_logfile("fast3_same3_general" + r)
        A = Anhuifast3()
    try:
        A.fast3_same3_single()
    except:
        write_logfile("fast3_same3_single" + r)
        A = Anhuifast3()
    try:
        A.fast3_same2_single()
    except:
        write_logfile("fast3_same2_single" + r)
        A = Anhuifast3()

    try:
        A.fast3_same2_duplex()
    except:
        write_logfile("fast3_same2_duplex" + r)


def fast3_half():
    try:
        time.sleep(30)
        A = Anhuifast3()
        A.fast3_diff3()
    except:
        write_logfile("fast3_diff3" + r)
        A = Anhuifast3()
    try:
        A.fast3_diff3_TD()
    except:
        write_logfile("fast3_diff3_TD" + r)
        A = Anhuifast3()
    try:
        A.fast3_diff2()
    except:
        write_logfile("fast3_diff2" + r)
        A = Anhuifast3()
    try:
        A.fast3_diff2_TD()
    except:
        write_logfile("fast3_diff2_TD" + r)
        A = Anhuifast3()
    try:
        A.fast3_continuous3_general()
    except:
        write_logfile("fast3_continuous3_general" + r)


def excute_toal():
    # 11c5
    try:
        excute_11c5()
    except:
        write_logfile('excute_11c5' + r1)
        htmlemail(content='excute_11c5' + r1)
    try:
        excute_11c5_gametown()
    except:
        write_logfile('excute_11c5_gametown' + r1)
        htmlemail(content='excute_11c5_gametown' + r1)

    # 时时彩M6-5游戏
    try:
        excute_M6_5_5star_4star()
    except:
        write_logfile('excute_M6_5_5star_4star' + r1)
        htmlemail(content='excute_M6_5_5star_4star' + r1)

    try:
        excute_M6_5_top3()

    except:
        write_logfile('excute_M6_5_top3' + r1)
        htmlemail(content='excute_M6_5_top3' + r1)
    try:


        excute_M6_5_last3()
    except:
        write_logfile('excute_M6_5_mid3' + r1)
        htmlemail(content='excute_M6_5_mid3' + r1)
    try:


        excute_M6_5_last3()
    except:
        write_logfile('excute_M6_5_last3' + r1)
        htmlemail(content='excute_M6_5_last3' + r1)

    try:

        excute_M6_5_top2_last2()
    except:
        write_logfile('excute_M6_5_top2_last2' + r1)
        htmlemail(content='excute_M6_5_top2_last2' + r1)

    try:
        excute_M6_5_postion_random_5star_top4_last4()


    except:
        write_logfile('excute_M6_5_postion_random_5star_top4_last4' + r1)
        htmlemail(content='excute_M6_5_postion_random_5star_top4_last4' + r1)
    try:
        excute_M6_5_random_top3_mid3_last3()

    except:
        write_logfile('excute_M6_5_random_gametown' + r1)
        htmlemail(content='excute_M6_5_random_gametown' + r1)

    try:
        random_choose2_3_4()
    except:
        write_logfile('random_choose2_3_4' + r1)
        htmlemail(content='random_choose2_3_4' + r1)

    try:

        excute_M6_5_gametown()
    except:
        write_logfile('excute_M6_5_gametown' + r1)
        htmlemail(content='excute_M6_5_gametown' + r1)

    try:
        excute_PK10()
    except:
        write_logfile('excute_PK10' + r1)
        htmlemail(content='excute_PK10' + r1)
    try:
        excute_pk10_gametown()
    except:
        write_logfile('excute_pk10_gametown' + r1)
        htmlemail(content='excute_pk10_gametown' + r1)

    # 3D
    try:
        excute3d_3star()

    except:
        write_logfile('excute3d_3star' + r1)
        htmlemail(content='excute3d_3star' + r1)
    try:
        excute3d_3star_half()

    except:
        write_logfile('excute3d_3star_half' + r1)
        htmlemail(content='excute3d_3star_half' + r1)
    try:

        excute3d_2star()
    except:
        write_logfile('excute3d_2star' + r1)
        htmlemail(content='excute3d_2star' + r1)
    try:

        excute_3d_random()
    except:
        write_logfile('excute_3d_random' + r1)
        htmlemail(content='excute_3d_random' + r1)
    try:
        excute_3d_gametown()
    except:
        write_logfile('excute_3d_gametown' + r1)
        htmlemail(content='excute_3d_gametown' + r1)

    #
    # 六合彩
    try:
        excute_marksix()

    except:
        write_logfile('excute_marksix' + r1)
        htmlemail(content='excute_marksix' + r1)
    try:

        excute_fast3()


    except:
        write_logfile('excute_fast3' + r1)

        htmlemail(content='excute_fast' + r1)
    try:

        fast3_half()

    except:
        write_logfile('excute_fast3_half' + r1)
        htmlemail(content='excute_fast_half' + r1)



try:
    excute_toal()

except:
    htmlemail(content='测试中断')


# 测试完成给我发消息
htmlemail(content='测试完成')
# 生成报告
get_emial_html()
# 压缩打包文件
upgrade_zipfile()
# 在ftp上建立今天的文件夹
new_dir_buid(date='20200615', type='android', key='YY')
new_dir_buid(date='20200615', type='android', key='BB')
# 上传原生文件/压缩文件
upload_zipfile_ftp(date='20200615', type='android', subtype='YY', key='上传视频')
upload_zipfile_ftp(date='20200615', type='android', subtype='YY', key='上传图片')
upload_zipfile_ftp(date='20200615', type='android', subtype='YY', key='上传html')

# 上传完整视频
upload_Mp4(date='20200615', type='android', subtype='YY')
# 发消息给小伙伴，喊他们围观
htmlemail(content='http://autotest.seektopser.com/20200614/android/YY/test_report.html')
