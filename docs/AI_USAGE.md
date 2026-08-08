# AI Usage Guide

## Primary Use Cases

This repository supports:

1. Professional resume generation
2. Company-specific resume generation
3. Company-specific placement preparation
4. Interview preparation
5. Project explanation
6. Skill-gap analysis
7. Learning-roadmap updates
8. Career decision support

## Read Order

For most tasks:

1. Read `AI_CONTEXT.md`.
2. Read the relevant canonical YAML files.
3. Read project `facts.yaml` before project `README.md`.
4. Apply `resume/instructions.md` when generating resume content.

## Company-Specific Placement Workflow

When a company is announced:

1. Read the actual JD/eligibility information supplied by Shabaz.
2. Extract role requirements and selection stages.
3. Map requirements to `VERIFIED` skills/projects/experience.
4. Identify gaps.
5. Create a prioritized preparation plan.
6. Generate role-specific interview questions.
7. Tailor the resume without inventing facts.

## Resume Workflow

The user may supply a custom prompt. Follow the prompt for:

- length
- layout
- tone
- target role
- project selection
- ordering
- ATS strategy

Repository facts remain the source of truth.

## Conflict Resolution

If a new user statement conflicts with an older repository fact:

- do not silently choose one;
- identify the conflict;
- prefer the newest explicit user confirmation if it is clearly a correction;
- record the change in the relevant source file and, where useful, `docs/CHANGELOG.md`.

## AEGIS Architecture Lock

Do not alter the AEGIS baseline architecture without explicitly flagging:

> ARCHITECTURE CHANGE PROPOSED

and documenting:

- current architecture
- proposed change
- reason
- technical impact
- affected documents
- implementation impact
- approval status
