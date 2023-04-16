import os

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.serverless import serverless_function

SENTRY_DSN = os.environ.get('SENTRY_DSN')


def init_sentry():
    """Initialize sentry, if SENTRY_DSN is set"""

    if not SENTRY_DSN:
        return

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[
            FlaskIntegration(),
        ],
        traces_sample_rate=1.0,
        send_default_pii=True,
    )


__ALL__ = [init_sentry, serverless_function]
