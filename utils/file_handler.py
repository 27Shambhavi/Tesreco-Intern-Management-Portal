import csv


FILE_NAME = "interns.csv"


def add_record(intern_id, name, email, domain, duration):

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([

            intern_id,

            name,

            email,

            domain,

            duration

        ])

    print("Record Added Successfully")


def search_record(intern_id):

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if row and row[0] == str(intern_id):

                return row

    return None


def delete_record(intern_id):

    rows = []

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)

        for row in reader:

            if row and row[0] != str(intern_id):

                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerows(rows)

    print("Record Deleted Successfully")


if __name__ == "__main__":

    add_record(

        "TES001",

        "Vaibhav",

        "vaibhav@gmail.com",

        "Data Science",

        6

    )

    print(search_record("TES001"))