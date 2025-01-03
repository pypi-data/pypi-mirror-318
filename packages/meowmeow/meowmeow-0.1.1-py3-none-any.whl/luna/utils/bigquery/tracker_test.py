import time

from .tracker import TqdmTracker

tracker = TqdmTracker()


def test_tqdm_tracker():
    tracker.start(total=100)
    for i in range(100):
        tracker.update_progress(i)
        time.sleep(0.1)
    tracker.done()


if __name__ == "__main__":
    test_tqdm_tracker()
