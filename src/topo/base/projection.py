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
from .simulation import EPConnection
from .sheet import Sheet


class Projection(EPConnection):
    __abstract = True
    
    def __init__(self, **param):
        super(Projection, self).__init__()

    def activate(self, input_activity):
        raise NotImplementedError

    def learn(self):
        pass
        
        
class ProjectionSheet(Sheet):
    def __init__(self, **param):
        super(ProjectionSheet, self).__init__(**param)

    def activate(self):
        pass

    def learn(self):
        pass
