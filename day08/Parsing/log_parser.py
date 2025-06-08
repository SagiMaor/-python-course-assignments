import re
from datetime import datetime, timedelta
from collections import defaultdict

TIME_FORMAT = "%H:%M"

def parse_log(file_path):
    with open(file_path, 'r') as f:
        content = f.read().strip()

    days = content.split("\n\n")
    parsed_days = []

    for day in days:
        lines = day.strip().split("\n")
        entries = []

        for line in lines:
            match = re.match(r"(\d{2}:\d{2}) (.+)", line)
            if match:
                time_str, activity = match.groups()
                entries.append((datetime.strptime(time_str, TIME_FORMAT), activity.strip()))

        parsed_days.append(entries)

    return parsed_days

def compute_blocks(entries):
    blocks = []
    for i in range(len(entries) - 1):
        start_time, activity = entries[i]
        end_time, _ = entries[i + 1]
        blocks.append((start_time, end_time, activity))
    return blocks

def format_block(start, end, activity):
    return f"{start.strftime(TIME_FORMAT)}-{end.strftime(TIME_FORMAT)} {activity}"

def summarize_activities(blocks_by_day):
    summary = defaultdict(timedelta)

    for blocks in blocks_by_day:
        for start, end, activity in blocks:
            summary[activity] += (end - start)

    return summary

def format_summary(summary_dict):
    total_time = sum(summary_dict.values(), timedelta())
    lines = []

    for activity, duration in sorted(summary_dict.items(), key=lambda x: -x[1]):
        minutes = int(duration.total_seconds() / 60)
        percent = round(100 * duration / total_time)
        lines.append(f"{activity:<25} {minutes:>3} minutes   {percent:>2}%")

    return lines
