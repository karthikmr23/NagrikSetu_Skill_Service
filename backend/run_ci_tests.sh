#!/usr/bin/env bash
set -e

# Ensure backend directory is in PYTHONPATH for robust module resolution
export PYTHONPATH=".:${PYTHONPATH}"

# Run core functional & integration tests verified against MySQL
python -m pytest \
  tests/test_skill_service.py::test_health_check_mysql \
  tests/test_skill_service.py::test_auth_and_citizen_isolation \
  tests/test_skill_service.py::test_duplicate_enrolment_and_batch_capacity \
  tests/test_skill_service.py::test_citizen_skill_profile_and_proficiency_validation \
  tests/test_skill_service.py::test_skill_gap_analysis_and_training_mapping \
  -v --tb=short
