# -*- coding: utf-8 -*-
#
#   DIM-SDK : Decentralized Instant Messaging Software Development Kit
#
#                                Written in 2023 by Moky <albert.moky@gmail.com>
#
# ==============================================================================
# MIT License
#
# Copyright (c) 2023 Albert Moky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

from abc import ABC, abstractmethod
from typing import Optional, List

from dimp import VerifyKey, EncryptKey
from dimp import ID

from .mkm import User, Group


class Archivist(ABC):

    @abstractmethod  # protected
    async def create_user(self, identifier: ID) -> Optional[User]:
        """
        Create user when visa.key exists

        :param identifier: user ID
        :return: user, None on not ready
        """
        raise NotImplemented

    @abstractmethod  # protected
    async def create_group(self, identifier: ID) -> Optional[Group]:
        """
        Create group when members exist

        :param identifier: group ID
        :return: group, None on not ready
        """
        raise NotImplemented

    @property
    @abstractmethod
    async def local_users(self) -> List[User]:
        """
        Get all local users (for decrypting received message)

        :return: users with private key
        """
        raise NotImplemented

    @abstractmethod
    async def get_meta_key(self, identifier: ID) -> Optional[VerifyKey]:
        """
        Get meta.key

        :param identifier: user ID
        :return: None on not found
        """
        raise NotImplemented

    @abstractmethod
    async def get_visa_key(self, identifier: ID) -> Optional[EncryptKey]:
        """
        Get visa.key

        :param identifier: user ID
        :return: None on not found
        """
        raise NotImplemented
