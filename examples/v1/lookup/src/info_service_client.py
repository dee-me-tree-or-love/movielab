import src.config.info as info_service
import logging

from .http_service_client import HttpServiceClient


class InfoServiceClient(HttpServiceClient):
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        super().__init__(info_service.HOST, info_service.RESOURCE)

    def get_item_override(self, item_id):
        response = super().retrieve_item(item_id)
        if super().is_successful_response(response):
            return response.json()
        return {}

