def start_spring(**data):
    new_data = {}
    for key, value in data.items():
        new_key = value
        new_value = key
        if new_key not in new_data:
            new_data[new_key] = []

        new_data[new_key] += [new_value]

    sorted_new_data = sorted(new_data.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result = ""
    for type_, name in sorted_new_data:
        result += type_ + ":" + "\n" + "-"
        sorted_names = sorted(name, reverse=False)
        result += "\n-".join([el for el in sorted_names]) + "\n"

    return result
