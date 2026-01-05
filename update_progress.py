import re

def update_readme():
    # 1. Read the current README
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # 2. Count all occurrences of [x]
    total_completed = content.count("[x]")

    # 3. Update the "Total Rooms" line at the bottom of the table
    # This looks for the line starting with "| Total Rooms:" and replaces the number after "= "
    new_content = re.sub(
        r"(\| \*\*Total Rooms:\*\*.*\|= )\*\*+= \d+\*\*", 
        f"\\1**= {total_completed}**", 
        content
    )

    # 4. Save the changes back to the file
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_readme()
