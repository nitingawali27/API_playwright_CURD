import pytest
import json
from Utilities.api_client import APIClient
from Utilities.api_url import DELETE_USER_URL, GET_USERS_URL, POST_USER_URL, PUT_USER_URL
from Utilities.payload import APIPayloads
from Utilities.common_verifications import *
from Utilities.logger import logger  # use the logger you already created

@pytest.mark.usefixtures("playwright")
class TestAPI:

    @pytest.fixture(autouse=True)
    def init_client(self, playwright):
        """
        Initialize API client with Playwright request context for all tests in this class.
        """
        self.client = APIClient(
            request=playwright.request.new_context(
                extra_http_headers={
                    "x-api-key": "reqres-free-v1",
                    "Content-Type": "application/json"
                }
            )
        )
        logger.info("API Client initialized with Playwright request context.")        
        yield
        # Dispose request context after all tests
        self.client.request.dispose()
        logger.info("API Client request context disposed.")
        

    # -----------------------------
    # GET Request Test
    # -----------------------------
    def test_get_users(self):
        logger.info("Starting GET Users test...")
        response = self.client.get(GET_USERS_URL)
        data = response.json()
        logger.info(f"GET Users response:\n{json.dumps(data, indent=4)}")
        verify_http_status_code(response, 200)
        verify_response_key(data.get("page"), 2, "page")
        verify_json_key_not_null(data.get("per_page"), "per_page")
        verify_json_key_not_null(data.get("total"), "total")
        logger.info("GET Users test completed successfully.")
        

    # -----------------------------
    # POST Request Test
    # -----------------------------
    def test_post_user(self):
        logger.info("Starting POST User test...")
        payload = APIPayloads.get_post_payload()
        response = self.client.post(POST_USER_URL, payload)
        data = response.json()
        logger.info(f"POST User payload: {payload}\nResponse:\n{json.dumps(data, indent=4)}")
        verify_http_status_code(response, 201)
        verify_response_key(data.get("name"), payload["name"], "name")
        verify_json_key_not_null(data.get("id"), "id")
        logger.info("POST User test completed successfully.")
        

    # -----------------------------
    # PUT Request Test
    # -----------------------------
    def test_put_user(self):
        logger.info("Starting PUT User test...")
        payload = APIPayloads.get_put_payload()
        response = self.client.put(PUT_USER_URL, payload)
        data = response.json()
        logger.info(f"PUT User payload: {payload}\nResponse:\n{json.dumps(data, indent=4)}")
        verify_http_status_code(response, 200)
        verify_response_key(data.get("job"), payload["job"], "job")
        verify_json_key_not_null(data.get("updatedAt"), "updatedAt")
        logger.info("PUT User test completed successfully.")

    # -----------------------------
    # DELETE Request Test
    # -----------------------------
    def test_delete_user(self):
        logger.info("Starting DELETE User test...")
        response = self.client.delete(DELETE_USER_URL)
        verify_http_status_code(response, 204)
        logger.info("DELETE request successful with empty response body.")
