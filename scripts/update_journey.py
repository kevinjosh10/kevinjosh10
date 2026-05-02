import datetime
import re

# Configuration
# Setting start date to March 1, 2026 so that May 2, 2026 is Day 62
START_DATE = datetime.date(2026, 3, 1) 
TOTAL_DAYS = 1000

def generate_progress_bar(current, total, length=25):
    percent = current / total
    filled_length = int(length * percent)
    bar = '█' * filled_length + '░' * (length - filled_length)
    
    percent_to_go = 100.0 - (percent * 100)
    
    return f"**[{bar}] {current}/{total} — Just {percent_to_go:.1f}% to go! 🚀**"

def main():
    today = datetime.date.today()
    days_passed = (today - START_DATE).days
    
    # Cap between 0 and 1000
    days_passed = max(0, min(days_passed, TOTAL_DAYS))
    
    progress_bar = generate_progress_bar(days_passed, TOTAL_DAYS)
    
    # Read README.md
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace the progress bar section, handling spaces carefully
    pattern = r"(<!-- JOURNEY_BAR_START -->\n).*?(\n\s*<!-- JOURNEY_BAR_END -->)"
    replacement = f"\\g<1>  {progress_bar}\\g<2>"
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"Updated journey progress to Day {days_passed}")

if __name__ == "__main__":
    main()
