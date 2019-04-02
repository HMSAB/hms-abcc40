# Copyright 2019 HMS Industrial Networks AB
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


import json
import unittest

import hms.abcc40


TEST_JSON = """{
"modulename": "ABCC M40",
"serial": "ABCDEF00",
"fwver": [ 2, 6, 0 ],
"uptime": [ 5, 123456 ],
"cpuload": 55,
"fwvertext": "1.05.02",
"vendorname": "HMS Industrial Networks",
"hwvertext": "2",
"networktype": 137
}"""


class TestModuleInfo(unittest.TestCase):

    def setUp(self):
        super(TestModuleInfo, self).setUpClass()
        self.CompactCom40 = hms.abcc40.CompactCom40("")
        self.CompactCom40._get = lambda _, key: json.loads(TEST_JSON)[key]

    def testModuleName(self):
        self.assertEqual(self.CompactCom40.module_name, "ABCC M40")

    def testSerialNumber(self):
        self.assertEqual(self.CompactCom40.serial_number, "ABCDEF00")

    def testFirmwareVersion(self):
        self.assertEqual(self.CompactCom40.firmware_version, [2, 6, 0])

    def testFirmwareVersionText(self):
        self.assertEqual(self.CompactCom40.firmware_version_text, "1.05.02")

    def testUptime(self):
        self.assertEqual(self.CompactCom40.uptime, (5 << 32) + 123456)

    def testCpuLoad(self):
        self.assertEqual(self.CompactCom40.cpu_load, 0.55)

    def testVendorName(self):
        self.assertEqual(self.CompactCom40.vendor_name,
                         "HMS Industrial Networks")

    def testHardwareVersionText(self):
        self.assertEqual(self.CompactCom40.hardware_version_text, "2")

    def testNetworkType(self):
        self.assertEqual(self.CompactCom40.network_type, 137)


if __name__ == "__main__":

    unittest.main()
