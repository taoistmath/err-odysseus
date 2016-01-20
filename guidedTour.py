#!/usr/bin/python
# -*- coding: utf-8 -*-

from errbot import botcmd, BotPlugin

__author__ = 'taoistmath'

class GuidedTour(BotPlugin):

    @botcmd
    def tour(self, mess, args):
        """ Starts the guided tour
        Example: !tour
        """
        tour = u"Welcome to the Guided Tour! For starters let me introduce you to the two types of commands I will accept: Slash commands and Bang Commands. Type ‘!slash’ to learn more about Slash Commands or ‘!bang’ to learn more about Bang Commands."

        return tour

    @botcmd
    def slash(self, mess, args):
        """ Tells you about using Slash commands
        Example: !slash
        """
        slash = u"Slash ‘/’ commands are Slack Integration commands.  Create your own private chat room by clicking the plus (+) next to CHANNELS then give your room a name and set to Private. Finally, click 'Create channel'. Once there, type ‘/giphy you’re awesome’ because well…you’re awesome!"

        return slash

    @botcmd
    def bang(self, mess, args):
        """ Tells you about using Bang commands
        Example: !bang
        """
        bang = u"Bang ‘!’ commands are Odysseus Bot commands and are available when chatting with me directly or in any room in which I am a member.  You can also type 'Odysseus' in place of the '!' if you'd like to be more formal. Type ‘!status’ to see a list of all the plugins that are available. Type ‘Odysseus, help <Plugin_name>’ to see what each plugin can do. When you’re done exploring type ‘!continue tour’."

        return bang

    @botcmd
    def continue_tour(self, mess, args):
        """ List of available bot commands
        Example: !available commands
        """
        continue_tour = u"Welcome back to the tour! Now that you know how to interact with the different types of bots let’s take a look at the resources that I can provide. Type ‘!human resources’ to see available links related to HR and Benefits. If you’re an Engineer type ‘!NewDevSetup’ to start configuring your machine."

        return continue_tour

    @botcmd
    def human_resources(self, mess, args):
        """ List of Human Resources references
        Example: !human resources
        """
        return_list = ''
        
        human_resources = [
        u'Fidelity Benefits: https://nb.fidelity.com/public/nb/dnb/home',
        u'#',
        ]
        for resource in human_resources:
            return_list = return_list + resource + '\n'
        return return_list

    @botcmd
    def newdevsetup(self, mess, args):
        """ List of New Dev references
        Example: !newdevsetup
        """
        newdevsetup = u"Welcome to the team! First things last, we have to finalize getting your machine set up. Log into Jira and visit our setup page: https://dunandb.jira.com/wiki/display/AUTOTEST/New+New+Developer+Documentation"

        return newdevsetup
