import time
from concurrent.futures import ThreadPoolExecutor, as_completed


class Runner:
    def __init__(self, max_workers=6) -> None:
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def run(self, process, elements) -> None:
        futures = []
        for element in elements:
            feature = self.executor.submit(process, element)
            futures.append(feature)
        for future in as_completed(futures):
            pass
