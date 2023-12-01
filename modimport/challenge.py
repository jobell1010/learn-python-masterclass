import time

time_info = time.get_clock_info('time')
mono_info = time.get_clock_info('monotonic')
perf_info = time.get_clock_info('perf_counter')
process_info = time.get_clock_info('process_time')

print(time_info)
print(perf_info)
print(mono_info)
print(process_info)
