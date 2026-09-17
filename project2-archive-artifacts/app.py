from pathlib import Path


def generate_report():
    report_path = Path("report.txt")

    report_content = (
        "Application Report\n"
        "Total Users: 120\n"
        "Active Sessions: 45\n"
    )

    report_path.write_text(report_content, encoding="utf-8")

    print("Report generated successfully.")
    print(f"Report location: {report_path.resolve()}")


if __name__ == "__main__":
    generate_report()