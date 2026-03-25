def paginate(data, page, limit):
    total = len(data)
    start = (page - 1) * limit
    end = start + limit

    return {
        "data": data[start:end],
        "total": total,
        "page": page,
        "limit": limit
    }