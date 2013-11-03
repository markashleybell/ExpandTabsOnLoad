import os
import re
import sublime
import sublime_plugin


class ExpandTabsOnLoad(sublime_plugin.EventListener):
    # Run ST's 'expand_tabs' command when opening a file,
    # only if there are any tab characters in the file
    def on_load(self, view):
        expand_tabs = view.settings().get("expand_tabs_on_load", False)
        if expand_tabs and view.find("\t", 0):
            view.run_command("expand_tabs")
            tab_size = view.settings().get("tab_size", 0)
            message = "Converted tab characters to {0} spaces".format(tab_size)
            sublime.status_message(message)
