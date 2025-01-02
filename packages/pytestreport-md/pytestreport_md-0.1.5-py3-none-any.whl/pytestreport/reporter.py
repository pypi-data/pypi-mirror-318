from datetime import datetime

def generate_report_pytest(prefix: str = "pytest", test_results: str = "", output_file: str = "report.md") -> None:
    """
    Generates a test report formatted with emojis.

    Args:
        test_results (str): Test results in the format 'name - status | name - status'.
        output_file (str): Name of the file where the report will be saved. Default: 'report.md'.
    """
    emoji_map = {"PASSED": "✅", "FAILED": "❌"}
    passed_tests, failed_tests = [], []

    for result in test_results.split(" | "):
        name, status = result.split(" - ")
        if status in emoji_map:
            (passed_tests if status == "PASSED" else failed_tests).append(name)

    total_tests = len(passed_tests) + len(failed_tests)
    report = (
        f"## Test Report - `{prefix}`\n"
        "--------------------------------------------------\n"
        "### :memo: Test results\n\n"
        f"**Total Tests**: {total_tests}\n"
        f"**Passed**: {len(passed_tests)} ✅\n"
        f"**Failed**: {len(failed_tests)} ❌\n\n"
        f"### Passed Tests ✅\n" + "\n".join([f"- {test}" for test in passed_tests]) +
        f"\n\n### Failed Tests ❌\n" + "\n".join([f"- {test}" for test in failed_tests]) +
        "\n--------------------------------------------------\n"
        "### :bar_chart: Test Summary\n\n"
        f"- **Passed Tests**: {len(passed_tests)} ✅\n"
        f"- **Failed Tests**: {len(failed_tests)} ❌\n"
        f"\n---\n_Report styled with ❤️ for `{prefix}` on {datetime.now().strftime('%d-%b-%Y at %H:%M:%S')}_\n"
    )

    with open(output_file, "w") as file:
        file.write(report)
