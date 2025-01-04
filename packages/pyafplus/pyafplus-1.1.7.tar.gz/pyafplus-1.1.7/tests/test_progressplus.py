import unittest
import time
from progressplus import ProgressBar, FastProgressBar, VFTProgressBar, RustProgressBar, RustProgressBarPlus
from progressplus.progress_bar import RUST_AVAILABLE

class TestProgressBar(unittest.TestCase):
    def test_progress_bar_speed(self):
        total = 10000000  # 1千万次迭代

        
        # 测试高速进度条速度
        start_time = time.time()
        fast_bar = FastProgressBar(total, unit='it', speed_unit='it/s')
        for i in range(total):
            fast_bar.update()
        fast_bar.finish()
        fast_duration = time.time() - start_time

        # 测试极速进度条速度
        start_time = time.time()
        vft_bar = VFTProgressBar(total, unit='it', speed_unit='it/s')
        for i in range(total):
            vft_bar.update()
        vft_bar.finish()
        vft_duration = time.time() - start_time
    
        # 预测标准进度条完成所需时长（放在最后测试）
        bar = ProgressBar(total, unit='it', speed_unit='it/s')
        start_time = time.time()
        for i in range(total):
            bar.update()
            if i == total // 100:  # 迭代到1%时预测总时间
                elapsed_time = time.time() - start_time
                estimated_total_time = elapsed_time * 100
                break
        bar.finish()
        standard_duration = estimated_total_time

        print(f"\n性能测试结果:")
        print(f"标准进度条耗时（预测）: {standard_duration:.4f} 秒")
        print(f"高速进度条耗时: {fast_duration:.4f} 秒 (提升 {standard_duration/fast_duration:.2f}x)")
        print(f"极速进度条耗时: {vft_duration:.4f} 秒 (提升 {standard_duration/vft_duration:.2f}x)")

        # 如果 Rust 扩展可用，测试 Rust 进度条速度
        if RUST_AVAILABLE:
            start_time = time.time()
            rust_bar = RustProgressBar(total, unit='it', speed_unit='it/s')
            for i in range(total):
                rust_bar.update()
            rust_bar.finish()
            rust_duration = time.time() - start_time
            print(f"Rust 进度条耗时: {rust_duration:.4f} 秒 (提升 {standard_duration/rust_duration:.2f}x)")

    def test_custom_units(self):
        """测试自定义单位功能"""
        total = 100
        
        # 测试文件大小单位
        bar = ProgressBar(total, unit='MB', speed_unit='MB/s')
        for i in range(total):
            time.sleep(0.01)
            bar.update()
        bar.finish()

        # 测试数据处理单位
        bar = ProgressBar(total, unit='条', speed_unit='条/s')
        for i in range(total):
            time.sleep(0.01)
            bar.update()
        bar.finish()

    def test_display_options(self):
        """测试显示选项"""
        total = 100
        
        # 只显示进度条和百分比
        bar = ProgressBar(total, show_speed=False, show_time=False)
        for i in range(total):
            time.sleep(0.01)
            bar.update()
        bar.finish()

        # 显示所有信息
        bar = ProgressBar(total, prefix='处理中:', suffix='完成',
                         show_speed=True, show_time=True, show_percent=True)
        for i in range(total):
            time.sleep(0.01)
            bar.update()
        bar.finish()

    def test_rust_features(self):
        """测试 Rust 进度条的特性"""
        if not RUST_AVAILABLE:
            self.skipTest("Rust 扩展未安装")
            return

        total = 100
        bar = RustProgressBar(
            total=total,
            prefix="Rust处理:",
            suffix="完成",
            decimals=1,
            length=50,
            fill="█",
            unit="MB",
            speed_unit="MB/s",
            show_speed=True,
            show_time=True,
            show_percent=True,
            update_threshold=1
        )

        for i in range(total):
            time.sleep(0.01)
            bar.update()
        bar.finish()

    def test_rust_plus_features(self):
        """测试增强版 Rust 进度条的特性"""
        if not RUST_AVAILABLE:
            self.skipTest("Rust 扩展未安装")
            return

        total = 100

        # 测试标准格式
        bar = RustProgressBarPlus(
            total=total,
            prefix="RustPlus处理:",
            suffix="完成",
            decimals=1,
            length=50,
            fill="█",
            empty="░",
            unit="MB",
            speed_unit="MB/s",
            show_speed=True,
            show_time=True,
            show_percent=True,
            show_count=True,
            show_bar=True,
            update_threshold=1,
            min_update_interval=0.1
        )

        for i in range(total):
            time.sleep(0.01)
            bar.update()
        bar.finish()

        # 测试自定义格式
        bar = RustProgressBarPlus(
            total=total,
            fill="=",
            empty=" ",
            unit="个",
            speed_unit="个/s",
            custom_format="自定义 |{bar}| {percent}% ({count}) [{speed}] ETA: {eta}"
        )

        for i in range(total):
            time.sleep(0.01)
            bar.update()
        bar.finish()

        # 测试最小显示
        bar = RustProgressBarPlus(
            total=total,
            show_speed=False,
            show_time=False,
            show_percent=False,
            show_count=False,
            min_update_interval=0.1
        )

        for i in range(total):
            time.sleep(0.01)
            bar.update()
        bar.finish()

        # 测试性能
        total = 10000000  # 1千万次迭代
        start_time = time.time()
        bar = RustProgressBarPlus(
            total=total,
            update_threshold=10000,
            min_update_interval=0.1
        )
        for i in range(total):
            bar.update()
        bar.finish()
        duration = time.time() - start_time
        print(f"增强版 Rust 进度条耗时: {duration:.4f} 秒")

if __name__ == '__main__':
    unittest.main() 