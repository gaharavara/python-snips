import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Menu Bar")
        self.set_border_width(10)
        box = Gtk.Box()
        self.add(box)

        # PopUp Button
        popup_button = Gtk.Button("Popup")
        popup_button.connect("clicked", self.generate_popup)

        box.add(popup_button)

    def generate_popup(self, widget):
        # PopUp
        popup_dialog = PopUp(self)
        # We keep running the dialog until we recieve a response
        response = popup_dialog.run()

        if response == Gtk.ResponseType.OK:
            print("User gave ok as response")
        elif response == Gtk.ResponseType.CANCEL:
            print("User gave cancel as response")

        # After handling the revcieved response we destroy the popup/dialog
        popup_dialog.destroy()

class PopUp(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Dialog", parent, Gtk.DialogFlags.MODAL)
        self.add_buttons("Ok I Agree", Gtk.ResponseType.OK, "Cancel It", Gtk.ResponseType.CANCEL)

        content_area = self.get_content_area()
        content_area.add(Gtk.Label("This is the content_area of the dialog"))

        self.show_all()

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

