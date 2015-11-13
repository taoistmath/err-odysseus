from errbot import botcmd, BotPlugin

__author__ = 'taoistmath'

class Odysseus(BotPlugin):

    @botcmd
    def whoareyou(self, mess, args):
        """ tells you who Odysseus is
        Example: !whoareyou
        """
        whoiam = ("My name, Odysseus, means 'trouble' in Greek, as is often the case in my wanderings. My heroic trait is my metis, or 'cunning intelligence': I am often described as the 'Peer of Zeus in Counsel'. This intelligence is most often manifested by my use of disguise and deceptive speech. My most evident flaw is that of my arrogance and my pride, or hubris.")

        return whoiam