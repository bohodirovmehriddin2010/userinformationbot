def start(**kwargs):
    info = ''

    info += f"first_name: {kwargs['first_name']}\n"
    info += f"User id: {kwargs['user_id']}\n"
    info += f"username: {kwargs['username']}\n"

    return info
