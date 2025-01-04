import unittest
import time
from progressplus import ProgressBar, FastProgressBar, VFTProgressBar, RustProgressBar
from progressplus.progress_bar import RUST_AVAILABLE

class TestProgressBar(unittest.TestCase):
    def test_progress_bar_speed(self):
        total = 10000000  # 1000 万次迭代

        # 测试标准进度条速度
        start_time = time.time()
        bar = ProgressBar(total)
        for i in range(total):
            bar.update()
        bar.finish()
        standard_duration = time.time() - start_time

        # 测试高速进度条速度
        start_time = time.time()
        fast_bar = FastProgressBar(total)
        for i in range(total):
            fast_bar.update()
        fast_bar.finish()
        fast_duration = time.time() - start_time

        # 测试极速进度条速度
        start_time = time.time()
        vft_bar = VFTProgressBar(total)
        for i in range(total):
            vft_bar.update()
        vft_bar.finish()
        vft_duration = time.time() - start_time

        print(f"\n性能测试结果:")
        print(f"标准进度条耗时: {standard_duration:.4f} 秒")
        print(f"高速进度条耗时: {fast_duration:.4f} 秒 (提升 {standard_duration/fast_duration:.2f}x)")
        print(f"极速进度条耗时: {vft_duration:.4f} 秒 (提升 {standard_duration/vft_duration:.2f}x)")

        # 如果 Rust 扩展可用，测试 Rust 进度条速度
        if RUST_AVAILABLE:
            start_time = time.time()
            rust_bar = RustProgressBar(total)
            for i in range(total):
                rust_bar.update()
            rust_bar.finish()
            rust_duration = time.time() - start_time
            print(f"Rust 进度条耗时: {rust_duration:.4f} 秒 (提升 {standard_duration/rust_duration:.2f}x)")

if __name__ == '__main__':
    unittest.main() 