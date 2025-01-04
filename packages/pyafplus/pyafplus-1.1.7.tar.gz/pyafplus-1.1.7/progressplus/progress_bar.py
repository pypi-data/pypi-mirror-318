import sys
import time
from typing import Optional

try:
    from . import rust_progressbar
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False

class ProgressBar:
    def __init__(self, total: int, prefix: str = '', suffix: str = '', 
                 decimals: int = 1, length: int = 50, fill: str = '█', 
                 unit: str = '', speed_unit: str = 'it/s',
                 show_speed: bool = True, show_time: bool = True,
                 show_percent: bool = True):
        """
        初始化进度条
        :param total: 总迭代次数
        :param prefix: 前缀字符串
        :param suffix: 后缀字符串
        :param decimals: 百分比的小数位数
        :param length: 进度条的长度
        :param fill: 进度条填充字符
        :param unit: 进度单位（如：MB, KB, 个）
        :param speed_unit: 速度单位（如：it/s, MB/s）
        :param show_speed: 是否显示速度
        :param show_time: 是否显示预计剩余时间
        :param show_percent: 是否显示百分比
        """
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.unit = unit
        self.speed_unit = speed_unit
        self.show_speed = show_speed
        self.show_time = show_time
        self.show_percent = show_percent
        
        self.iteration = 0
        self.start_time = time.time()
        self.last_update_time = self.start_time
        self._speed = 0

    def print(self, end: str = ""):
        """打印进度条"""
        percent = ("{0:." + str(self.decimals) + "f}") \
                 .format(100 * (self.iteration / float(self.total)))
        filled_length = int(self.length * self.iteration // self.total)
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        
        # 计算速度和预计剩余时间
        current_time = time.time()
        elapsed_time = current_time - self.start_time
        if elapsed_time > 0:
            self._speed = self.iteration / elapsed_time
            eta = (self.total - self.iteration) / self._speed if self._speed > 0 else 0
        else:
            self._speed = 0
            eta = 0

        # 构建输出字符串
        output_parts = []
        if self.prefix:
            output_parts.append(f"{self.prefix}")
        
        output_parts.append(f"|{bar}|")
        
        if self.show_percent:
            output_parts.append(f" {percent}%")
        
        if self.unit:
            output_parts.append(f" {self.iteration}{self.unit}/{self.total}{self.unit}")
        
        if self.show_speed:
            output_parts.append(f" {self._speed:.2f}{self.speed_unit}")
        
        if self.show_time:
            output_parts.append(f" ETA: {eta:.1f}s")
        
        if self.suffix:
            output_parts.append(f" {self.suffix}")

        print('\r' + ' '.join(output_parts), end=end)
        sys.stdout.flush()

    def update(self, iteration: Optional[int] = None):
        """
        更新进度条
        :param iteration: 当前迭代次数，如果为None则自动加1
        """
        if iteration is not None:
            self.iteration = iteration
        else:
            self.iteration += 1
        self.print()

    def finish(self):
        """完成进度条"""
        self.iteration = self.total
        self.print(end="\n")

class FastProgressBar(ProgressBar):
    def __init__(self, total: int, min_update_interval: float = 0.1, **kwargs):
        """
        初始化快速进度条
        :param total: 总迭代次数
        :param min_update_interval: 最小更新间隔（秒）
        """
        super().__init__(total, **kwargs)
        self.min_update_interval = min_update_interval
        self.last_update_time = time.time()

    def update(self, iteration: Optional[int] = None):
        current_time = time.time()
        if current_time - self.last_update_time >= self.min_update_interval:
            super().update(iteration)
            self.last_update_time = current_time
        elif iteration is not None:
            self.iteration = iteration
        else:
            self.iteration += 1

class VFTProgressBar(ProgressBar):
    def __init__(self, total: int, update_threshold: int = 1000, **kwargs):
        """
        初始化极速进度条
        :param total: 总迭代次数
        :param update_threshold: 更新阈值（每多少次迭代更新一次）
        """
        super().__init__(total, **kwargs)
        self.update_threshold = update_threshold
        self.update_count = 0

    def update(self, iteration: Optional[int] = None):
        if iteration is not None:
            self.iteration = iteration
        else:
            self.iteration += 1
        
        self.update_count += 1
        if self.update_count >= self.update_threshold:
            self.print()
            self.update_count = 0

class RustProgressBar:
    def __init__(self, total: int, prefix: str = '', suffix: str = '',
                 decimals: int = 1, length: int = 50, fill: str = '█',
                 unit: str = '', speed_unit: str = 'it/s',
                 show_speed: bool = True, show_time: bool = True,
                 show_percent: bool = True, update_threshold: int = 1000):
        """
        初始化 Rust 实现的进度条
        :param total: 总迭代次数
        :param prefix: 前缀字符串
        :param suffix: 后缀字符串
        :param decimals: 百分比的小数位数
        :param length: 进度条的长度
        :param fill: 进度条填充字符
        :param unit: 进度单位（如：MB, KB, 个）
        :param speed_unit: 速度单位（如：it/s, MB/s）
        :param show_speed: 是否显示速度
        :param show_time: 是否显示预计剩余时间
        :param show_percent: 是否显示百分比
        :param update_threshold: 更新阈值（每多少次迭代更新一次）
        """
        if not RUST_AVAILABLE:
            raise ImportError("Rust 扩展未安装，请先编译安装 rust_progressbar")
        
        self.bar = rust_progressbar.RustProgressBar(
            total, prefix, suffix, decimals, length, fill,
            unit, speed_unit, show_speed, show_time, show_percent,
            update_threshold
        )

    def update(self, iteration: Optional[int] = None):
        """更新进度"""
        self.bar.update(iteration if iteration is not None else 1)

    def finish(self):
        """完成进度"""
        self.bar.finish() 

class RustProgressBarPlus:
    def __init__(self, total: int, prefix: str = '', suffix: str = '',
                 decimals: int = 1, length: int = 50, fill: str = '█',
                 empty: str = '░', unit: str = '', speed_unit: str = 'it/s',
                 show_speed: bool = True, show_time: bool = True,
                 show_percent: bool = True, show_count: bool = True,
                 show_bar: bool = True, update_threshold: int = 1000,
                 min_update_interval: float = 0.1, custom_format: str = None):
        """
        初始化增强版 Rust 进度条
        :param total: 总迭代次数
        :param prefix: 前缀字符串
        :param suffix: 后缀字符串
        :param decimals: 百分比的小数位数
        :param length: 进度条的长度
        :param fill: 进度条填充字符
        :param empty: 进度条空白字符
        :param unit: 进度单位（如：MB, KB, 个）
        :param speed_unit: 速度单位（如：it/s, MB/s）
        :param show_speed: 是否显示速度
        :param show_time: 是否显示预计剩余时间
        :param show_percent: 是否显示百分比
        :param show_count: 是否显示计数
        :param show_bar: 是否显示进度条
        :param update_threshold: 更新阈值（每多少次迭代更新一次）
        :param min_update_interval: 最小更新间隔（秒）
        :param custom_format: 自定义格式字符串，支持以下占位符：
                            {bar} - 进度条
                            {percent} - 百分比
                            {count} - 计数
                            {speed} - 速度
                            {eta} - 预计剩余时间
        """
        if not RUST_AVAILABLE:
            raise ImportError("Rust 扩展未安装，请先编译安装 rust_progressbar")
        
        self.bar = rust_progressbar.RustProgressBarPlus(
            total, prefix, suffix, decimals, length, fill, empty,
            unit, speed_unit, show_speed, show_time, show_percent,
            show_count, show_bar, update_threshold, min_update_interval,
            custom_format
        )

    def update(self, iteration: Optional[int] = None):
        """更新进度"""
        self.bar.update(iteration if iteration is not None else None)

    def finish(self):
        """完成进度"""
        self.bar.finish() 