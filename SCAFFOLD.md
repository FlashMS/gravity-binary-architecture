# Gravity Binary Architecture — Scaffold Overview

This document provides a high-level overview of the repository structure for the Gravity Binary Architecture (v0.1). It is intended as a quick reference for contributors, reviewers, and anyone exploring the system layout.

---

## Core Architecture (/core)

The deterministic execution engine and foundational reasoning components:

- intent_frame.py — Defines the Intent Frame structure
- capsule.py — Capsule abstraction and lifecycle
- validator.py — Structural and constraint validation
- constraint_engine.py — Constraint evaluation logic
- provenance.py — Execution lineage tracking
- chaining.py — Deterministic chaining of frames/capsules
- execution_engine.py — Orchestrates execution flow
- signature.py — Compatibility and signature checks
- storage.py — Lightweight state and caching utilities
- test_engine_full.py — Full-stack validation harness

---

## Reflex API (/GravityBinaryReflexAPI)

C# API surface for interacting with the architecture:

- Program.cs
- appsettings.json
- launchSettings.json
- GravityBinaryReflexAPI.csproj

---

## Validators and Capsules

- /validators — JSON-based validator definitions
- /validatorCapsule — Capsule-level validator surfaces
- capsule_registry.json — Capsule metadata registry
- capsule-reaction-history.log — Reaction and audit traces

---

## Registry

- /registry/registry.yaml — Primary registry definition
- registry_backup.json — Backup registry snapshot
- registry-v112.txt — Versioned registry export

---

## Projects (/projects)

Example or experimental project validators:

- AIInsuranceAgent
- MakeTheWorldBetter
- UCEEngine

Each contains a validator.json file.

---

## Site and Public Assets

- /site — Public-facing HTML pages
- /gravity-binary-site — Additional site assets
- index.html, Home.html, trust_index.html

---

## Audit and Introspection Logs

These files capture execution traces, reactions, and trust evaluations:

- capsule_log.txt
- capsule-reflection.log
- trigger-audit.log
- trust_audit.log
- layout-audit.log

---

## Utility

- gravity.sh — Deterministic execution helper
- dispatch-uce.json — UCE dispatch configuration

---

## Status

This scaffold represents the v0.1 architecture layout. Higher-level layers (Reflex, Trust Engine, Registry v2, etc.) will build on top of this foundation in future versions.

