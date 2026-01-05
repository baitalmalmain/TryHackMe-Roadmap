import os

def update_readme():
    # 1. Read the README
    if not os.path.exists("README.md"):
        return
        
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 2. Count every [x] in the entire file
    # This counts your progress across all categories
    total_completed = 0
    for line in lines:
        total_completed += line.count("[x]")

    # 3. Update the Statistics Table
    new_lines = []
    for line in lines:
        # We look for the row that contains "Total Rooms:"
        if "**Total Rooms:**" in line:
            # We split the row by the "|" symbol
            parts = line.split("|")
            if len(parts) >= 4:
                # parts[3] is the third column (Completed by Me)
                # We force it to update to your new count
                parts[3] = f" **= {total_completed}** "
                line = "|".join(parts)
        new_lines.append(line)

    # 4. Save the changes
    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)
    
    print(f"Successfully counted {total_completed} rooms.")

if __name__ == "__main__":
    update_readme()
