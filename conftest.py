# file: conftest.py
# version: 1.0.0
# guid: 3f8b1d47-6c29-4a05-8e73-b91d2c4f6a08
# last-edited: 2026-07-20

"""Root pytest configuration.

This is a Rust project. The only Python that ships here is the self-contained
``scripts/copilot-firewall`` sub-tool, which ``pytest.ini`` excludes because it
has its own project definition and dependencies. The root test run therefore
collects nothing, which is the correct and expected outcome — not a failure.

pytest signals an empty collection with exit code 5, and CI treats any non-zero
exit as a failed job. This narrows that one case to success while leaving every
genuine failure (exit 1, 2, 3, 4) untouched.
"""

import pytest

PYTEST_NO_TESTS_COLLECTED = 5


def pytest_sessionfinish(session: pytest.Session, exitstatus: int) -> None:
    """Treat "no tests collected" as success, since there are none to collect."""
    if exitstatus == PYTEST_NO_TESTS_COLLECTED:
        session.exitstatus = 0
