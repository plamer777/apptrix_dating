
def get_user_ava_path(instance: 'participant.Client', filename: str):
    return f'ava/{instance.email}/{filename}'
