from multiprocessing import Process


def generate_performance_report(name):

    print(f"Performance Report Generated for {name}")


if __name__ == "__main__":

    interns = [

        "Vaibhav",

        "Khushi",

        "Raushan"

    ]

    processes = []

    for intern in interns:

        process = Process(

            target=generate_performance_report,

            args=(intern,)

        )

        processes.append(process)

        process.start()

    for process in processes:

        process.join()

    print("\nAll Performance Reports Generated Successfully")