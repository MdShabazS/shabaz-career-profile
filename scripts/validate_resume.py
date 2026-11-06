#!/usr/bin/env python3
"""Check public resume content for required sections and accidental phone exposure.

This verifies source/output consistency and public-copy privacy. It does not assign
a universal ATS score. See resume/ats-analysis.md for the job-description workflow.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, "resume", "Mohammed_Shabaz_S_Master_Resume.pdf")
TXT = os.path.join(ROOT, "resume", "Mohammed_Shabaz_S_Master_Resume.txt")

REQUIRED = [
    "MOHAMMED SHABAZ S",
    "Software & Embedded Engineer",
    "SUMMARY",
    "TECHNICAL SKILLS",
    "EXPERIENCE",
    "PROJECTS",
    "EDUCATION",
    "CERTIFICATIONS",
    "NOKIA SOLUTIONS AND NETWORKS INDIA PRIVATE LIMITED",
    "Telecom/5G engineering roles",
    "LTE and 5G study",
]
PHONE_PATTERN = re.compile(r"(?<!\d)(?:\+?91[ -]?)?[6-9]\d{9}(?!\d)")


def main():
    try:
        import fitz
    except ImportError:
        print("PyMuPDF is required to extract text from the generated PDF.")
        sys.exit(1)

    if not os.path.exists(PDF):
        print("PDF not found. Run scripts/build_resume.py first.")
        sys.exit(1)

    doc = fitz.open(PDF)
    text = "\n".join(page.get_text() for page in doc)
    with open(TXT, "w", encoding="utf-8") as output:
        output.write(text)

    errors = []
    if doc.page_count != 1:
        errors.append(f"Expected a one-page resume; found {doc.page_count}.")
    for item in REQUIRED:
        if item not in text:
            errors.append(f"Missing required text: {item}")
    if PHONE_PATTERN.search(text):
        errors.append("A phone number appears in the public resume; remove it before publishing.")

    if errors:
        for error in errors:
            print("FAIL:", error)
        sys.exit(1)

    print("PASS: one-page public resume, required sections and Telecom/5G content found; no phone number detected.")
    print("No universal ATS score is calculated. Tailor against a specific job description.")


if __name__ == "__main__":
    main()
