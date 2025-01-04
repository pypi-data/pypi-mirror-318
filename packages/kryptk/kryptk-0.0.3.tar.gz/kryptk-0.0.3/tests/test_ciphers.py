# coding: utf-8

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import random
from tqdm import tqdm
import unittest
from ksupk import gen_random_string, mkdir_with_p, create_random_file, calc_hash_of_file
from kryptk import encrypt_file, decrypt_file
from kryptk.pyca_fernet import PycaFernet, PycaFernetKey

class TestCiphers(unittest.TestCase):

    def test_PycaFernet(self):
        str_seed = gen_random_string()
        n_keys = 25
        n_rounds = 25
        print(f"Start TestCiphers.test_PycaFernet ({str_seed})...")
        rnd = random.Random(str_seed)
        testings_keys = [PycaFernetKey(b""), PycaFernetKey("")]
        for _ in range(n_keys-2):
            if rnd.randint(0, 1) == 1:
                cur_key = PycaFernetKey(rnd.randbytes(rnd.randint(0, 10**5)))
            else:
                cur_key = PycaFernetKey(gen_random_string(rnd.randint(0, 10**5)))
            testings_keys.append(cur_key)
            self.assertEqual(cur_key.dump().get_as_str(), PycaFernetKey(cur_key.dump()).dump().get_as_str())
            self.assertEqual(PycaFernetKey(cur_key.dump()).dump().get_as_bytes(), cur_key.dump().get_as_bytes())

        for key_i in tqdm(testings_keys):
            c1, c2 = PycaFernet(key_i), PycaFernet(key_i)
            self.assertEqual(c1.get_key().dump().get_as_str(), c1.get_key().dump().get_as_str())
            for _ in tqdm(range(n_rounds)):
                if rnd.randint(0, 1) == 1:
                    words = gen_random_string(rnd.randint(0, 10**7))
                else:
                    words = rnd.randbytes(rnd.randint(0, 10**7))
                for __ in range(3):
                    en1, en2 = c1.encrypt(words), c2.encrypt(words)
                    self.assertNotEqual(en1, en2)
                    de1, de2 = c1.decrypt(en1), c2.decrypt(en2)
                    self.assertEqual(de1, de2)
                    self.assertEqual(de1, words)
                    self.assertEqual(words, c1.decrypt(c1.encrypt(de2)))

        print("Done! TestCiphers.test_PycaFernet OK")

    def test_file_operations(self):
        str_seed = gen_random_string()
        n_keys = 25
        n_rounds = 25
        print(f"Start TestCiphers.test_PycaFernet with files ({str_seed})...")
        rnd = random.Random(str_seed)
        testings_keys = [PycaFernetKey(b""), PycaFernetKey("")]
        for _ in range(n_keys-2):
            if rnd.randint(0, 1) == 1:
                cur_key = PycaFernetKey(rnd.randbytes(rnd.randint(0, 10**5)))
            else:
                cur_key = PycaFernetKey(gen_random_string(rnd.randint(0, 10**5)))
            testings_keys.append(cur_key)

        root_dir = "/tmp/kryptk/file_operation_testing"
        mkdir_with_p(root_dir)
        round_file_size = [rnd.randint(512, 18388608) for _ in range(n_rounds-3)]
        round_file_size = [0, 1, 240000000] + round_file_size
        for key_i in tqdm(testings_keys):
            c1 = PycaFernet(key_i)
            self.assertEqual(c1.get_key().dump().get_as_str(), c1.get_key().dump().get_as_str())
            for round_i in tqdm(range(n_rounds)):
                file_i = os.path.join(root_dir,
                                      gen_random_string(_lenght=rnd.randint(19, 31),
                                                        seed=rnd.randint(-1000000, 1000000))
                                      )
                file_i_gpg = file_i + ".kcryptk"
                create_random_file(file_i, min_bytes_count=round_file_size[round_i], max_bytes_count=round_file_size[round_i],
                                   seed=rnd.randint(-1000000, 1000000))
                file_i_hash = calc_hash_of_file(file_i)
                gpg_hashes = []
                for __ in range(3):
                    encrypt_file(file_i, file_i_gpg, c1)
                    gpg_hash = calc_hash_of_file(file_i_gpg)
                    if round_file_size[round_i] != 0:
                        self.assertEqual(gpg_hash not in gpg_hashes, True)
                    gpg_hashes.append(gpg_hash)
                    decrypt_file(file_i_gpg, file_i, c1)
                    file_i_hash_2 = calc_hash_of_file(file_i)
                    os.unlink(file_i_gpg)
                    self.assertEqual(file_i_hash, file_i_hash_2)
                os.unlink(file_i)
        print("Done! TestCiphers.test_PycaFernet with files OK")


if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath('..'))
    unittest.main()
