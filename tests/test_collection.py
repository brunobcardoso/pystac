import os
import unittest
from tempfile import TemporaryDirectory

from pystac import *
from tests.utils import (TestCases, RANDOM_GEOM, RANDOM_BBOX)

class CollectionTest(unittest.TestCase):
    def test_spatial_extent_from_coordinates(self):
        extent = SpatialExtent.from_coordinates(RANDOM_GEOM['coordinates'])

        self.assertEqual(len(extent.bboxes), 1)
        bbox = extent.bboxes[0]
        self.assertEqual(len(bbox), 4)
        for x in bbox:
            self.assertTrue(type(x) is float)