# coding: utf-8

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import random
from tqdm import tqdm
import unittest
from ksupk import gen_random_string
from kryptk import EncodedEntity


class TestUtils(unittest.TestCase):

    def test_EncodedEntity(self):
        str_seed = gen_random_string()
        print(f"Start TestUtils.test_EncodedEntity ({str_seed})...")
        rnd = random.Random(str_seed)
        case0 = b""
        buff = EncodedEntity(case0)
        buff1, buff2 = buff.get_as_bytes(), EncodedEntity(case0).get_as_str()
        self.assertEqual(EncodedEntity(buff1).get_as_bytes(), EncodedEntity(buff2).get_as_bytes())
        self.assertEqual(EncodedEntity(buff2).get_as_str(), buff.get_as_str())

        for _ in tqdm(range(1000)):
            case = rnd.randbytes(rnd.randint(0, 10**7))
            buff = EncodedEntity(case)
            buff1, buff2 = buff.get_as_bytes(), EncodedEntity(case).get_as_str()
            self.assertEqual(EncodedEntity(buff1).get_as_bytes(), EncodedEntity(buff2).get_as_bytes())
            self.assertEqual(EncodedEntity(buff2).get_as_str(), buff.get_as_str())

        print("Done! TestUtils.test_EncodedEntity OK")


if __name__ == "__main__":
    unittest.main()
