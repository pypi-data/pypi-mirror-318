import pytest
from pytestreport.reporter import generate_report_pytest

def test_add_emojis_to_report(tmp_path):
    test_results = "test_1 - PASSED | test_2 - FAILED"
    output_file = tmp_path / "report.md"
    name = "My project"
    generate_report_pytest(prefix=name, test_results=test_results, output_file=output_file)
    
    with open(output_file) as f:
        content = f.read()
    
    assert "✅" in content
    assert "❌" in content
