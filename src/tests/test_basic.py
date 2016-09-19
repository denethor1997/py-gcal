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
import unittest


class TestBasics(unittest.TestCase):
    def test_inherit1(self):
        print Fourth()

    def test_inherit2(self):
        print Sixth()
        print Sixth.__mro__


class Orphan(object):
    def __init__(self, d, e, f):
        print "Orphan is initialized! d=%d, e=%d, f=%d" % (d, e, f)


class First(object):
    def __init__(self):
        print "First is initialized!"


class Second(First):
    def __init__(self, a):
        super(Second, self).__init__()
        print "Second is initialized! a=%d" % a


class Third(Second):
    def __init__(self, b, c):
        super(Third, self).__init__(3)
        print "Third is initialized! b=%d, c=%d" % (b, c)


class Fourth(Third, Second, Orphan):
    def __init__(self):
        super(Fourth, self).__init__(1, 2)
        print "Fourth is initialized!"


"""
Below definition will cause MRO error:

class Fifth(Second, Third, Orphan):
    def __init__(self):
        super(Fifth, self).__init__(1, 2)
        print "Fifth is initialized!"
"""


class Sixth(Orphan, Second):
    def __init__(self):
        super(Sixth, self).__init__(1, 2, 3)
        print "Sixth is initialized!"


if __name__ == '__main__':
    unittest.main()
