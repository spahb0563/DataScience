# import game.sound.echo
#game.sound.echo.echo_test()
import sys
sys.path.append("C:/Pywork/DataScience/pkg_test")

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()
'''
환경변수에서 PYTHONPATH 하고 패키지 경로 위치 잡아주면 잡아온다
'''
from game.sound import *
wav.wav_test()