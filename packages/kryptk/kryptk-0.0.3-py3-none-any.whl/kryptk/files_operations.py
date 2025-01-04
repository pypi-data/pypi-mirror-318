# coding: utf-8

import os
import random
from ksupk import mkdir_with_p, get_file_size, int_to_bytes, bytes_to_int
from kryptk.interfaces import ICipher
from kryptk.global_params import GlobalParams


def encrypt_file(file_in_path: str, file_out_path: str, cipher: ICipher):
    if not os.path.isfile(file_in_path):
        raise ValueError(f"\"{file_in_path}\" is not file. ")

    file_in_path = os.path.abspath(file_in_path)
    file_out_path = os.path.abspath(file_out_path)

    needed_dir_to_exists = os.path.dirname(file_out_path)
    if not os.path.isdir(needed_dir_to_exists):
        mkdir_with_p(needed_dir_to_exists)

    i, N = 0, get_file_size(file_in_path)
    FILE_BUFFER_SIZE = GlobalParams.get_buffer_size()

    with open(file_in_path, "rb") as fd_in, open(file_out_path, "wb") as fd_out:
        while i < N:
            block = fd_in.read(FILE_BUFFER_SIZE)
            i += FILE_BUFFER_SIZE
            block_en = cipher.encrypt(block)
            # bytes_len = int_to_bytes(len(block_en))
            # assert len(bytes_len) == 1
            # fd_out.write(bytes_len)
            fd_out.write(block_en)
        fd_out.flush()


def decrypt_file(file_in_path: str, file_out_path: str, cipher: ICipher):
    if os.path.isfile(file_in_path) == False:
        raise ValueError(f"\"{file_in_path}\" is not file. ")

    file_in_path = os.path.abspath(file_in_path)
    file_out_path = os.path.abspath(file_out_path)

    needed_dir_to_exists = os.path.dirname(file_out_path)
    if not os.path.isdir(needed_dir_to_exists):
        mkdir_with_p(needed_dir_to_exists)

    i, N = 0, get_file_size(file_in_path)
    FILE_BUFFER_SIZE = len(type(cipher)(None).encrypt(random.randbytes(GlobalParams.get_buffer_size())))

    with open(file_in_path, "rb") as fd_in, open(file_out_path, "wb") as fd_out:
        while i < N :
            block = fd_in.read(FILE_BUFFER_SIZE)
            i += len(block)
            block_de = cipher.decrypt(block)
            fd_out.write(block_de)
        fd_out.flush()
