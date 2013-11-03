import sublime, sublime_plugin, os, re

class ExpandTabsOnLoad(sublime_plugin.EventListener):
    # Run ST's 'expand_tabs' command when opening a file,
    # only if there are any tab characters in the file
    def on_load(self, view):
        if view.settings().get("expand_tabs_on_load", False) and view.find("\t", 0):
            view.run_command("expand_tabs")
            message = "Converted tab characters to {0} spaces".format(view.settings().get("tab_size", 0))
            sublime.status_message(message)