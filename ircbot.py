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

import socket, logging, sys, ircbotconf
from threading import Thread

class IrcBot(Thread):

    def __init__(self, server, nick, user, room, port=6667):
        """Set up the IrcBot by setting necessary fields. """

        Thread.__init__(self)

        # set up the data
        self.server = server
        self.port = port
        self.nick = nick
        self.user = user
        self.room = room

        # we need a socket to connect to the irc server
        self.sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

    def run(self):
        """Starts the bot by connecting to the server and joining a room."""

        try:
            logging.info('trying to connect to %s:%d' % (self.server, self.port))
            self.sock.connect( (self.server, self.port) )
            connected = True
            logging.info('connected to %s:%d' % (self.server, self.port))
        except:
            logging.fatal('unable to connect to %s:%d' % (self.server, self.port))
            sys.exit(1)

        logging.debug('trying to register nick "%s"' %self.nick)
        self.send('NICK %s' % self.nick)

        logging.debug('trying to register user "%s"' %self.user)
        self.send('USER %s' %self.user)

        logging.debug('trying to join room "%s"' %self.room)
        self.send('JOIN %s' % self.room)

        # infinite loop handling data
        while True:
            data = self.sock.recv(4096)

            logging.debug('received %s' % data)

            # stop if empty data is received
            if data == '': 
                logging.info('disconnected')
                break
            
            self.handle(data)
            
    def handle(self, data):
        """Handles received data"""
        pass


    def send(self, data):
        """Sends the given data to the IRC server."""
        self.sock.send( data + '\r\n' )
        logging.debug('sent %s' % data)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    bot = IrcBot(ircbotconf.server, ircbotconf.nick, ircbotconf.user, ircbotconf.room)
    bot.start()

