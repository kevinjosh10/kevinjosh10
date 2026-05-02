import datetime
import re

# Configuration
START_DATE = datetime.date(2026, 4, 15)  # The day the 1000-day journey started
TOTAL_DAYS = 1000

def generate_progress_bar(current, total, length=25):
    percent = current / total
    filled_length = int(length * percent)
    bar = '█' * filled_length + '░' * (length - filled_length)
    return f"**[{bar}] {percent*100:.1f}%**"

def main():
    today = datetime.date.today()
    days_passed = (today - START_DATE).days
    
    # Cap between 0 and 1000
    days_passed = max(0, min(days_passed, TOTAL_DAYS))
    
    progress_bar = generate_progress_bar(days_passed, TOTAL_DAYS)
    
    status_text = f"**Day {days_passed} of {TOTAL_DAYS}** {progress_bar}"
    
    # Read README.md
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace the progress bar section
    pattern = r"(<!-- JOURNEY_BAR_START -->\n)(.*)(\n<!-- JOURNEY_BAR_END -->)"
    replacement = f"\\g<1>{status_text}\\g<3>"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Updated journey progress to Day {days_passed}")

if __name__ == "__main__":
    main()
