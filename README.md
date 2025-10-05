# TRG Assessment - Playwright Tests

Quick Start Guide to run end-to-end tests

---

## Prerequisites

- **Python 3.9+** installed
- Git installed

---

## Quick Start

1. **Clone the repository**

```bash
git clone git@github.com:danilotodorovic/trg_assessment.git
cd trg_assessment
```

2. **Create and activate virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Install Playwright browsers**

```bash
playwright install
```

5. **Run tests**

```bash
pytest
```
