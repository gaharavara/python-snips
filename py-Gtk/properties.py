import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

window = Gtk.Window()
label = Gtk.Label()
# We have a bunch of set methods to set various properties
# and play with the widget
label.set_label("label name")
label.set_angle(30)
window.add(label)

# We have get properties to retrieve and view the properties
# of the widget
print(label.get_properties("angle"))

window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
