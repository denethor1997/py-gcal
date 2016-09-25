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
import overrides
from overrides import overrides

import param

from holoviews.core import BoundingBox


class PatternGenerator(param.Parameterized):
    __abstract = True

    bounds = BoundingBox(points = ((-0.5, -0.5), (0.5, 0.5)))
    xdensity = 256
    ydensity = 256
    x = 0.0
    y = 0.0
    z = None
    group = 'Pattern'
    position = param.Composite(attribs=['x','y'])
    orientation = 0.0
    size = 1.0
    scale = 1.0
    offset = 0.0
    output_fns = []

    def __init__(self, **params):
        super(PatternGenerator, self).__init__(**params)

    def __call__(self, **kwargs):
        pass

    def channels(self, **params):
        pass

    def num_channels(self):
        return 1

    def function(self, p):
        pass


class CompositeBase(PatternGenerator):
    __abstract = True


class Composite(CompositeBase):

    @overrides
    def function(self, p):
        pass


class ChannelGenerator(PatternGenerator):
    __abstract = True
    
    def __init__(self, **params):
        super(ChannelGenerator, self).__init__(**params)

    @overrides
    def channels(self, **params):
        pass