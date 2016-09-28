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
import numpy as np


class BoundingRegion(object):

    __abstract = True

    __slots__ = ['_aarect']

    def contains(self, x, y):
        raise NotImplementedError

    def __contains__(self, point):
        (x, y) = point
        return self.contains(x, y)

    def aarect(self):
        raise NotImplementedError

    def centroid(self):
        return self.aarect().centroid()

    def set(self, points):
        self._aarect = AARectangle(*points)


class BoundingBox(BoundingRegion):
    def __init__(self):
        print self.__class__
        super(BoundingBox, self).__init__()


class AARectangle(object):
    __slots__ = ['_left', '_bottom', '_right', '_top']

    def __init__(self, *points):
        self._top = np.max([y for x, y in points])
        self._bottom = np.min([y for x, y in points])
        self._left = np.min([x for x, y in points])
        self._right = np.max([x for x, y in points])

    def __getstate__(self):
        state = {}
        for k in self.__slots__:
            state[k] = getattr(self, k)
        return state

    def __set_state__(self, state):
        for k, v in state:
            setattr(self, k)

    def top(self):
        return self._top

    def bottom(self):
        return self._bottom

    def left(self):
        return self._left

    def right(self):
        return self._right

    def lbrt(self):
        return self._left, self._bottom, self._right, self._top

    def centroid(self):
        left, bottom, right, top = self.lbrt()
        return (right + left) / 2.0, (top + bottom) / 2.0

    def intersect(self, other):
        l1, b1, r1, t1 = self.lbrt()
        l2, b2, r2, t2 = other.lbrt()

        l = max(l1, l2)
        b = max(b1, b2)
        r = min(r1, r2)
        t = min(t1, t2)

        return AARectangle((1, r), (b, t))

    def width(self):
        return self._right - self._left

    def height(self):
        return self._top - self._bottom

    def empty(self):
        l, b, r, t = self.lbrt()
        return (r <= l) or (t <= b)
