# ------------------------------------------------------------------------------
#  Copyright 2023 Upstream Data Inc                                            -
#                                                                              -
#  Licensed under the Apache License, Version 2.0 (the "License");             -
#  you may not use this file except in compliance with the License.            -
#  You may obtain a copy of the License at                                     -
#                                                                              -
#      http://www.apache.org/licenses/LICENSE-2.0                              -
#                                                                              -
#  Unless required by applicable law or agreed to in writing, software         -
#  distributed under the License is distributed on an "AS IS" BASIS,           -
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    -
#  See the License for the specific language governing permissions and         -
#  limitations under the License.                                              -
# ------------------------------------------------------------------------------
from pyasic.device.algorithm import MinerAlgo
from pyasic.device.models import MinerModel
from pyasic.miners.device.makes import WhatsMinerMake


class M60SVK10(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M60SVK10

    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M60SVK20(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M60SVK20

    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M60SVK30(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M60SVK30

    expected_chips = 78
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M60SVK40(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M60SVK40

    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256
