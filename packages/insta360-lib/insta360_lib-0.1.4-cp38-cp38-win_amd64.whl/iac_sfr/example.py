import iac_sfr.iac_sfr as mod

class RawImageProcessor:

    def __init__(self):
        self.width = 3072
        self.height = 4096
        self.nyx = 3
        self.near_cent = 0
        self.far_cent = 0

    def input_data(self, near_points, far_points):
        """设置用于处理的点数据"""
        self.near_cent = near_points
        self.far_cent = far_points

    def input_resolution(self, raw_width, raw_height, ny):
        """输入图像的分辨率和ny值"""
        self.width = raw_width
        self.height = raw_height
        self.nyx = ny
        print(f"width: {self.width}, height: {self.height}")

    def process_image(self, raw_path, output_path, raw_type):
        sfr_param = mod.SFRParam()
        sfr_result = mod.SFRResult_IAC2()
        sfr_param.nyX = self.nyx
        sfr_param.roiSize = 64
        sfr_param.offset = 100

        # 根据传入的raw_type选择合适的函数调用
        ret_code = {
            "raw14": mod.sunnyinstaSFR_raw14_IAC3B,
            "raw16_8k": mod.sunnyinstaSFR_raw16_IAC2_8K,
            "raw16": mod.sunnyinstaSFR_raw16_IAC3B,
            "default": mod.sunnyinstaSFR_raw16_IAC3B,
            "tc4_raw10": mod.sunnyinstaSFR_raw10_IAC3B,
        }.get(raw_type, mod.sunnyinstaSFR_raw16_IAC3B)(raw_path, self.width, self.height, sfr_param, sfr_result)

        print(f"ret: {ret_code}")
        self._log_output(sfr_result, output_path, ret_code)
    def _log_output(self, sfr_result, output_path, ret_code):
        """根据处理结果输出日志到文件"""
        try:
            with open(output_path, 'w') as f:
                f.write(f"Result code: {ret_code}\n")
                for idx, sfr_detail in enumerate(sfr_result.get_sfr()):
                    print(f"SFR Detail {idx}: roicx={sfr_detail.roicx}, "
                            f"roicy={sfr_detail.roicy}, sfr_ny4={sfr_detail.sfr_ny4}")
                    f.write(f"SFR Detail {idx}: roicx={sfr_detail.roicx}, "
                            f"roicy={sfr_detail.roicy}, sfr_ny4={sfr_detail.sfr_ny4}\n")
                print(f"Processing completed with code {ret_code}")
        except IOError:
            print("Error writing to output file")
if __name__ == '__main__':


    print(dir(mod))
    test = RawImageProcessor()
    test.process_image(r"E:\perf_test\perf_test\perf_test\perf_test\1227_SFR_TEST\SFR_TEST.raw", r"E:\perf_test\perf_test\perf_test\perf_test\1227_SFR_TEST\SFR_TEST.log", "raw16")