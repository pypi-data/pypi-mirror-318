import sys
import time
from typing import Optional, Callable, Any, Union
import threading

try:
    from .rust_progressbar import RustProgressBar as _RustProgressBar
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False
    _RustProgressBar = None

class ProgressBar:
    """标准进度条，提供丰富的自定义选项"""
    def __init__(
        self,
        total: int,
        prefix: str = '',
        suffix: str = '',
        decimals: int = 1,
        length: int = 50,
        fill: str = '█',
        empty: str = '░',
        print_end: str = '\r',
        show_percentage: bool = True,
        show_time: bool = True,
        show_count: bool = True,
        update_interval: float = 0.1,
        custom_format: Optional[str] = None,
        custom_formatter: Optional[Callable[[float, Any], str]] = None
    ):
        """
        初始化进度条
        :param total: 总迭代次数
        :param prefix: 前缀字符串
        :param suffix: 后缀字符串
        :param decimals: 百分比的小数位数
        :param length: 进度条的长度
        :param fill: 已完成部分的填充字符
        :param empty: 未完成部分的填充字符
        :param print_end: 打印结束符
        :param show_percentage: 是否显示百分比
        :param show_time: 是否显示耗时
        :param show_count: 是否显示计数
        :param update_interval: 更新间隔（秒）
        :param custom_format: 自定义格式字符串
        :param custom_formatter: 自定义格式化函数
        """
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.empty = empty
        self.print_end = print_end
        self.show_percentage = show_percentage
        self.show_time = show_time
        self.show_count = show_count
        self.update_interval = update_interval
        self.custom_format = custom_format
        self.custom_formatter = custom_formatter
        
        self.iteration = 0
        self.start_time = time.time()
        self._last_update = 0
        self._lock = threading.Lock()

    def print(self, iteration: Optional[int] = None):
        """打印进度条"""
        if iteration is not None:
            self.iteration = iteration

        current_time = time.time()
        if current_time - self._last_update < self.update_interval and self.iteration != self.total:
            return
        
        self._last_update = current_time
        
        percent = 100 * (self.iteration / float(self.total))
        filled_length = int(self.length * self.iteration // self.total)
        bar = self.fill * filled_length + self.empty * (self.length - filled_length)
        
        # 构建输出字符串
        if self.custom_format and self.custom_formatter:
            output = self.custom_formatter(percent, {
                'bar': bar,
                'iteration': self.iteration,
                'total': self.total,
                'time': time.time() - self.start_time
            })
        else:
            components = []
            if self.prefix:
                components.append(f"{self.prefix}")
            
            components.append(f"|{bar}|")
            
            if self.show_percentage:
                components.append(f"{percent:.{self.decimals}f}%")
            
            if self.show_count:
                components.append(f"({self.iteration}/{self.total})")
            
            if self.show_time:
                elapsed_time = time.time() - self.start_time
                components.append(f"[{elapsed_time:.1f}s]")
            
            if self.suffix:
                components.append(f"{self.suffix}")
            
            output = " ".join(components)

        print(f'\r{output}', end=self.print_end)
        sys.stdout.flush()

        if self.iteration == self.total:
            print()

    def update(self, n: int = 1):
        """更新进度"""
        with self._lock:
            self.iteration = min(self.iteration + n, self.total)
            self.print()

    def finish(self):
        """完成进度"""
        self.iteration = self.total
        self.print()

class FastProgressBar:
    """高速进度条，提供基本功能但运行速度更快"""
    def __init__(
        self,
        total: int,
        length: int = 50,
        fill: str = '█',
        empty: str = '░'
    ):
        """
        初始化高速进度条
        :param total: 总迭代次数
        :param length: 进度条的长度
        :param fill: 已完成部分的填充字符
        :param empty: 未完成部分的填充字符
        """
        self.total = max(1, total)
        self.length = length
        self.fill = fill
        self.empty = empty
        
        self.iteration = 0
        self._last_percent = -1
        self._bar = None
        self._update_step = max(1, total // 100)  # 每1%更新一次
        
    def print(self, iteration: Optional[int] = None):
        """打印进度条"""
        if iteration is not None:
            self.iteration = iteration
            
        # 只在达到更新步长或完成时更新显示
        if self.iteration % self._update_step != 0 and self.iteration != self.total:
            return
            
        current_percent = self.iteration * 100 // self.total
        
        # 只在百分比变化时更新显示
        if current_percent == self._last_percent and self.iteration != self.total:
            return
            
        self._last_percent = current_percent
        
        # 计算进度条
        filled_length = self.length * self.iteration // self.total
        bar = self.fill * filled_length + self.empty * (self.length - filled_length)
        
        # 直接打印，不使用格式化
        print(f'\r|{bar}| {current_percent}% ({self.iteration}/{self.total})', end='\r')
        
        if self.iteration == self.total:
            print()

    def update(self, n: int = 1):
        """更新进度"""
        self.iteration = min(self.iteration + n, self.total)
        self.print()

    def finish(self):
        """完成进度"""
        self.iteration = self.total
        self.print()

class VFTProgressBar:
    """极速进度条，只保留最基本功能，追求极致性能"""
    def __init__(self, total: int):
        """
        初始化极速进度条
        :param total: 总迭代次数
        """
        self.total = max(1, total)
        self.iteration = 0
        self._last_percent = -1
        self._update_step = max(1, total // 50)  # 每2%更新一次
        self._bar_length = 50
        self._bar_cache = {}  # 缓存进度条字符串

    def _get_bar(self, percent: int) -> str:
        """从缓存获取进度条字符串"""
        if percent not in self._bar_cache:
            filled = self._bar_length * percent // 100
            self._bar_cache[percent] = '█' * filled + '░' * (self._bar_length - filled)
        return self._bar_cache[percent]

    def print(self):
        """打印进度条"""
        # 只在达到更新步长时更新显示
        if self.iteration % self._update_step != 0 and self.iteration != self.total:
            return

        percent = min(100, self.iteration * 100 // self.total)
        
        # 只在百分比变化时更新显示
        if percent == self._last_percent and self.iteration != self.total:
            return
            
        self._last_percent = percent
        
        # 使用缓存的进度条字符串
        bar = self._get_bar(percent)
        
        # 使用最简单的格式化
        print(f'\r|{bar}|{percent:3d}%', end='\r')
        
        if self.iteration == self.total:
            print()

    def update(self, n: int = 1):
        """更新进度"""
        self.iteration = min(self.iteration + n, self.total)
        self.print()

    def finish(self):
        """完成进度"""
        self.iteration = self.total
        self.print()

class RustProgressBar:
    """Rust 实现的超高速进度条"""
    def __init__(self, total: int):
        """
        初始化 Rust 进度条
        :param total: 总迭代次数
        """
        if not RUST_AVAILABLE:
            raise ImportError("Rust 扩展未安装，请先编译安装 rust_progressbar")
        self._bar = _RustProgressBar(total)

    def update(self, n: int = 1):
        """更新进度"""
        self._bar.update(n)

    def finish(self):
        """完成进度"""
        self._bar.finish() 