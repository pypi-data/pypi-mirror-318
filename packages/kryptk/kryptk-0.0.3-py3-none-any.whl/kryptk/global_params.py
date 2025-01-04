# coding: utf-8

from ksupk import int_to_bytes


class GlobalParams:

    @staticmethod
    def get_buffer_size():
        return 256*1024

    @staticmethod
    def calc_buffer_bytes_count():
        return int_to_bytes(GlobalParams.get_buffer_size())