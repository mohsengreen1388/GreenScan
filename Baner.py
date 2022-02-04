from abc import ABCMeta, abstractmethod
from Color import Color as color


class BanerInterface(ABCMeta):

    @abstractmethod
    def printBaner(self):
        pass


class BanerNmap(BanerInterface):

    def printBaner(self):
        print(
            "''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n"
            ",                              Nmap search scan                                   ,\n"
            ",  #########################################################################      ,\n"
            ",  #  1  #   port scan                                                     #      ,\n"
            ",  #  2  #   port scan no ping                                             #       ,\n"
            ",  #  3  #   network scan 192.168.1.0                                      #      , \n"
            ",  #########################################################################      ,\n"
            ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n"
        )


class BanerMain(BanerInterface):

    def printBaner(self):

        print(color.CRED2 + r"""
                            ,GreenScan,
                           /(        )`
                           \ \___   / |
                           /- _  `-/  '
                           (/\/ \ \   /\
                           / /   | `    
                           O O   ) /    |
                           `-^--'`<     '
                           (_.)  _  )   /
                            .___/`    /
                             `-----' /
                     <----.     / __   \
                     <----|====O)))==) \) /====
                     <----'  `--' `.__,' \ 
                                |        |
                                 \       /
                          ______( (_  / \______
                         ,'  ,-----'   |        \
                         `--{__________)        \/

                    """ + color.CEND)

        print(
            color.CGREEN +
            "''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\n"
            ",                              List software scan                                 ,\n"
            ",  #########################################################################      ,\n"
            ",  #  1  #   nmap scan                                                     #      ,\n"
            ",  #  2  #   ping target                                                   #      , \n"
            ",  #########################################################################      ,\n"
            ",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,\n"
        )


class Baner:
    baner = None

    def __init__(self, BanerInterface):
        self.baner = BanerInterface
        self.baner.printBaner(self)
