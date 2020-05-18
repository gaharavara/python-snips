import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# create a window
window = Gtk.Window()
# connect delete-event to the window whose callback method is Gtk.main_quit
window.connect("delete-event", Gtk.main_quit)
# show whatever you have created, here Gtk.Window
window.show_all()
# start the main loop of the window which keeps running to display the window
Gtk.main()
