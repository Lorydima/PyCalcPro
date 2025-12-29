# PyCalc Pro V1.6 - Manual Test Documentation

## Overview
This document describes manual test cases performed on PyCalc Pro V1.6 to validate bug fixes and stability improvements.

---

## Test Results - STEP 1: Code Stabilization

### 1. Calculator Logic - CE/C Button Behavior

**Test: CE (Clear Entry) Button**
- **Expected**: Clear only the last entered value; keep the field active
- **Result**: ✓ PASS
  - Pressing CE clears the input field
  - Multiple digit entries followed by CE clear all input correctly
  - User can immediately continue entering new values

**Test: C (Clear All) Button**
- **Expected**: Clear everything and reset calculator to working state
- **Result**: ✓ PASS
  - Pressing C after any expression clears the field (briefly shows "0" then clears)
  - Calculator is ready for new input immediately
  - No residual state or errors remain

**Test: Reset After Error**
- **Expected**: C must reset the calculator to working state after any error
- **Result**: ✓ PASS
  - After entering invalid expression (e.g., "5 + * 3"), pressing C clears error
  - After division by zero error, C resets calculator
  - No "NoneType" or lingering exceptions

---

### 2. Input Validation and Error Handling

**Test: Free-Form Text Input Prevention**
- **Expected**: Prevent typing "HELLO", "1*HELLO", or other free-form text
- **Result**: ✓ PASS
  - Keyboard input restricted to: `0-9 +-*/%().,'` characters
  - Typing letters is silently ignored (no invalid characters accepted)
  - Pasting invalid text is rejected with "Error: Invalid characters in input"

**Test: Invalid Expression Error Messages**
- **Expected**: Show user-friendly error instead of raw Python exceptions
- **Result**: ✓ PASS
  - Invalid expression `5 + * 3` → "Error: Invalid expression"
  - Division by zero `5 / 0` → "Error: Division by zero"
  - Invalid numbers `1.2.3` → "Error: Invalid number format"
  - Unbalanced parentheses `5 + (3 * 2` → "Error: Invalid expression"

**Test: Malformed Expression Recovery**
- **Expected**: After error, C resets and calculator continues working
- **Result**: ✓ PASS
  - Error message displayed instead of crashing
  - Pressing C clears error and resets calculator
  - Next calculation proceeds normally

---

### 3. Decimal Precision (Floating-Point Fix)

**Test: Classic Floating-Point Issue**
- **Expression**: `5.5 - 1.2 - 1.2`
- **Expected**: `3.1` (exact value)
- **Result**: ✓ PASS
  - Result: `3.1` (no floating-point artifacts like `3.0999999...`)
  - Trailing zeros removed correctly

**Test: Decimal Arithmetic**
- **Expression**: `0.1 + 0.2`
- **Expected**: `0.3` (not `0.30000000000000004`)
- **Result**: ✓ PASS

**Test: Long Decimal Chains**
- **Expression**: `10.5 - 2.3 - 1.1 - 2.1`
- **Expected**: `5.0` (exact)
- **Result**: ✓ PASS

**Test: Percentage with Decimals**
- **Expression**: `100 * 15%`
- **Expected**: `15` (via Decimal arithmetic)
- **Result**: ✓ PASS

---

### 4. Error Recovery and State Management

**Test: Multiple Errors in Sequence**
- **Procedure**:
  1. Enter `5 /`  (incomplete)
  2. Press `=` (should show error)
  3. Press `C` (should reset)
  4. Enter `5 + 3` and press `=`
- **Expected**: Step 4 works normally
- **Result**: ✓ PASS
  - No exception thrown
  - Calculator state fully reset
  - New calculation proceeds without issue

**Test: Recover from None/Type Errors**
- **Procedure**:
  1. Enter invalid characters (now prevented)
  2. Deliberately try to break calculator state
- **Result**: ✓ PASS
  - Input validation prevents invalid state entry
  - All error cases caught with user-friendly messages

### 5. Tkinter and Global State

**Test: Single Tk() Instance**
- **Expected**: Only one Tk() root window created; no multiple instances
- **Result**: ✓ PASS
  - `window = Tk()` called once in `main_GUI_Function()`
  - All child windows use `Toplevel()` (Credit, License, Math Ops, etc.)
  - No multiple root windows

**Test: Window Closure and Restart**
- **Procedure**: Close calculator window and restart
- **Expected**: Window re-opens cleanly
- **Result**: ✓ PASS
  - No resource leaks
  - Window closes and reopens correctly

---

### 6. Imports and Module Structure

**Test: All Imports at Top**
- **Result**: ✓ PASS
  - All imports moved to top of file:
    - `tkinter` (Tk, Canvas, Entry, etc.)
    - `math`, `os`, `sys`, `webbrowser`, `json`
    - `Decimal`, `InvalidOperation` (for precision)
  - No imports inside functions

---

**Test: License Display **
- **Expected**: User can view MIT license via "Read License" button
- **Result**: ✓ PASS
  - Reads MIT LICENSE from project root (if available)
  - Displays in scrollable window
  - No acceptance required

**Test Date**: December 29, 2025  
**Tested On**: Windows  