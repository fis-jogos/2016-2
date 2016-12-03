import argparse
import pong_game
from pong_game import __version__


def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser('pong-game')
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version)
    return parser

def main(args=None):
    """
    Main entry point for your project.

    Args:
        args : list
            A of arguments as if they were input in the command line. 
            Leave it None to use sys.argv.
    """

    parser = get_parser()
    args = parser.parse_args(args)
    
    # Roda jogo!
    from pong_game.pong import start_game
    start_game()

if __name__ == '__main__':
    main()
    
