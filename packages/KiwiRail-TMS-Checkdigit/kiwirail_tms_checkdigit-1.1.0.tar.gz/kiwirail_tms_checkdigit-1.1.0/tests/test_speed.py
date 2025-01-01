import cProfile

def test_speed(self):
    print(f"\nSystem Specs: OS={platform.system()}, Processor={platform.processor()}, Architecture={platform.machine()}, CPU Count={os.cpu_count()}, Python={platform.python_version()}")
    
    def calculate_check_digit_multiple_times():
        for example in self.examples:
            calculate_check_digit(example[:-1])

    profiler = cProfile.Profile()
    profiler.enable()
    start_time = time.time()
    iterations = 0
    while time.time() - start_time < 0.1:
        calculate_check_digit_multiple_times()
        iterations += len(self.examples)
    profiler.disable()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Performance Results: {iterations} iterations in {(elapsed_time*1000):.0f}ms, Average time per iteration: {(elapsed_time / iterations) * (1000000):.1f}us")
    profiler.print_stats(sort='cumulative')
