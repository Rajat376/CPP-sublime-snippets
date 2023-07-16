import sublime
import sublime_plugin


class CtrlAltClickCursorPlugin(sublime_plugin.EventListener):
    def on_text_command(self, view, command_name, args):
        if command_name == "drag_select" and "by" in args and args["by"] == "words" and "additive" in args and args["additive"] and sublime.platform() == "windows":
            # Ctrl+Alt+Click detected when selecting words on Windows
            # Remove the default selection and add a new cursor
            view.sel().clear()
            for region in view.get_regions("ctrl_alt_click_cursors"):
                view.sel().add(region)
            view.erase_regions("ctrl_alt_click_cursors")
            return ("noop", None)
        return None

    def on_post_text_command(self, view, command_name, args):
        if command_name == "drag_select" and "by" in args and args["by"] == "words" and "additive" in args and args["additive"] and sublime.platform() == "windows":
            # Ctrl+Alt+Click detected when selecting words on Windows
            # Store the new cursor position as a region
            region = view.sel()[0]
            regions = view.get_regions("ctrl_alt_click_cursors")
            regions.append(region)
            view.add_regions("ctrl_alt_click_cursors", regions, "string", "", sublime.HIDDEN)
