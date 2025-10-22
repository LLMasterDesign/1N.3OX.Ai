# GitHub Configuration

This directory contains GitHub-specific configuration files for the SunsetGlow repository.

## Files

- `workflows/tests.yml` - Automated testing workflow that runs on push and PR
  - Tests against Python 3.8, 3.9, 3.10, 3.11, 3.12
  - Verifies all imports work correctly
  - Runs the complete test suite
  - Validates demo runs successfully

## CI/CD

The test workflow ensures:
- ✅ All 35 tests pass
- ✅ Package imports work correctly
- ✅ Demo runs without errors
- ✅ Compatible with Python 3.8+
