# NETREPLAY-SIM

> **Developer Tools track**  
> *Record the network. Replay the failure. Prove the fix.*

**NETREPLAY** is a developer tool and flight recorder for mobile apps operating on Indian networks. It captures the network conditions and app events surrounding a failure on the phone, uses an on-device AI model to explain the cause, allows developers to replay the exact conditions on demand, and repeatedly verifies a fix through automated reproduction runs.

This repository contains **NETREPLAY-SIM**, a concept prototype built for the iQOO Hackathon 2026 Grand Finale idea-submission portal. It simulates the entire product loop directly within the terminal, demonstrating the exact forensic process and workflow our Android SDK, vivo Office Kit integration, and Laptop Console will follow.

## The Problem
Network-related failures on mobile are historically notorious to reproduce. 
- 17% of bug reports in one industrial and five open-source trackers were non-reproducible, leading to significantly delayed fixes (Joorabchi et al., MSR 2014).
- A study of 154 real network-related bugs across 42 Android apps proved that complex, multi-stage network patterns are often required to trigger failures (NATE, ASE 2025).
- India's best operator met Opensignal's standards, but the remaining variability demands robust handling of connection handovers, dropouts, and congestion.

## The Workflow (Loop)
1. **CAPTURE:** Ring-buffer based data capture intercepts requests, network dropouts, and application events right on the phone.
2. **AUTOPSY:** Explains the failure using change-point detection and causal chain rules, combined with local LLMs (Ollama).
3. **REPLAY:** Accurately recreates identical network latency and drop circumstances locally.
4. **FIX:** Automatically suggests the necessary fix (e.g. Idempotency-Keys, Retries with Jitter).
5. **VERIFY:** Statistically proves the fix using Wilson confidence intervals and Fisher's exact tests over `N` runs.

## Setup and Installation

### Prerequisites
- Python 3.10+
- OS: Windows, macOS, or Linux

### Installation
Clone this repository and install the sole dependency (`rich`):

```bash
git clone https://github.com/JayasriKapil/NETREPLAY.git
cd NETREPLAY
pip install -r requirements.txt
```

*(Note: Optional graceful degradations for `--llm` and `--voice` transcription exist. To utilize them, you would need `ollama` and `faster-whisper` installed locally.)*

## Usage

NETREPLAY-SIM features an interactive, stage-by-stage demo designed to walk judges through the concept workflow.

```bash
# Run the interactive, guided terminal demo (Press Enter to advance stages)
python -m netreplay demo

# Run the demo automatically with a 2-second delay between stages
python -m netreplay demo --auto

# Run a specific sub-set of critical stages quickly
python -m netreplay demo --short --fast

# Export SVGs of each stage into a directory (Great for pitch decks!)
python -m netreplay demo --fast --export-svg presentation_assets/
```

### Modes and Flags
* `--plain`: Turns off Unicode formatting and colors. Essential for older terminal hosts.
* `--runs N`: Set the number of replay iterations to `N` (default: 20).
* `--llm`: Uses a local Ollama LLM endpoint to generate explanations instead of deterministic templates.
* `--voice <file.wav>`: Transcribes a tester's note directly onto the forensics timeline.

## Disclaimer
> **CONCEPT PROTOTYPE** - All network data, profiles (like `lift` or `metro-tunnel`), and fictional applications (PayLite) in this repository are simulated purely for the grand finale pitch demonstration.