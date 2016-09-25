# Copyright 2015 The py-gcal Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from .parameterized import Parameterized, Parameter


class Composite(Parameter):
    __slots__ = ['attribs', 'objtype']

    def __init__(self, attribs=None, **params):
        if attribs is None:
            attribs = []
        super(Composite, self).__init__(**params)
        self.attribs = attribs

    def __get__(self, instance, owner):
        if not instance:
            return [getattr(owner, a) for a in self.attribs]
        else:
            return [getattr(instance, a) for a in self.attribs]

    def __set__(self, instance, value):
        if not instance:
            for a, v in zip(self.attribs, value):
                setattr(self.objtype, a, v)
        else:
            for a, v in zip(self.attribs, value):
                setattr(instance, a, v)
