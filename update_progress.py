import re

def update_readme():
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Define the sections and their exact headings in the README
    # The key is the link name in the table, the value is the heading name
    sections = {
        "Introductory Rooms": "## Intro Rooms",
        "Linux Fundamentals": "## Linux Fundamentals",
        "Windows Fundamentals": "## Windows Fundamentals",
        "Basic Rooms": "## Basics Rooms",
        "Reconnaissance": "## Recon",
        "Scripting": "## Scripting",
        "Networking": "## Networking",
        "Tooling": "## Tooling",
        "Container Security": "## Container Security",
        "Cryptography & Hashes": "## Cryptography & Hashes",
        "Steganography": "## Steganography",
        "Web": "## Web",
        "Android": "## Android",
        "Forensics": "## Forensics",
        "Wifi Hacking": "## Wi-Fi Hacking",
        "Reverse Engineering": "## Reverse Engineering",
        "Malware Analysis": "## Malware Analysis",
        "Privilege Escalation": "## PrivEsc",
        "Windows": "## Windows",
        "Active Directory": "## Active Directory",
        "PCAP Analysis": "## PCAP Analysis",
        "Buffer Overflow": "## BufferOverflow",
        "Easy CTF": "## Easy CTF",
        "Medium CTF": "## Medium CTF",
        "Hard CTF": "## Hard CTF",
        "Insane CTF": "## Insane CTF",
        "Misc": "## Misc",
        "Special Events": "## Special Events"
    }

    # 2. Split content into parts to count [x] per section
    # We count how many [x] appear between one heading and the next
    section_counts = {}
    content_parts = re.split(r'(## .*)', content)
    
    current_heading = ""
    for part in content_parts:
        if part.startswith("## "):
            current_heading = part.strip()
        elif current_heading:
            count = part.count("[x]")
            # Find which category this heading belongs to
            for cat_name, heading in sections.items():
                if heading == current_heading:
                    section_counts[cat_name] = section_counts.get(cat_name, 0) + count

    # 3. Update the Table of Contents rows
    lines = content.splitlines()
    updated_lines = []
    total_completed = 0

    for line in lines:
        new_line = line
        # Check if the line is a table row (starts and ends with |)
        if line.startswith("|") and "[" in line and "](#" in line:
            for cat_name, count in section_counts.items():
                if f"[{cat_name}]" in line:
                    # Update the count in the 3rd column
                    parts = line.split("|")
                    if len(parts) >= 4:
                        parts[3] = f"            {count}                "
                        new_line = "|".join(parts)
                        total_completed += count
        
        # 4. Update the Grand Total line at the bottom
        if "**Total Rooms:**" in line:
            parts = line.split("|")
            if len(parts) >= 4:
                parts[3] = f"          **= {total_completed}** "
                new_line = "|".join(parts)

        updated_lines.append(new_line)

    # 5. Save the updated README
    with open("README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(updated_lines))

if __name__ == "__main__":
    update_readme()
