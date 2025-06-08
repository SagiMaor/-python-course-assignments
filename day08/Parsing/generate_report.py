from log_parser import parse_log, compute_blocks, format_block, summarize_activities, format_summary

def main():
    log_file = "examples/regex/timelog.log"
    parsed_days = parse_log(log_file)

    all_blocks = []

    for day in parsed_days:
        blocks = compute_blocks(day)
        all_blocks.append(blocks)

        for start, end, activity in blocks:
            print(format_block(start, end, activity))
        print()  # blank line between days

    summary = summarize_activities(all_blocks)
    print("\n" + "\n".join(format_summary(summary)))

if __name__ == "__main__":
    main()
