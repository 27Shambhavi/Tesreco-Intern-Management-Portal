from abc import ABC, abstractmethod


class Report(ABC):

    @abstractmethod
    def generate_report(self):
        pass


class AttendanceReport(Report):

    def generate_report(self):

        print("Attendance Report Generated Successfully")


class PerformanceReport(Report):

    def generate_report(self):

        print("Performance Report Generated Successfully")


if __name__ == "__main__":

    attendance = AttendanceReport()
    attendance.generate_report()

    performance = PerformanceReport()
    performance.generate_report()