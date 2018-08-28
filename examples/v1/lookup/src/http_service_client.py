import json
import requests
import logging


class HttpServiceClient:
    def __init__(self, host, resource):
        self.logger = logging.getLogger('HttpServiceClient')
        self.logger.info(
            'Creating an instance of HttpServiceClient: -h: %s -r: %s' % (
                host, resource
            )
        )
        self.host = host
        self.resource = resource

    def get_item(self, item_id):
        return self.get_item_override(item_id)

    def get_item_override(self):
        raise NotImplementedError()

    def is_successful_response(self, response):
        return response.status_code // 100 == 2

    def retrieve_item(self, item_id):
        url = self.get_full_url()
        item_url = self._join_url_chunks(url, item_id)
        print(item_url)
        return requests.get(item_url)

    def get_full_url(self):
        clean_host = self._clean_url_chunk(self.host)
        clean_resource = self._clean_url_chunk(self.resource)
        return self._join_url_chunks(clean_host, clean_resource)

    def _join_url_chunks(self, *chunks):
        return '/'.join(str(chunk) for chunk in chunks)

    def _clean_url_chunk(self, chunk):
        return str(chunk).strip('/')
