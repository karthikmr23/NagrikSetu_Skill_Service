#!/usr/bin/env bash
set -e

# Ensure backend directory is in PYTHONPATH for robust module resolution
export PYTHONPATH=".:${PYTHONPATH}"

# Run the complete test suite across all 9 backend tests
python -m pytest tests/test_skill_service.py -v --tb=short

