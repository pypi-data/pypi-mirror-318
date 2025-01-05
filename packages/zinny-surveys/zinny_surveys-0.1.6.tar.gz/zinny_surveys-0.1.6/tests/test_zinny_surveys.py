"""Tests for the zinny_surveys module."""

import os
import json
from unittest.mock import patch, MagicMock
import pytest
# from importlib import resources
from zinny_surveys import (
    list_file_types,
    list_scopes,
    list_files,
    list_surveys,
    load_file,
    load_survey,
    validate_survey_file,
    save_file,
)

# pylint: disable=redefined-outer-name,unused-argument,missing-function-docstring

# Mocking resources for tests
@pytest.fixture
def mock_resources():
    with patch("zinny_surveys.resources") as mock_resources:
        yield mock_resources

# Test Data
SURVEY_SAMPLE = {
    "id": "vfx",
    "name": "Visual Effects Assessment",
    "criteria": [
        {"id": "artistry", "name": "Artistry", "range": [1, 10]},
        {"id": "technical", "name": "Technical Achievement", "range": [1, 10]}
    ]
}

@pytest.fixture
def mock_file_structure(mock_resources, tmp_path):
    """Mock a file structure for surveys and weights."""
    data_dir = tmp_path / "data"

    surveys_dir = data_dir / "surveys"
    surveys_shared = surveys_dir / "shared"
    surveys_local = surveys_dir / "local"

    weights_dir = data_dir / "weights"
    weights_shared = weights_dir / "shared"
    weights_local = weights_dir / "local"

    # Create directories
    surveys_shared.mkdir(parents=True)
    surveys_local.mkdir(parents=True)
    weights_shared.mkdir(parents=True)
    weights_local.mkdir(parents=True)

    # Create sample files
    survey_file = surveys_shared / "vfx_test_survey.json"
    survey_file.write_text(json.dumps(SURVEY_SAMPLE))

    # Mock the resource path
    mock_resources.files.return_value = MagicMock()
    mock_resources.files.return_value.joinpath.side_effect = lambda x: tmp_path / x

    yield tmp_path

# Tests
def test_list_file_types(mock_file_structure):
    """Test listing file types."""
    result = list_file_types()
    assert "surveys" in result
    assert "weights" in result

def test_list_scopes(mock_file_structure):
    """Test listing scopes for a file type."""
    result = list_scopes("surveys")
    assert "shared" in result
    assert "local" in result

def test_list_files(mock_file_structure):
    """Test listing files in a scope."""
    result = list_files("surveys", "shared")
    assert "vfx_test_survey.json" in result

def test_list_surveys(mock_file_structure):
    """Test listing surveys in a scope."""
    result = list_surveys("shared")
    assert "vfx_test_survey.json" in result

def test_load_file(mock_file_structure):
    """Test loading a file's content."""
    result = load_file("surveys", "shared", "vfx_test_survey.json")
    assert result == SURVEY_SAMPLE

def test_load_survey(mock_file_structure):
    """Test loading a survey file."""
    result = load_survey("vfx_test_survey.json", "shared")
    assert result == SURVEY_SAMPLE

def test_validate_survey_file():
    """Test validating survey file content."""
    assert validate_survey_file(SURVEY_SAMPLE) is True
    assert validate_survey_file({}) is False

def test_save_file(mock_file_structure):
    """Test saving content to a file."""
    new_content = {"id": "new_survey", "name": "New Survey", "criteria": []}
    result = save_file("surveys", "new_survey.json", new_content)
    print(result)

    # Ensure the file exists and content matches
    saved_path = mock_file_structure / "data/surveys/local/new_survey.json"
    assert os.path.exists(saved_path)
    with open(saved_path, "r", encoding="utf-8") as f:
        assert json.load(f) == new_content
