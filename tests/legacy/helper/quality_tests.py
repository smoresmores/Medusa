# coding=utf-8
# This file is part of Medusa.
#
# Medusa is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Medusa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Medusa. If not, see <http://www.gnu.org/licenses/>.

"""Test qualities."""

from __future__ import print_function

import unittest

from medusa.common import ANY, HD, HD1080p, HD720p, Quality, SD
from medusa.helpers.quality import get_quality_string

from six import iteritems


class QualityTests(unittest.TestCase):
    """Test qualities."""

    def test_get_quality_string(self):
        tests = {
            ANY: 'Any',
            HD: 'HD',
            HD720p: 'HD720p',
            HD1080p: 'HD1080p',
            Quality.FULLHDBLURAY: '1080p BluRay',
            Quality.FULLHDTV: '1080p HDTV',
            Quality.FULLHDWEBDL: '1080p WEB-DL',
            Quality.HDBLURAY: '720p BluRay',
            Quality.HDTV: '720p HDTV',
            Quality.HDWEBDL: '720p WEB-DL',
            Quality.NONE: 'N/A',
            Quality.RAWHDTV: 'RawHD',
            Quality.SDDVD: 'SD DVD',
            Quality.SDTV: 'SDTV',
            Quality.UNKNOWN: 'Unknown',
            SD: 'SD',
            1000000: 'Custom',  # An invalid quality number to test the default case
        }

        for (quality, result) in iteritems(tests):
            self.assertEqual(get_quality_string(quality), result)
