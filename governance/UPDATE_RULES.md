# Update Rules

How to change this repository without breaking it as a source of truth.

## When adding or changing a fact

1. Find the single canonical file that owns the fact (see the map in the root [`README.md`](../README.md)). Edit only that file; do not duplicate the fact elsewhere.
2. Carry a status label ([`STATUS_SYSTEM.md`](STATUS_SYSTEM.md)). New, unconfirmed items start `TO_VERIFY`.
3. Keep ownership boundaries intact: team vs individual, internship vs employment, app-side vs backend, planned vs completed.
4. If it conflicts with an existing fact, resolve using the conflict order in [`STATUS_SYSTEM.md`](STATUS_SYSTEM.md) and record the change in [`CHANGELOG.md`](CHANGELOG.md).
5. Never let a planned item drift into a completed section.

## Dates

Convert relative dates ("next month", "2 months from now") to absolute dates before saving. Re-check lifecycle labels against today's date — an `UPCOMING` internship becomes `IN_PROGRESS` on its start date and `COMPLETED` on its end date.

## AEGIS architecture

The AEGIS baseline architecture and its AI-recommends / human-decides boundary are locked. To change them, add an explicit `ARCHITECTURE CHANGE PROPOSED` section containing: current architecture, proposed change, reason, technical impact, affected documents, and approval status. Do not treat a proposal as the new baseline until Shabaz approves it.

## Confidentiality gate

Before publishing anything about Nokia or MITRA, check [`CONFIDENTIALITY.md`](CONFIDENTIALITY.md).

## Derived outputs

Resumes, portfolio copy, LinkedIn text, and interview prep are **outputs**, not sources. Generate them from the canonical files; do not edit a canonical fact to match a resume. Keep one master resume source of truth in [`../resume/master-resume.md`](../resume/master-resume.md).
