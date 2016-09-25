# Copyright 2016 The py-gcal Authors. All Rights Reserved.
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


class SheetCoordinateSystem(object):

    @property
    def xdensity(self):
        return self.__xdensity

    @property
    def ydensity(self):
        return self.__ydensity

    @property
    def shape(self):
        return self.__shape

    def __init__(self, bounds, xdensity, ydensity):
        self.bounds = bounds
        self.__set_xdensity(xdensity)
        self.__set_ydensity(ydensity)
        self.lbrt = np.array(bounds.lbrt())

    def __set_xdensity(self, xdensity):
        self.__xdensity = xdensity
        self.__xstep = 1.0/xdensity

    def __set_ydensity(self, ydensity):
        self.__ydensity = ydensity
        self.__ystep = 1.0/ydensity

    def sheet2matrix(self, x, y):
        float_col = (x - self.lbrt[0]) * self.__xdensity
        float_row = (self.lbrt[3] - y) * self.__ydensity
        return float_row, float_col


class Slice(np.ndarray):

    __slots__ = []

    def __new__(cls, a):
        a = np.array(a).view(cls)
        return a

    def submatrix(self, matrix):
        return matrix[self[0]:self[1], self[2]:self[3]]



    def _boundsspec2slicespec(boundsspec, scs):
        l, b, r, t = boundsspec


