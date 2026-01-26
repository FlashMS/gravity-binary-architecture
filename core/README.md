# ?? **core/README.md — Gravity Binary Core Architecture (v0.1)**

## **Overview**
The /core directory contains the foundational execution and reasoning components of the Gravity Binary architecture. These modules define how intent is framed, validated, constrained, executed, chained, and traced. Everything else in the system builds on top of this layer.

## **Module Breakdown**

### **intent_frame.py**
Defines the Intent Frame, the atomic reasoning unit of Gravity Binary.

### **capsule.py**
Implements Capsules — wrappers around executable logic with metadata and lifecycle hooks.

### **validator.py**
Validates Intent Frames and Capsules for structural correctness and constraint satisfaction.

### **constraint_engine.py**
Evaluates and enforces constraints attached to frames or capsules.

### **provenance.py**
Tracks the lineage of every execution step.

### **chaining.py**
Implements deterministic chaining of frames and capsules.

### **signature.py**
Defines execution signatures for compatibility checks.

### **storage.py**
Provides lightweight storage utilities for state passing and caching.

### **execution_engine.py**
The orchestrator for executing frames and capsules.

### **test_engine_full.py**
A full-stack test harness validating chaining, execution, provenance, and constraint enforcement.

## **Execution Flow (Simplified)**

Intent Frame ? Validation ? Constraint Evaluation ? Capsule Execution  
? ? Provenance ? Signature Check ? Storage ? Chaining ? Output

## **Purpose of the Core Layer**
The Core Architecture provides the deterministic, consequence-aware foundation that higher-order reasoning layers build upon.
