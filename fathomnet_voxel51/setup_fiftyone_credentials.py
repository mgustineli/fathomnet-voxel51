"""
Shared utility to configure FiftyOne Enterprise credentials from .env.

This module sets up FiftyOne credentials from prefixed environment variables
(MURILO_* or PRERNA_*) to the standard FIFTYONE_API_URI and FIFTYONE_API_KEY
that the FiftyOne library expects.
"""

import os


def setup_fiftyone_credentials(deployment: str = "murilo"):
    """
    Set FiftyOne credentials from prefixed environment variables.

    Args:
        deployment: Which deployment to use ("murilo" or "prerna")

    Raises:
        ValueError: If required environment variables are not found
    """
    prefix = deployment.upper()
    uri_key = f"{prefix}_FIFTYONE_API_URI"
    api_key = f"{prefix}_FIFTYONE_API_KEY"

    uri = os.getenv(uri_key)
    key = os.getenv(api_key)

    if not uri or not key:
        raise ValueError(
            f"Missing credentials for deployment '{deployment}'. "
            f"Expected {uri_key} and {api_key} in .env file."
        )

    os.environ["FIFTYONE_API_URI"] = uri
    os.environ["FIFTYONE_API_KEY"] = key
    print(f"Using FiftyOne deployment: {deployment} ({uri})")
