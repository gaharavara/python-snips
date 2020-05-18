import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="stack and stack_switcher")
        self.set_border_width(10)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(box)

        # Stack
        stack = Gtk.Stack()
        # Put some cool transition effects
        stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stack.set_transition_duration(2000)

        # Label for one tab
        label = Gtk.Label("This is stack area 1")
        label.set_markup("<big>OMG!</big>")
        # Adding the label to the stack
        # params: widget to add, refernece name to be used in code
        # title of the stack to be displayed
        stack.add_titled(label, "a_label", "Big Label")

        # CheckButton for the second tab
        checkbutton = Gtk.CheckButton("Do Not Check Me")
        stack.add_titled(checkbutton, "a_checkbutton","Check Button")

        # StackSwitcher
        stackswitcher = Gtk.StackSwitcher()
        # Setting stack
        stackswitcher.set_stack(stack)
        # Now in the vertically oriented box add stackswitcher and stack
        box.pack_start(stackswitcher, True, True, 0)
        box.pack_start(stack, True, True, 0)

window = MainWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
