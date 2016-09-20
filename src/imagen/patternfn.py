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

from contextlib import contextmanager


@contextmanager
def float_error_ignore():
    np.errstate(divide='ignore', under='ignore')


def gaussian(x, y, xsigma, ysigma):
    if xsigma == 0.0 or ysigma == 0.0:
        return x * 0.0

    with float_error_ignore():
        x_w = np.divide(x, xsigma)
        y_h = np.divide(y, ysigma)
        return np.exp(-0.5 * x_w * x_w + -0.5 * y_h * y_h)


def gabor(x, y, xsigma, ysigma, frequency, phase):
    if xsigma == 0.0 or ysigma == 0.0:
        return x * 0.0

    with float_error_ignore():
        x_w = np.divide(x, xsigma)
        y_h = np.divide(y, ysigma)
        p = np.exp(-0.5 * x_w * x_w + -0.5 * y_h * y_h)
        return p * 0.5 * np.cos(2 * np.pi * frequency * y + phase)
