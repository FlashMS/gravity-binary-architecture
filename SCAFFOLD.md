# Gravity Binary Architecture — Scaffold Overview

This document provides a high-level overview of the repository structure for
the Gravity Binary Architecture (v0.1). It is intended as a quick reference
for contributors, reviewers, and anyone exploring the system layout.

## Core Architecture (/core)

The deterministic execution engine and foundational reasoning components:

## Reflex API (/GravityBinaryReflexAPI)

C# API surface for interacting with the architecture:

## Validators and Capsules

## Registry

## Projects (/projects)

Example or experimental project validators:

Each contains a validator.json file.

## Site and Public Assets

## Audit and Introspection Logs

These files capture execution traces, reactions, and trust evaluations:

## Utility

## Status

This scaffold represents the v0.1 architecture layout.
Higher-level layers (Reflex, Trust Engine, Registry v2, etc.) will build on top
of this foundation in future versions.
