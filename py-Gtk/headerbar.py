import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="this will be removed")
        self.set_border_width(10)

        # HeaderBar
        headerbar = Gtk.HeaderBar()
        headerbar.set_title("Music Player")
        headerbar.props.show_close_button = True
        self.set_titlebar(headerbar)

        # CD Icon Button
        cd_button = Gtk.Button()
        # Create a Gio themed icon 
        cd_icon = Gio.ThemedIcon(name="gnome-dev-cdrom-audio")
        # Extract the image to a button size
        image = Gtk.Image.new_from_gicon(cd_icon, Gtk.IconSize.BUTTON)
        cd_button.add(image)
        headerbar.pack_end(cd_button)

        # Box with packed left right arrow buttons
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box.get_style_context(), "linked")
        headerbar.pack_start(box)

        left_button = Gtk.Button()
        # Left Arrow Button
        left_arrow = Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE)
        left_button.add(left_arrow)
        box.add(left_button)

        right_button = Gtk.Button()
        right_arrow = Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE)
        right_button.add(right_arrow)
        box.add(right_button)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()

        

