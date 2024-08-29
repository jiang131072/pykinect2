"""Generate Python enum definition from C++ enum definition"""

import re


# WARN: This can't deal with HandType Enum, its cpp define is not standard
def cpp2py_enum(cpp_str):
    py_keywords = ["None", "False", "True"]

    search_name = re.search(r"typedef enum _(\w+)", cpp_str)
    if not search_name:
        raise ValueError("Invalid C++ enum definition")

    name = search_name.group(1)
    members = re.findall(r"_(\w+)\s=\s(\w+)", cpp_str)
    if not members:
        raise ValueError("No members found")

    py_str = f"class {name}(_Enum):\n"
    for mem_key, mem_val in members:
        if mem_key in py_keywords:
            mem_key += "_"
        py_str += f"    {mem_key} = {mem_val}\n"

    return py_str


path = input("Enter output path: ")
while (q := input("Enter C++ enum definition:\n")) != "q":
    py_str = cpp2py_enum(q)
    with open(path, "a") as f:
        f.write(py_str)
        f.write("\n\n")
