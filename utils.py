"""This file contains utility functions"""


def get_user_ava_path(instance: 'participant.Client', filename: str) -> str:
    """This function returns the path for the current user avatar image
    :param instance: an instance of the Client model
    :param filename: a string representing the name of the image file
    :return: a string representing the path for the user avatar image
    """
    return f'ava/{instance.email}/{filename}'
