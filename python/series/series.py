def slices(series, length):
    if len(series) < length:
        raise ValueError("error")
    if length <= 0:
        raise ValueError("error")

    resp = []

    for i in range(0, len(series) - length + 1):
        resp.append(series[i:i+length])

    return resp
