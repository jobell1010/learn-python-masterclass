from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """Copy a dictionary, creating copies of the `list` or `dict` values

    The function will crash with an AttributeError is the values aren't
    lists or dictionaries.

    :param d: The dictionary to copy
    :return: A copy of `d`, with the values being copies of the original
    """
    new_dict = {}
    for key in d:
        values = d[key]
        new_value = values.copy()
        new_dict[key] = new_value

    return new_dict


recipes_copy = my_deepcopy(recipes)
print(recipes_copy)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
