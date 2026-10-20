# Impact of Parameter Size on Large Language Models in Automatic Code Refactoring

This repository contains the dataset collection pipeline, raw database, and extracted Python source code used to evaluate how parameter size affects Large Language Models (LLMs) in automatic code refactoring tasks.

---

## 📋 Overview of the Data Collection Pipeline

All programming problems and reference solutions in this dataset are sourced from the **Aizu Online Judge (AOJ)** via the [AOJ Developers API](http://developers.u-aizu.ac.jp).

The dataset construction follows a 4-stage pipeline:
1. **Problem Selection & Fetching** — Curating problem IDs across 8 core computer science courses and retrieving problem descriptions.
2. **Automated Solution Harvesting** — Querying the API for verified, publicly available Python solutions.
3. **Database Consolidation** — Converting raw JSON API responses into a structured SQLite database (`fetched-aoj-data.sqlite`).
4. **Source Code Extraction** — Exporting the raw Python solutions into standalone script files (`extracted-python-code/`).

---

## 🧩 Step 1: Problem Selection & Fetching

Problem IDs were manually curated from eight foundational AOJ course categories (e.g., `ITP1_1_A`, `ITP1_1_B`, `ALDS1_10_B`, `DPL_2_A`):

* **ITP1** — Introduction to Programming I
    ├──ITP1_1_A
    ├──ITP1_1_B
    ├──...
* **ITP2** — Introduction to Programming II
    ├──ITP2_1_A
    ├──...
* **ALDS1** — Algorithms and Data Structures I
* **DSL** — Data Sets and Queries
* **CGL** — Computational Geometry
* **GRL** — Graph Algorithms
* **DPL** — Combinatorial / Dynamic Programming
* **NTL** — Number Theory

Using this curated list of IDs, an automated script queried the AOJ API to retrieve the problem metadata. Each record stores the following attributes:

| Attribute | Description |
| :--- | :--- |
| `problem_id` | Unique identifier for the AOJ problem (e.g., `ITP1_1_A`) |
| `lang` | Language of the problem text |
| `description` | Full problem statement, constraints, and **sample inputs/outputs** used for validation |

```text
Example data:
"ITP1_1_A"	"en"	"{""language"":""en"",""html"":""<H1>Hello World</H1>\n\n<p>\nWelcome to Online Judge!\n</p>\n\n<p>\nWrite a program which prints \""Hello World\"" to standard output.\n</p>\n\n<H2>Input</H2>\n\n<p>\nThere is no input for this problem.\n</p>\n\n<H2>Output</H2>\n\n<p>\n  Print \""Hello World\"" in a line.\n</p>\n\n<p>\n  Do not forget to add a new line at the end. Please note that missing required white spaces or line breaks, or printing extra white spaces or line breaks, will result in a 'Presentation Error' and an incorrect answer.\n</p>\n\n\n<H2>Sample Input 1</H2>\n<pre>\nNo input\n</pre>\n<H2>Sample Output 1</H2>\n<pre>\nHello World\n</pre>\n"",""commentaries"":[],""solvedUser"":93780,""successRate"":57.79058066807411,""score"":0.25,""recommend"":null,""recommendations"":675,""bookmarks"":null,""isSolved"":false,""source"":null,""problem_id"":""ITP1_1_A"",""time_limit"":1,""memory_limit"":131072,""created_at"":1514744635000,""server_time"":1770368282490}"

```

---

## 🔍 Step 2: Automated Solution Harvesting

For each curated `problem_id`, an automated script queried the AOJ API to fetch a reference solution. To ensure high data quality and consistency, every fetched solution had to meet **four strict criteria**:

1. **Language:** Written in **Python**.
2. **Verification Status:** Marked as **Accepted (AC)** by the judge to guarantee functional correctness.
3. **Visibility:** Marked with a **Public** policy so the source code is openly accessible.
4. **Sampling:** **One solution** was randomly sampled per problem from the pool of qualifying submissions.

Each fetched submission includes the following schema attributes:

| Attribute | Description |
| :--- | :--- |
| `judge_id` | 
| `problem_id` | 
| `user_id` | 
| `language` | 
| `status` | 
| `submission_date` | 
| `cpu_time` | 
| `memory` | 
| `source_code` | 
| `policy` | 

```text
Example data:
"judge_id"	"problem_id"	"user_id"	"language"	"status"	"submission_date"	"cpu_time"	"memory"	"source_code"	"policy"
"2574387"	"DPL_2_A"	"htkb"	"Python3"	"Accepted"	"1508497935010"	"16"	"8704"	"def solve():
    V, E = map(int, input().split())
    edges = [[] for _ in [0]*V]
    for _ in [0]*E:
        s, t, d = map(int, input().split())
        edges[s].append((t, d))

    result = float(""inf"")
    beam_width = 70
    for i in range(V):
        q = [(0, i, {i})]
        for j in range(V-1):
            _q = []
            append = _q.append
            for cost, v, visited in q[:beam_width+1]:
                for dest, d_cost in edges[v]:
                    if dest not in visited:
                        append((cost+d_cost, dest, visited | {dest}))
            q = sorted(_q)
        for cost, v, visited in q[:beam_width+1]:
            for dest, d_cost in edges[v]:
                if dest == i:
                    if result > cost + d_cost:
                        result = cost + d_cost
                        break

    print(result if result < float(""inf"") else -1)


if __name__ == ""__main__"":
    solve()
"	"public"

```

---

## 🗄️ Step 3: Database Consolidation (`fetched-aoj-data.sqlite`)

Although the AOJ API returns data in raw JSON format, all fetched problem descriptions and solution records were parsed and consolidated into a single relational SQLite database: **`fetched-aoj-data.sqlite`**. 

This makes querying, filtering, and joining problems with their corresponding solutions fast and reproducible.

---

## 🐍 Step 4: Source Code Extraction (`extracted-python-code/`)

To prepare the code for LLM refactoring experiments, a secondary extraction script parsed `fetched-aoj-data.sqlite` to isolate the `source_code` field from each submission. 

All extracted Python scripts are stored in the **`extracted-python-code/`** directory, ready to be fed into the models for refactoring and evaluation.

---

## 📁 Key Repository Files

```text
├── fetched-aoj-data.sqlite   # Consolidated SQLite database (problems + solutions)
├── extracted-python-code/    # Standalone Python scripts extracted from the database
└── README.md                 # Project documentation
```