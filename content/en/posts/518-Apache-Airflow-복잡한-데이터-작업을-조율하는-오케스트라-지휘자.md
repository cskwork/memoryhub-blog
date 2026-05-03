---
title: "Apache Airflow - The Orchestra Conductor Orchestrating Complex Data Tasks 🎼"
date: 2025-03-24T21:46:15+09:00
slug: "518-Apache-Airflow-복잡한-데이터-작업을-조율하는-오케스트라-지휘자"
original_url: "https://memoryhub.tistory.com/518"
tistory_id: 518
draft: false
categories: ["Dev Framework"]
tags: ["Apache"]
---

Hello! 👋 Data engineering, machine learning pipelines, ETL tasks... aren't the workflows you need to handle becoming increasingly complex? 🎪 Like an orchestra conductor leading numerous musicians, how can we harmoniously manage and execute these complex tasks? Today, let's explore a wonderful solution to this problem, **Apache Airflow**, in an easy and fun way!

## Background of Its Emergence

How did people handle complex tasks in the past? 🤔 Many probably created lots of shell scripts (`.sh`) and registered them in **crontab**.

- **Early days**: Individual scripts were written and scheduled to run at specific times using Linux's `cron` scheduler.
- **Problems**:
  - Managing dependencies between tasks 📊 (Task A must finish before Task B runs) was difficult.
  - When a specific task failed ⛔️, retrying or identifying the cause was cumbersome.
  - It was hard to see the overall workflow at a glance 🙈, and schedule changes weren't flexible.
  - Log checking and progress monitoring were scattered, making management difficult.

Out of these frustrations came a question: "Can't we define workflows in code, schedule them intelligently, and manage them easily?" And from Airbnb's efforts to answer this question, **Airflow** was born! 🌟 Today, it's an Apache Foundation Top-Level project actively used by countless companies worldwide.

## Problems Airflow Solves (Features/Uses)

Airflow elegantly solves the problems mentioned above.

1. **Code-based definition and management of complex workflows**:
   - Workflows (DAG) can be clearly defined in Python code. Thanks to this, version control (Git, etc.) is easy, and dynamic pipeline generation is possible. You can easily implement task ordering, parallelization, etc. 🔄
2. **Smart scheduling and execution**:
   - Beyond simply running at fixed times, it offers flexible scheduling options like conditional execution, external event triggers, and automatic retries on failure. Backfill functionality for processing historical data is also powerful. 📅
3. **Intuitive monitoring and management**:
   - Through the Web UI, you can visually understand the workflow structure, execution status, logs, etc. at a glance. ✅ You can easily track each task's success/failure, execution time, etc., and respond quickly when issues arise. 🚨

## Core Principles

Airflow's core is the **DAG (Directed Acyclic Graph)**. The name sounds difficult, but think of it simply as 'defining how tasks flow in a specific order'.

```
# Simple DAG visualization example (text-based)

      +-----------+      +-----------+
      | Task A    | ---> | Task B    |
      | (Start)   |      | (After A) |
      +-----------+      +-----------+
           |                    |
           |                    v
           v              +-----------+
      +-----------+      | Task D    |
      | Task C    | ---> | (After B,C)|
      | (After A) |      +-----------+
      +-----------+
```

- **DAG**: The blueprint of the entire workflow. Defined in Python file (`.py`), including when and how it will run (schedule).
- **Task**: Individual work units composing the DAG. Task A, B, C, D in the above diagram correspond to each Task.
- **Operator**: A template defining what each Task 'does'. For example,
  - `BashOperator`: Executes shell commands.
  - `PythonOperator`: Executes Python functions.
  - `PostgresOperator`: Executes PostgreSQL queries.
  - And many other types of Operators exist to integrate with various systems. 🔧

**Operational Flow Summary**:

1. **Scheduler**: Periodically scans defined DAG files to find DAG Runs and Task Instances that are due to run, placing them in the execution queue.
2. **Executor**: Determines how to execute Tasks. (Example: local sequential execution, distributed execution using Celery/Kubernetes, etc.)
3. **Worker**: The entity that executes actual Tasks under Executor's direction.
4. **Web Server**: Provides UI to users and offers features like checking DAG status, manual execution, etc.
5. **Metadata Database**: Stores all metadata like DAG information, Task status, execution history, etc. (Usually PostgreSQL or MySQL)

|  |  |  |
| --- | --- | --- |
| **Component** | **Role** | **Analogy** |
| **DAG** | Entire workflow structure and schedule definition | Orchestra score |
| **Task** | Individual work unit within workflow | Specific part in score |
| **Operator** | Template defining Task's actual behavior | Instrument type (instructions) |
| **Scheduler** | Places Tasks in execution queue according to schedule | Conductor (start playing!) |
| **Executor/Worker** | Actually executes Tasks | Musicians |
| **Web Server** | Provides user interface (monitoring, management) | Concert venue guide/manager |
| **Metadata DB** | Stores all state information (score, performance records, etc.) | Music library |

## Cautions and Tips 🚀

⚠️ **These are critical points!**

1. **Maintain idempotency**: Tasks should produce identical results even when executed multiple times.
   - **Detailed explanation**: Tasks may be executed multiple times due to network errors. If results differ, data consistency becomes problematic. 📊
   - **Solution**: Instead of simple INSERT, use `INSERT ... ON CONFLICT DO NOTHING/UPDATE` (UPSERT), or delete and re-insert data for specific partitions/dates.
2. **Keep Tasks light and atomic**: Design Tasks so they don't do too much or take too long.
   - **Detailed explanation**: Heavy Tasks incur high retry costs when they fail, and debugging becomes difficult.
   - **Solution**: Break large tasks into multiple smaller Tasks with dependencies, composing the DAG accordingly.
3. **Keep DAG definition files light**: Don't perform heavy operations (database queries, API calls, etc.) directly in DAG files.
   - **Detailed explanation**: The Scheduler parses DAG files frequently. If this takes time, it affects overall Airflow performance. 🔴
   - **Solution**: Keep actual work logic inside Operators (e.g., the `python_callable` function of `PythonOperator`), and focus DAG files on structure definition.

💡 **Useful Tips**

- **Connections & Hooks**: Store external system connection information (databases, cloud services, etc.) safely in Airflow UI's Connections, and use Hooks in code to easily retrieve connection information. Security UP! ✨
- **Variables & Macros**: Manage frequently used values (paths, settings, etc.) as Variables, and use Jinja templates and Macros for dynamic values, increasing flexibility. (Example: `{{ ds }}` is execution date)
- **TaskGroups**: Visually group related Tasks to make complex DAGs easier to view. (Airflow 2.0 and above) 📊
- **SubDAGs (use cautiously)**: Useful for creating reusable Task groups, but potential issues like deadlocks exist, making TaskGroups the recommended choice.
- **Custom Operators**: If an Operator for your needed functionality doesn't exist, you can create one yourself! 🛠️

## Conclusion

We've explored what Apache Airflow is, why it's needed, and how it works. At first, concepts like DAG and Operator might feel unfamiliar, but the ability to systematically manage complex data pipelines through Python code is really attractive! 🌟 I hope this article has been a small help on your data journey! If you have questions or want to share tips while using Airflow, please leave a comment! 🙋‍♀️

## References 📚

- [Apache Airflow Official Documentation](https://airflow.apache.org/docs/)
- [Apache Airflow Tutorial](https://www.google.com/search?q=https://airflow.apache.org/docs/apache-airflow/stable/tutorial.html)
- [Astronomer - Airflow Guide](https://www.astronomer.io/guides/) (Managed Airflow service provider, offering quality guides)

---

#ApacheAirflow #Airflow #DataPipeline #WorkflowManagement #DataEngineering #ETL #Orchestration
