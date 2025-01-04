import unittest
import time
from progressplus import ProgressBar, FastProgressBar

class TestProgressBar(unittest.TestCase):
    def test_progress_bar_basic(self):
        total = 100
        bar = ProgressBar(total)
        for i in range(total):
            bar.update()
            time.sleep(0.01)  # 模拟工作
        bar.finish()

    def test_progress_bar_custom(self):
        total = 50
        bar = ProgressBar(
            total,
            prefix='Progress:',
            suffix='Complete',
            decimals=2,
            length=40,
            fill='#',
            empty='-',
            show_time=True,
            show_count=True
        )
        for i in range(total):
            bar.update()
            time.sleep(0.01)  # 模拟工作
        bar.finish()

    def test_fast_progress_bar(self):
        total = 1000
        bar = FastProgressBar(total)
        for i in range(total):
            bar.update()
        bar.finish()

if __name__ == '__main__':
    unittest.main() 