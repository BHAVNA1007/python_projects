def validate_id(value):
    if value.isdigit() and int(value) > 0:
        return True
    return False


def validate_required(value):
    if value.strip():
        return True
    return False


def validate_rating(value):
    try:
        rating = float(value)

        if 0 <= rating <= 10:
            return True

        return False

    except ValueError:
        return False


def validate_release_year(value):
    try:
        year = int(value)

        if 1888 <= year <= 2026:
            return True

        return False

    except ValueError:
        return False    


def validate_choice(value, min_value, max_value):
    if value.isdigit():
        choice = int(value)

        if min_value <= choice <= max_value:
            return True

    return False


def validate_status(value):
    allowed_status = ["Want to Watch", "Watched"]

    if value in allowed_status:
        return True

    return False
    

