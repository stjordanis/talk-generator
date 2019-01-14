import time

from talkgenerator import run
from talkgenerator.util import os_util


def run_time_test(number_of_times):
    words = os_util.read_lines("../data/eval/common_words.txt")[0:number_of_times]
    result_file = open("../data/eval/timings.txt", "a+")

    for topic in words:
        arguments = run.get_argument_parser().parse_args(
            ['--topic', topic, '--num_slides', '7', '--save_ppt', 'False', '--open_ppt', 'False'])

        start = time.process_time()
        clock_start = time.perf_counter()

        run.main(arguments)

        end = time.process_time()
        clock_end = time.perf_counter()
        timing = end - start
        clock_timing = clock_end - clock_start
        print("It took {} seconds to generate the presentation, and {} seconds system-wide ".format(str(timing),
                                                                                                    str(clock_timing)))
        result_file.write(topic + ", " + str(timing) + ", " + str(clock_timing) + '\n')
        result_file.flush()

    result_file.close()
