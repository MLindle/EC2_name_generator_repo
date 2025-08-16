# EC2 Name Generator
A small Python script that generates random, human-readable EC2 instance names. Names are prefixed by a **department** and the literal `-EC2-`, followed by a 9-character random token.
Example output:

## How it works
- Prompts for:
  1. **Number of names** to generate (`int`)
  2. **Department name** (`Marketing`, `Accounting`, or `FinOps`, case-sensitive)
- Each token is 3 repeated groups of: **digit 1–9** + **uppercase A–Z** + **lowercase a–z** (ASCII ranges 65–90 for uppercase, 97–122 for lowercase).
- Final format: `<Department>-EC2-<dUl dUl dUl>` (9 characters after the dash).
## Input & Validation
- **total_names**: must be an integer. If conversion fails, the script prints an error and exits.
- **department_name**:
  - Must be exactly one of `Marketing`, `Accounting`, or `FinOps` (case-sensitive).
  - Additional case rules in the script:
    - First character **must be uppercase** for all departments.
    - For `FinOps`, the **4th character** (`O`) must also be uppercase.
  - If validation fails, an error is printed and the script exits.
> Note: The script currently excludes the digit `0` (uses `1–9`).
## Requirements
- Python 3.x
No third-party packages required.
## Usage
From the repository root:
```bash
python ec2_name_generator.py

