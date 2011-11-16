# Copyright (c) 2011 Matthias Matousek <m@tou.io>
# 
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
# 
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

import socket, logging, sys
from threading import Thread

class IrcBot(Thread):

    def __init__(self, server, nick, port=6667):
        # set up the data
        self.server = server
        self.port = port
        self.nick = nick

        # we need a socket to connect to the irc server
        self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    def run(self):
        try:
            logging.info('trying to connect to %s:%d' % (self.server, self.port))
            self.sock
            logging.info('connected to %s:%d' % (self.server, self.port))
        except:
            logging.fatal('unable to connect to %s:%d' % (self.server, self.port))
            sys.exit(1)




