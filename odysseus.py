#!/usr/bin/python
# -*- coding: utf-8 -*-

from errbot import botcmd, BotPlugin

__author__ = 'taoistmath'

class Odysseus(BotPlugin):       

    @botcmd
    def hello_odysseus(self, mess, args):
        """ Introduce yourself to Odysseus
        Example: !hello Odysseus
        """
        hello_odysseus = u"Hi there, nice to meet you! I'm Odysseus and I'm here to help you with all your business needs. Type '!help Odysseus' at any time to see what I can do. If this is our first time meeting I suggest you take the guided tour by typing ‘!tour’ or ‘Odysseus, tour'. You can also type ‘!help GuidedTour’ to see the outline of the tour topics. If you have any questions or suggestions please reach out to me in my chat room 'Ithaca'."

        return hello_odysseus

    @botcmd
    def whoareyou(self, mess, args):
        """ Tells you who Odysseus is
        Example: !whoareyou
        """
        whoiam = u"I'm Odysseus, the hero of Homer's Odyssey and also your local ChatOps Bot. There have been many famous people named after me, including President Ulysses S. Grant, who used to work for Dun and Bradstreet as well. Why am I named Odysseus? Type '!why Odysseus' to find out more."

        return whoiam

    @botcmd
    def why_odysseus(self, mess, args):
        """ Why was the name Odysseus chosen
        Example: !why Odysseus
        """
        why_odysseus = u"My name, Odysseus, means 'trouble' in Greek, as is often the case in my wanderings. My heroic trait is my metis, or 'cunning intelligence' and I am often described as the 'Peer of Zeus in Counsel'. This intelligence is most often manifested by my use of disguise and deceptive speech. My most evident flaw is that of my arrogance and my pride, or hubris. - Wikipedia"

        return why_odysseus

    @botcmd
    def devops_calendar(self, mess, args):
        return 'https://calendar.google.com/calendar/embed?src=h0soenb4ge2ssak4fvc2neq3kc%40group.calendar.google.com&ctz=America/Los_Angeles"'
        
