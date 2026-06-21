def certificate_generator(intern_names):

    for name in intern_names:

        yield f"Certificate Generated for {name}"


if __name__ == "__main__":

    interns = [

        "Khushi",

        "Raushan",

        "Vaibhav"

    ]

    certificates = certificate_generator(interns)

    for certificate in certificates:

        print(certificate)