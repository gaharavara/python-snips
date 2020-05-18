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
        file_button = Gtk.Button("Open File")
        file_button.connect("clicked", self.generate_file_chooser)

        box.add(file_button)

    def generate_file_chooser(self, widget):
        # FileChooserDialog
        file_choser_dialog = Gtk.FileChooserDialog("Select a file", self, Gtk.FileChooserAction.OPEN, ("open", Gtk.ResponseType.OK, "cancel", Gtk.ResponseType.CANCEL))
        # We keep running the dialog until we recieve a response
        response = file_choser_dialog.run()

        if response == Gtk.ResponseType.OK:
            print("User gave ok as response")
            print("Selected File:", file_choser_dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("User gave cancel as response")

        # After handling the revcieved response we destroy the dialog
        file_choser_dialog.destroy()

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

