"""
Constants that are used in the rest of the system
"""
import enum


class ApiEnvironment:
    """
    Which environment you are hitting. By default you should be using PROD_API_URL

    Examples
    --------
    >>> from rhino_health import ApiEnvironment.LOCALHOST_API_URL, ApiEnvironment.DEV_URL, ApiEnvironment.PROD_API_URL, ApiEnvironment.DEMO_DEV_URL
    """

    LOCALHOST_API_URL = "http://localhost:8080/api/"
    QA_URL = "https://qa-cloud.rhinohealth.com/api/"
    DEV_URL = "https://dev.rhinohealth.com/api/"
    DEV2_URL = "https://dev2.rhinohealth.com/api/"
    DEV3_URL = "https://dev3.rhinohealth.com/api/"
    DEV4_URL = "https://dev4.rhinofcp.com/api/"
    DEMO_DEV_URL = "https://demo-dev.rhinohealth.com/api/"
    DEMO_URL = "https://demo-prod.rhinohealth.com/api"
    PROD_API_URL = "https://prod.rhinohealth.com/api/"
    PROD_GCP_URL = "https://prod.rhinofcp.com/api/"


class Dashboard:
    """
    Which dashboard serves the environment
    """

    LOCALHOST_URL = "http://localhost:3000"
    DEV_URL = "https://dev-dashboard.rhinohealth.com"
    DEV4_URL = "https://dev4-dashboard.rhinofcp.com"
    DEMO_DEV_URL = "https://demo-dev-dashboard.rhinohealth.com"
    DEMO_URL = "https://demo.rhinohealth.com"
    PROD_URL = "https://dashboard.rhinohealth.com"
    PROD_GCP_URL = "https://dashboard.rhinofcp.com"


class ECRService:
    """
    Which ecr serves the environment
    """

    TEST_URL = "localhost:5201"
    LOCALHOST_URL = "localhost:5001"
    DEV_URL = "913123821419.dkr.ecr.us-east-1.amazonaws.com"
    DEMO_DEV_URL = "913123821419.dkr.ecr.us-east-1.amazonaws.com"
    DEMO_URL = "913123821419.dkr.ecr.us-east-1.amazonaws.com"
    PROD_URL = "913123821419.dkr.ecr.us-east-1.amazonaws.com"


BASE_URL_TO_DASHBOARD = {
    ApiEnvironment.LOCALHOST_API_URL: Dashboard.LOCALHOST_URL,
    ApiEnvironment.DEV_URL: Dashboard.DEV_URL,
    ApiEnvironment.DEV2_URL: Dashboard.DEV_URL,
    ApiEnvironment.DEV3_URL: Dashboard.DEV_URL,
    ApiEnvironment.DEV4_URL: Dashboard.DEV4_URL,
    ApiEnvironment.DEMO_DEV_URL: Dashboard.DEMO_DEV_URL,
    ApiEnvironment.DEMO_URL: Dashboard.DEMO_URL,
    ApiEnvironment.PROD_API_URL: Dashboard.PROD_URL,
    ApiEnvironment.PROD_GCP_URL: Dashboard.PROD_GCP_URL,
}
"""
Mapping of Base URL to Dashboard
"""


class CloudProvider(str, enum.Enum):
    AWS = "aws"
    GCP = "gcp"
