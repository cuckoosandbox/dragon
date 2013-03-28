# Copyright (C) 2010-2013 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import gtk
import random
import gobject

from lib.dragon.common.abstracts import Report

APT_MESSAGES = [
    "APT ALERT!",
]

class APTAlert(Report):

    def run(self, results):
        dialog = gtk.Dialog("Dragon Sandbox", None,
            gtk.DIALOG_DESTROY_WITH_PARENT,
            (gtk.STOCK_OK, gtk.RESPONSE_ACCEPT))
        dialog.resize(300,100)
        dialog.modify_bg(dialog.get_state(), gtk.gdk.Color("red"))

        width, height = dialog.get_size()
        movex = random.randint(100, gtk.gdk.screen_width() - width - 100)
        movey = random.randint(100, gtk.gdk.screen_height() - height -100)
        dialog.move(movex, movey)

        label = gtk.Label()
        #msg = random.choice(APT_MESSAGES)
        msg = "APT ALERT!"
        label.set_markup('<span size="x-large" weight="heavy">{0}</span>'.format(msg));
        dialog.vbox.pack_start(label)
        label.show()

        def timercb(*args, **kwargs):
            if not dialog.get_visible(): return

            gobject.timeout_add(300, timercb)
            if label.get_visible(): label.hide()
            else: label.show()

        def got_response(dialog, code):
            dialog.hide()
            dialog.destroy()

        dialog.connect("response", got_response)
        dialog.show()
        #timercb()
