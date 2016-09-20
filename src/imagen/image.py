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
import param

from overrides import overrides
from patterngenerator import ChannelGenerator


class ImageSampler(param.Parameterized):
    __abstract = True

    def __call__(self,image,x,y,sheet_xdensity,sheet_ydensity,width=1.0,height=1.0):
        pass


class PatternSampler(ImageSampler):

    @overrides
    def __call__(self, image, x, y, sheet_xdensity, sheet_ydensity, width=1.0, height=1.0):
        pass


class GenericImage(ChannelGenerator):
    __abstract = True

    def __init__(self, **params):
        super(GenericImage, self).__init__(**params)

    def _get_image(self, p):
        pass


class FileImage(GenericImage):

    def __init__(self, **params):
        super(FileImage, self).__init__(**params)

    def __call__(self, **params_to_overrides):
        pass
