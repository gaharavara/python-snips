import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GObject, GdkPixbuf, Gdk

user_data = [("Akshay", 88, "Actor"),("Luffy", 18, "Pirate"), ("Zoro", 21, "Swordsman")]

class Item(GObject.GObject):
    text = str
    age = GObject.property(type = int)
    profession = GObject.property(type = str)
    pix_buf = GdkPixbuf.Pixbuf
    uri = object

    def __init__(self):
        GObject.GObject.__init__(self)
    def __repr__(self):
        print(text)

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Flow Box")
        self.set_border_width(10)
        self.set_size_request(200,200)
        handle = Gtk.EventBox()
        handle.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], Gdk.DragAction.COPY)
        handle.add(Gtk.Image.new_from_icon_name("open-menu-symbolic", 1))
        self.add(handle)
        
    def create_widget_func(self, item):
        flowbox_child = Gtk.FlowBoxChild()

        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        label1 = Gtk.Label(item.text)
        label2 = Gtk.Label(item.age)
        label3 = Gtk.Label(item.profession)

        box.pack_start(label1, True, True, 0)
        box.pack_start(label2, True, True, 0)
        box.pack_start(label3, True, True, 0)

        flowbox_child.add(box)

        return flowbox_child

    def flowbox_child_activated(self, flowbox, child):
        print("child activated")

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
