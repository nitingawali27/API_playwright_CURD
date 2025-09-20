import json
import jsonschema

# -----------------------------
# HTTP Status Code Verification
# -----------------------------
def verify_http_status_code(response, expected_code):
    """
    Verify that the HTTP response status matches expected
    """
    assert response.status == expected_code, \
        f"Expected HTTP {expected_code}, but got {response.status}"


# -----------------------------
# Verify a specific response header
# -----------------------------
def verify_response_header(response, header_name, expected_value):
    """
    Verify that a specific header in the response matches expected value
    """
    actual_value = response.headers.get(header_name)
    assert actual_value == expected_value, \
        f"Header '{header_name}' mismatch. Expected: {expected_value}, Got: {actual_value}"


# -----------------------------
# Verify JSON key-value
# -----------------------------
def verify_response_key(actual_value, expected_value, key_name=None):
    """
    Verify that a JSON key has the expected value
    """
    assert actual_value == expected_value, \
        f"Key {key_name or ''} mismatch. Expected: {expected_value}, Got: {actual_value}"


# -----------------------------
# JSON key should not be null or empty
# -----------------------------
def verify_json_key_not_null(key, key_name=None):
    """
    Ensure a JSON key is not None or empty
    """
    assert key is not None and key != "", \
        f"Key {key_name or ''} should not be null/empty"


# -----------------------------
# JSON key should be greater than zero
# -----------------------------
def verify_json_key_gr_zero(key, key_name=None):
    """
    Ensure a numeric JSON key is greater than zero
    """
    assert key > 0, f"Key {key_name or ''} should be greater than zero, but got {key}"


# -----------------------------
# Verify response contains expected text
# -----------------------------
def verify_response_contains(response, expected_text):
    """
    Verify that the response text contains the expected string
    """
    assert expected_text in response.text(), \
        f"Response does not contain expected text '{expected_text}'"


# -----------------------------
# Verify JSON schema
# -----------------------------
def verify_json_schema(response_json, schema):
    """
    Validate that the JSON response matches the provided JSON schema
    """
    try:
        jsonschema.validate(instance=response_json, schema=schema)
    except jsonschema.exceptions.ValidationError as e:
        assert False, f"JSON schema validation failed: {e.message}"
