# payloads_config.py

class APIPayloads:
    """
    Class to store and manage API payloads
    """

    @staticmethod
    def get_post_payload():
        """
        Payload for creating a new user (POST)
        """
        return {
            "name": "morpheus",
            "job": "leader"
        }

    @staticmethod
    def get_put_payload():
        """
        Payload for updating an existing user (PUT)
        """
        return {
            "name": "morpheus",
            "job": "zion resident"
        }
