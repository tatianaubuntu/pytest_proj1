def get_val(collection=dict, key=str, default='git'):
    """
    возвращает значение из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается значение default
    """
    if key in collection:
        return collection[key]
    else:
        return default
