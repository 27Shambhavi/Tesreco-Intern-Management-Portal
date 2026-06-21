import copy


intern = {

    "name": "Vaibhav",

    "projects": [

        "Flask",

        "Machine Learning"

    ]

}

# Shallow Copy
shallow_copy = copy.copy(intern)

# Deep Copy
deep_copy = copy.deepcopy(intern)

shallow_copy["projects"].append("Python")

print("Original Dictionary")
print(intern)

print("\nShallow Copy")
print(shallow_copy)

print("\nDeep Copy")
print(deep_copy)