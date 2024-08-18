import time

# Use this code as guidance to conduct your experiment.
# Design and write your experiment program in methods and call them to run the experiment.

def experiment():
    print("running experiment", end="")
    for i in range(6):
        time.sleep(1)
        print(". ", end="")
    print()

def run_experiment():
    print("call and run your experiment here")
    start = time.thread_time_ns()
    experiment()
    end = time.thread_time_ns()
    duration_nano = (end - start)/100000
    print("Duration: ",duration_nano)


def run_sample_experiment(no_experiments):
    for i in range(no_experiments):
        print("Experiment #", i+1)
        run_experiment()


run_sample_experiment(3)