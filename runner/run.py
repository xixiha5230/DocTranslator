from concurrent.futures import ThreadPoolExecutor, as_completed


class Runner:
    def __init__(self, max_workers=12) -> None:
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def run(self, process, elements) -> None:
        futures = [self.executor.submit(process, element) for element in elements]
        for future in as_completed(futures):
            pass
