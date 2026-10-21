# TI-84 Plus CE Python text RPG Framework (CRAWL & CRLLIB)

## System Overview
This is a lightweight text-based RPG game optimized specifically for the strict hardware constraints of the TI-84 Plus CE Python graphing calculator. The engine handles text rendering line-by-line using standard terminal control escape sequences and basic procedural battle systems.

## Critical Hardware Restrictions (For AI Refactoring)
When generating new code, modifying this project, or adding modules via an LLM, the following platform limitations **MUST** be strictly respected:
* **The ~150KB RAM Limit:** The calculator's Python co-processor has very low available memory. Large files or high memory allocations cause instant crashes.
* **No Class Inheritance:** Do not use `class Derived(Base):` or `super()`. All entities must belong to flattened, structural classes. Use configuration switches/integers (e.g., `self.t`) to differentiate entity variants.
* **No Custom Object Registries:** Do not create objects for tiny structures (e.g., coordinates, individual status blocks, questions). Use raw native data types like `tuples`, `lists`, or `integers`.
* **String Memory Footprint:** Keep string literals, variable identifiers, and method names punchy and short. Long names bloat the global execution dictionary.
* **On-The-Fly Calculations:** Never pre-load large lists or tables. Compute data dynamically on a loop-by-loop basis.

## Module Architecture

### 1. CRLLIB.py (Core Game Module)
Manages the application state, player properties, rendering layout, and runtime entity generation.
* `Player`: Tracks `hp`, currencies (`mry`), and stance mechanics (`mode`). Handles user input for swapping configurations (`M`) and assessing metrics (`S`).
* `GameScreen`: Maintains a precise `buf` array representing 9 lines of terminal display. Implements clear screen commands (`\x1b[2J\x1b[H`) for clean frames.
* `Monster`: A unified class driving all adversarial behaviors. Uses an entry tracking ID `t` (0 for Goblin, 1 for DigiBat) to compute health pools, baseline metrics, and select tuple-packaged calculations.

### 2. CRAWL.py (Game Runner Execution Script)
Acts as the central execution loop. 
* Orchestrates target setup and handles resolution steps for active loops.
* Feeds active question structures seamlessly into the player's loop mechanism.
* Dynamically recreates fresh target instances from a random pool whenever an adversary reaches zero health (`alive == False`).

## Implementation Pattern for New Entities
To add a new monster variant:
1. Go to `CRLLIB.py` inside the `Monster.__init__` structure.
2. Increment the conditional type parsing check (e.g., add `elif t == 2:`).
3. Assign its name, stance traits, baseline scaling parameters, and question logic routines inside `move_op()` and `get_basic()`.
4. Append the type array selector wrapper inside the game loop file.