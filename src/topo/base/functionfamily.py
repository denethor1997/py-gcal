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
import param


class LearningFn(param.Parameterized):
    __abstract = True

    def __call__(self,input_activity, unit_activity, weights, single_connection_learning_rate):
        raise NotImplementedError


class Hebbian(LearningFn):

    def __call__(self,input_activity, unit_activity, weights, single_connection_learning_rate):
        weights += single_connection_learning_rate * unit_activity * input_activity


class ResponseFn(param.Parameterized):
    __abstract = True

    def __call__(self,m1,m2):
        raise NotImplementedError


class DotProduct(ResponseFn):

    def __call__(self,m1,m2):
        return np.dot(m1.ravel(), m2.ravel())


class CoordinateMapperFn(param.Parameterized):
    __abstract = True

    def __call__(self, x, y):
        raise NotImplementedError


class IdentityMF(CoordinateMapperFn):

    def __call__(self, x, y):
        return x,y
