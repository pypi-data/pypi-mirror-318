from pygeai.core.common.exceptions import WrongArgumentError


def get_messages(message_list: list):
    """
    Processes a list of message dictionaries and extracts the "role" and "content" fields.

    :param message_list: list - A list of dictionaries, where each dictionary must contain the keys "role" and "content".
    :return: list - A list of dictionaries, each containing the "role" and "content" fields extracted from the input.
    :raises WrongArgumentError: If a dictionary in the list is not in the expected format or missing the required keys.
    """
    messages = []
    if any(message_list):
        try:
            for message_dict in message_list:
                messages.append({
                    "role": message_dict['role'],
                    "content": message_dict['content']
                })
        except ValueError as e:
            raise WrongArgumentError(
                "Each message must be in JSON format: '{\"role\": \"user\", \"content\": \"message content\"}' "
                "Each dictionary must contain role and content")

    return messages
