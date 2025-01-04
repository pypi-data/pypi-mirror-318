import ctypes

# 定义常量
max_eeg_group_num = 256
max_channel = 16
max_wave_channel = 4
max_ir_channel=256


# 定义结构体
class Pkg(ctypes.Structure):
    _fields_ = [
        ("pkglen", ctypes.c_int16),
        ("pkgnum", ctypes.c_int32),
        ("time_mark", ctypes.c_int32),
        ("pkg_type", ctypes.c_uint8),
        ("eeg_channel", ctypes.c_uint8),
        ("eeg_data_num", ctypes.c_uint8),
        ("ir_channel", ctypes.c_uint8),
        ("brain_elec", (ctypes.c_float * max_eeg_group_num) * max_channel),
        ("near_infrared", (ctypes.c_float * max_wave_channel) * max_ir_channel),
        ("acceleration_x", ctypes.c_float),
        ("acceleration_y", ctypes.c_float),
        ("acceleration_z", ctypes.c_float),
        ("temperature", ctypes.c_float),
        ("Battery_State", ctypes.c_float),
        ("fall_off", ctypes.c_int32),
        ("error_state", ctypes.c_int32),
    ]

    def covert_to_pkg(self):
        # 初始化字典
        result = {}

        # 属性列表
        attributes = [
            'pkglen', 'pkgnum', 'time_mark', 'pkg_type', 'eeg_channel', 'eeg_data_num',
            'ir_channel', 'brain_elec', 'near_infrared', 'acceleration_x', 'acceleration_y',
            'acceleration_z', 'temperature', 'Battery_State', 'fall_off', 'error_state'
        ]

        pkg_type = getattr(self, "pkg_type", None)
        for attr in attributes:
            if attr in ['brain_elec', 'near_infrared']:
                if pkg_type == 1 :
                    result["brain_elec"] = [list(sublist)for sublist in getattr(self,"brain_elec",[])]
                elif pkg_type == 2:
                    result["near_infrared"] = [list(sublist)for sublist in getattr(self,"near_infrared",[])]
            else:
                result[attr] = getattr(self, attr, None)

        return result