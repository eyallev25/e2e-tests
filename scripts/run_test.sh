#! /usr/bin/env bash

set -euo pipefail


poetry run pytest --junitxml "test-report.xml" --html "test-report.html"
