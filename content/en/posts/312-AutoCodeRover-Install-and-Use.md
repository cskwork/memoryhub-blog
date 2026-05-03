---
title: "AutoCodeRover Install and Use"
date: 2024-06-24T12:49:50+09:00
slug: "312-AutoCodeRover-Install-and-Use"
original_url: "https://memoryhub.tistory.com/312"
tistory_id: 312
draft: false
---

*Here's a step-by-step guide on installing and running AutoCodeRover locally:*

### 1. Prerequisites

- **Docker**: Ensure Docker is installed on your machine. Docker helps in containerizing the application, ensuring a consistent environment.

### 2. Cloning the Repository

First, clone the AutoCodeRover repository from GitHub:

```
git clone https://github.com/nus-apr/auto-code-rover.git
cd auto-code-rover
```

### 3. Setting Up Environment Variables

Set up the necessary environment variables for API keys. Replace the placeholder text with your actual API keys:

```
export OPENAI_KEY=sk-YOUR-OPENAI-API-KEY-HERE
export ANTHROPIC_API_KEY=sk-YOUR-ANTHROPIC-API-KEY-HERE
export GROQ_API_KEY=sk-YOUR-GROQ-API-KEY-HERE
```

### 4. Building the Docker Image

Build the Docker image using the provided Dockerfile. This step will create a container with all the dependencies:

```
docker build -f Dockerfile -t acr .
```

If you are using an ARM64 architecture (e.g., Apple Silicon), use the alternative Dockerfile:

```
docker build -f Dockerfile.scratch -t acr .
```

### 5. Running the Docker Container

Run the Docker container, exposing the necessary ports:

```
docker run -it -e OPENAI_KEY="${OPENAI_KEY}" -p 3000:3000 -p 5000:5000 acr
```

### 6. Running AutoCodeRover

You can run AutoCodeRover in different modes: GitHub issue mode, local issue mode, and SWE-bench mode.

#### GitHub Issue Mode

For running on a live GitHub issue:

```
cd /opt/auto-code-rover
conda activate auto-code-rover
PYTHONPATH=. python app/main.py github-issue --output-dir output --setup-dir setup --model gpt-4-0125-preview --model-temperature 0.2 --task-id <task id> --clone-link <repo clone link> --commit-hash <commit hash> --issue-link <issue link>
```

#### Local Issue Mode

For running on a local repository and issue file:

```
cd /opt/auto-code-rover
conda activate auto-code-rover
PYTHONPATH=. python app/main.py local-issue --output-dir output --model gpt-4-0125-preview --model-temperature 0.2 --task-id <task id> --local-repo <path to local repo> --issue-file <path to issue file>
```

#### SWE-bench Mode

For running on SWE-bench tasks:

1. Setup the tasks:

   ```
    cd /opt/SWE-bench
    echo django__django-11133 > tasks.txt
    conda activate swe-bench
    python harness/run_setup.py --log_dir logs --testbed testbed --result_dir setup_result --subset_file tasks.txt
   ```
2. Run a single task:

   ```
    cd /opt/auto-code-rover
    conda activate auto-code-rover
    PYTHONPATH=. python app/main.py swe-bench --model gpt-4-0125-preview --setup-map ../SWE-bench/setup_result/setup_map.json --tasks-map ../SWE-bench/setup_result/tasks_map.json --output-dir output --task django__django-11133
   ```

### 7. Accessing the Web UI

For visualization, you can access the web UI:

```
cd /opt/auto-code-rover/demo_vis/
bash run.sh
```

Open `localhost:3000` in your web browser to see the visualization.

### Troubleshooting

If you encounter issues, particularly with Docker on M1 Macs, you may need to adjust dependencies or consult the project's GitHub issues for specific workarounds【6†source】【7†source】【9†source】【10†source】.

---

**Next Steps:**

1. **Explore**: Try running AutoCodeRover on different projects and issues to get a feel for its capabilities.
2. **Customization**: Look into the configuration files to customize the setup for your specific use cases.
3. **Contribution**: Consider contributing to the project by reporting issues, suggesting improvements, or submitting pull requests.
