""" python-libtiepie - Python interface for libtiepie-hw library

Copyright (c) 2024 TiePie engineering

Website: http://www.tiepie.com/LibTiePie

"""

from ctypes import *
from .api import api
from .const import *
from .library import library
from .exceptions import InvalidIndexError
from .server import Server


class NetworkServers(object):
    """"""

    def __getitem__(self, index):
        try:
            return self.get_by_index(index)
        except (InvalidIndexError):
            raise IndexError()

    def __len__(self):
        return self.count

    def add(self, url):
        """ Add a server to the list of servers.

        :param url: XXX
        :returns: Instance of :class:`.Server`
        .. version added:: 1.0
        """
        url = url.encode('utf-8')
        handle = c_uint32(0)
        result = api.tiepie_hw_network_servers_add(url, STRING_LENGTH_NULL_TERMINATED, byref(handle))
        library.check_last_status_raise_on_error()
        return Server(handle.value) if result else None

    def remove(self, url, force):
        """ Remove a server from the list of servers.

        :param url: Pointer to URL character buffer.
        :param force: If ``True`` all open devices are closed, if ``False`` remove only succeeds if no devices are open.
        :returns: ``True`` if removed successfully, ``False`` otherwise.
        .. version added:: 1.0
        """
        url = url.encode('utf-8')
        force = BOOL_TRUE if force else BOOL_FALSE
        result = api.tiepie_hw_network_servers_remove(url, STRING_LENGTH_NULL_TERMINATED, force)
        library.check_last_status_raise_on_error()
        return result != BOOL_FALSE

    def _get_count(self):
        """ Number of servers available. """
        value = api.tiepie_hw_network_servers_get_count()
        library.check_last_status_raise_on_error()
        return value

    def get_by_index(self, index):
        """ Get the handle of a server, based on its index in the list of servers.

        :param index: A server index, ``0`` .. tiepie_hw_network_servers_get_count() - 1.
        :returns: Instance of :class:`.Server`.
        .. version added:: 1.0
        """
        result = api.tiepie_hw_network_servers_get_by_index(index)
        library.check_last_status_raise_on_error()
        return Server(result)

    def get_by_url(self, url):
        """ Get the handle of a server, based on its URL.

        :param url: Pointer to URL character buffer.
        :returns: Instance of :class:`.Server`.
        .. version added:: 1.0
        """
        url = url.encode('utf-8')
        result = api.tiepie_hw_network_servers_get_by_url(url, STRING_LENGTH_NULL_TERMINATED)
        library.check_last_status_raise_on_error()
        return Server(result)

    count = property(_get_count)
