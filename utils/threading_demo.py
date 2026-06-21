import threading
import time


def attendance_processing():

    for i in range(5):

        print("Attendance Processing...")

        time.sleep(1)


def certificate_generation():

    for i in range(5):

        print("Certificate Generation...")

        time.sleep(1)


thread1 = threading.Thread(

    target=attendance_processing

)

thread2 = threading.Thread(

    target=certificate_generation

)


thread1.start()

thread2.start()


thread1.join()

thread2.join()


print("\nBoth Tasks Completed Successfully")