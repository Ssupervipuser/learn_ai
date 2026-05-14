# AGENTS.md

This is a Python learning/study repository with no formal build system, package manager, or test framework. All code is run directly with `python <file>.py`.

## Directory layout

| Directory | Content |
|---|---|
| `PythonProject/` | Python basics + advanced (OOP, threading, sockets, regex) |
| `上课代码/` | Class demos — Jupyter notebooks + pandas exercises |
| `teacher_code/` | Day-by-day lessons (`day01/`–`day14/`), each self-contained `.py` |
| `提示词工程/` | Prompt engineering — LLM API calls (DashScope/Qwen) |
| `ML_project/` | ML with scikit-learn (regression, classification, KNN) |
| `numpy_pandas_matplotlib/` | Data science Jupyter notebooks |
| `data structure and algorithms/` | Pure Python DSA implementations |
| `mysql_learn/` | SQL scripts — run against a MySQL instance |
| `finebi实战/` | FineBI practice — single SQL schema dump |
| `data/` | Shared CSV/JSON data files consumed by scripts across directories |

## Running code

- **Python scripts**: `python <file.py>` — no venv/conda env needed, but install deps first:
  ```
  pip install openai python-dotenv dashscope pandas numpy matplotlib scikit-learn requests
  ```
- **Jupyter notebooks**: launch from any directory containing `.ipynb` files
- **SQL**: run against a local MySQL instance
- **No CI, no linter, no formatter, no typechecker, no tests**

## 提示词工程 (Prompt Engineering) — key quirks

- Requires `.env` in `提示词工程/`:
  ```
  api_key=sk-...
  base_url=https://dashscope.aliyuncs.com/compatible-mode/v1
  model_name=qwen-max
  ```
- Shared client helper: `utils.get_llm_client()` — loads `.env` via `python-dotenv`, returns `OpenAI(api_key=..., base_url=...)`
- Uses Alibaba Cloud DashScope (OpenAI-compatible API), not OpenAI directly

## Data

- `data/` is the central data directory; several scripts reference it via relative path
- CSV datasets: housing (Boston), e-commerce, wine reviews, stock data, global GDP, etc.
- JSON files: test/train records

## What is NOT here

- No `requirements.txt` or lockfile — dependencies are ad-hoc
- No virtual environment setup
- No test framework or tests
- No CI/CD or deployment config
- No monorepo tooling (no npm, no Cargo, no Go modules)
