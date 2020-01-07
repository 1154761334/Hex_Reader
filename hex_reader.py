import sys
import os

from intelhex import IntelHex
from datetime import datetime

def import_file(filename):
    ih = IntelHex()
    ih.loadfile(filename, format='bin')
    return ih

# def give_hex(ih, start_position, num_index=1):
#     this_hex = ''
#     for i in range(start_position,start_position + num_index):
#         this_bit = hex(ih[i]).strip('0x')
#         if len(this_bit) == 1:
#             this_bit = '0' + this_bit
#         this_hex = this_bit + this_hex
#     this_hex = '0x'+ this_hex
#     return this_hex


class Camera:
    def __init__(self,ih):
        self.ih  = ih
        self.time_index =8
        self.vision_index = 7
        self.value_index = 16
        self.area_data = 164

    def give_hex(self, start_position, num_index=1):
        ih  = self.ih
        this_hex = ''
        for i in range(start_position, start_position + num_index):
            this_bit = hex(ih[i]).strip('0x')
            if len(this_bit) == 1:
                this_bit = '0' + this_bit
            this_hex = this_bit + this_hex
        this_hex = '0x' + this_hex
        return this_hex

    def get_start_time(self):
        start = 0
        num = 4
        ih = self.ih
        time_stamp = int(self.give_hex(start, num), 16)
        return datetime.fromtimestamp(time_stamp)

    def get_end_time(self):
        start = 4
        num = 4
        ih = self.ih
        time_stamp = int(self.give_hex(start, num), 16)
        return datetime.fromtimestamp(time_stamp)

    def get_polygon(self,area):
        ih = self.ih
        start = self.time_index + self.value_index + self.vision_index + 13 + (area-1)*164
        return hex(ih[start])

    def get_pass(self,area):

        ih = self.ih
        start = 107 + (area-1)*164
        num = 2
        return int(self.give_hex(start,num),16)

    # def get_pass(self,area_1,area_2):
    #     ih = self.ih
    #     start = 107 + (area-1)*164
    #     num = 2


def main(file_name):
    ih = import_file(file_name)
    a = Camera(ih)
    print('开始记录的时间是：', a.get_start_time())
    print('结束记录的时间是：',a.get_end_time())
    # print('当前多边形的顶点数量为：',a.get_polygon(1))
    print('当前多边形1的经过人数为：',a.get_pass(1))
    # print('当前多边形的顶点数量为：',a.get_polygon(2))
    print('当前多边形2的经过人数为：', a.get_pass(2))


if __name__ == '__main__':
    main(file_name='10251026.hmd')