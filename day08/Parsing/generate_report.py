from log_parser import parse_log, compute_blocks, format_block, summarize_activities, format_summary

def main():
    log_file = "examples/regex/timelog.log"
    output_file = "examples/regex/timelog.txt"

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
