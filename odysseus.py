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
        hello_odysseus = "Hi there, nice to meet you! I'm Odysseus and I'm here to help you with all your business needs. Type '!help Odysseus' at any time to see what I can do. If this is our first time meeting I suggest you take the guided tour by typing ‘!tour’ or ‘Odysseus, tour'. You can also type ‘!help GuidedTour’ to see the outline of the tour topics. If you have any questions or suggestions please reach out to me in my chat room 'Ithica'."

        return hello_odysseus

    @botcmd
    def whoareyou(self, mess, args):
        """ Tells you who Odysseus is
        Example: !whoareyou
        """
        whoiam = "I'm Odysseus, the hero of Homer's Odyssey and also your local ChatOps Bot. There have been many famous people named after me, including President Ulysses S. Grant, who used to work for Dun and Bradstreet as well. Why am I named Odysseus? Type '!why Odysseus' to find out more."

        return whoiam

    @botcmd
    def why_odysseus(self, mess, args):
        """ Why was the name Odysseus chosen
        Example: !why Odysseus
        """
        why_odysseus = " My name, Odysseus, means 'trouble' in Greek, as is often the case in my wanderings. My heroic trait is my metis, or 'cunning intelligence' and I am often described as the 'Peer of Zeus in Counsel'. This intelligence is most often manifested by my use of disguise and deceptive speech. My most evident flaw is that of my arrogance and my pride, or hubris. - Wikipedia"

        return why_odysseus

    @botcmd
    def available_commands(self, mess, args):
        """ List of available bot commands
        Example: !available commands
        """
        return_list = ''
        
        available_commands = [
        'Slash Commands: Slash commands start with "/" and are room specific only, HipChat Admins can add these to your room(s)',
        '#',
        'Bang Commands: Bang commands start with "!" and are Odysseus commands. These can be used in rooms where Odysseus is present or when speaking directly to Odysseus. Odysseus Admins can add Odysseus to your room(s)',
        '#',
        '!plugin reload Odysseus: Reload the Odysseus plugin, do this from time to time to stay up to date on all the latest changes.',
        '#',
        '!help: Gives you a list of available plugins. !help <plugin> will give you the plugins available commands', 
        '#',
        '!status: Gives the status of all available commands', 
        '#',
        '/sassy: Sassy gets stuff for you. Images, memes, weather, videos, info, whatever.', 
        '#',
        '/pol: You have a question. You know the options. You want input. Your team votes. Polly declares the winner!', 
        '#',
        '/howdoi: Instant answers to your coding question in HipChat',
        '#',
        '/standup: Standup likes to listen and it has a good memory. Add your standup status. Standup will remember! Great for remote teams.' 
        ]
        for command in available_commands:
            return_list = return_list + command + '\n'
        return return_list
