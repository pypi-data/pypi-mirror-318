# ------------------------------------------------------------------------------
#  Copyright 2022 Upstream Data Inc                                            -
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


class M50VE30(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VE30

    expected_hashboards = 4
    expected_chips = 255
    expected_fans = 2
    algo = MinerAlgo.SHA256


class M50VG30(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VG30

    expected_chips = 156
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VH10(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VH10

    expected_chips = 86
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VH20(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VH20

    expected_chips = 111
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VH30(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VH30

    expected_chips = 117
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VH40(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VH40

    expected_chips = 84
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VH50(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VH50

    expected_chips = 105
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VH60(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VH60

    expected_chips = 84
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VH70(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VH70

    expected_chips = 105
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VH80(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VH80

    expected_chips = 111
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VH90(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VH90

    expected_chips = 117
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VJ10(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VJ10

    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VJ20(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VJ20

    expected_chips = 111
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256


class M50VJ30(WhatsMinerMake):
    raw_model = MinerModel.WHATSMINER.M50VJ30

    expected_chips = 117
    expected_fans = 2
    expected_hashboards = 3
    algo = MinerAlgo.SHA256
