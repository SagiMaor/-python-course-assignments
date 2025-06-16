import os
from log_parser import parse_log, compute_blocks, format_block, summarize_activities, format_summary

def create_sample_log_file(filepath):
    sample_data = """09:20 Introduction
11:00 Exercises
11:15 Break
11:35 Numbers and strings
12:30 Lunch Break
13:30 Exercises
14:10 Solutions
14:30 Break
14:40 Lists
15:40 Exercises
17:00 Solutions
17:30 End

09:30 Lists and Tuples
10:30 Break
10:50 Exercises
12:00 Solutions
12:30 Dictionaries
12:45 Lunch Break
14:15 Exercises
16:00 Solutions
16:15 Break
16:30 Functions
17:00 Exercises
17:30 End
"""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w") as f:
        f.write(sample_data)
    print(f"📄 Sample log file created at: {filepath}")

def main():
    log_file = "examples/regex/timelog.log"
    output_file = "examples/regex/timelog.txt"

    if not os.path.exists(log_file):
        create_sample_log_file(log_file)

    parsed_days = parse_log(log_file)
    all_blocks = []
    report_lines = []

    for day in parsed_days:
        blocks = compute_blocks(day)
        all_blocks.append(blocks)

        for start, end, activity in blocks:
            line = format_block(start, end, activity)
            report_lines.append(line)
            print(line)

        report_lines.append("")  # blank line between days
        print()

    summary = summarize_activities(all_blocks)
    summary_lines = format_summary(summary)

    report_lines.extend(summary_lines)
    print("\n" + "\n".join(summary_lines))

    with open(output_file, "w") as f:
        f.write("\n".join(report_lines))
    print(f"\n✅ Report written to: {output_file}")

if __name__ == "__main__":
    main()
