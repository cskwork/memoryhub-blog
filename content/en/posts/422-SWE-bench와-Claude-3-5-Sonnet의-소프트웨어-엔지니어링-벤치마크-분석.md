---
title: "SWE-bench and Claude 3.5 Sonnet: Software Engineering Benchmark Analysis"
date: 2024-12-21T20:16:22+09:00
slug: "422-SWE-bench와-Claude-3-5-Sonnet의-소프트웨어-엔지니어링-벤치마크-분석"
original_url: "https://memoryhub.tistory.com/422"
tistory_id: 422
draft: false
categories: ["Dev Library"]
tags: ["Claude"]
---

Hello! Today, let's take a detailed look at SWE-bench, which evaluates AI coding capabilities, and Claude 3.5 Sonnet's remarkable achievements.

## What is SWE-bench?

SWE-bench is a benchmark for evaluating the actual software engineering capabilities of AI models. It tests whether an AI can solve GitHub issues like a real developer!

### Key Features:

- Uses issues from real open-source Python projects
- Evaluates the entire process of AI understanding code, fixing it, and testing it
- Validates with unit tests from actual Pull Requests (PRs)
- Evaluates the entire 'agent' system (AI model + software scaffolding)

## Claude 3.5 Sonnet's Revolutionary Achievement

### Performance Comparison

```
Model                          Score
Claude 3.5 Sonnet (New)       49%
Previous Best Performance      45%
Claude 3.5 Sonnet (Old)       33%
Claude 3 Opus                 22%
```

## How Did It Achieve Such Results?

### 1. Tool Using Agent Design Philosophy

- Grant maximum autonomy to AI model
- Maintain minimum scaffolding
- Provide two core tools:
  - Bash Tool: Execute commands
  - Edit Tool: Manipulate files

### 2. Prompt Optimization

```
Key Steps:
1. Explore repository structure
2. Write error reproduction script
3. Modify source code
4. Verify by re-running
5. Handle edge cases
```

### 3. Sophistication in Tool Design

- Clear tool descriptions
- Error prevention mechanisms
- State management
- File path handling optimization

## Real Working Example

1. **Initial Exploration**
   - Analyze repository structure
   - Understand the problem situation
2. **Error Reproduction**
   - Create test data n = 100 x = np.random.randn(n, 30) y = np.random.normal(size = n)
3. **Code Modification**
   - Identify exact location
   - Solve with minimum changes

## Challenges

1. **Resource Consumption**
   - Long execution time
   - High token costs
   - Hundreds of interactions needed
2. **Evaluation Difficulty**
   - Environment configuration issues
   - Hidden test cases
   - Abstraction level mismatch
3. **Multimodal Limitations**
   - Limited file visualization
   - Difficulty referencing URLs
   - Debugging complexity

## Future Outlook

Claude 3.5 Sonnet's achievements have opened new horizons for AI coding capabilities. In particular:

- Higher accuracy
- Improved self-correction ability
- Attempts at various solutions
- Continuous improvement potential

## References

1. SWE-bench Official Site: <https://www.swebench.com/>
2. Anthropic Blog: Claude 3.5 Sonnet Update Announcement
3. SWE-Agent Framework Documentation

---

# A Practical Software Engineering Guide with Claude 3.5 Sonnet

Let's look at how Claude 3.5 Sonnet actually solves coding problems with concrete examples.

## 1. Real Bug Fix Case: RidgeClassifierCV Parameter Issue

### Problem Situation

```
# Code that causes error
from sklearn import linear_model as lm
import numpy as np

n = 100
x = np.random.randn(n, 30)
y = np.random.normal(size = n)

rr = lm.RidgeClassifierCV(
    alphas = np.arange(0.1, 1000, 0.1), 
    normalize = True,
    store_cv_values = True
).fit(x, y)
```

### Error Occurred

```
TypeError: __init__() got an unexpected keyword argument 'store_cv_values'
```

### Claude's Analysis Process

1. **Code Exploration**

   ```
   # Inside ridge.py file
   class RidgeClassifierCV:
    def __init__(self, alphas=(0.1, 1.0, 10.0), 
                 fit_intercept=True,
                 normalize=False, 
                 scoring=None, 
                 cv=None, 
                 class_weight=None):
        # store_cv_values parameter is missing!
   ```

2. **Solution Derivation**

   ```
   # Fixed code
   def __init__(self, alphas=(0.1, 1.0, 10.0),
             fit_intercept=True,
             normalize=False,
             scoring=None,
             cv=None,
             class_weight=None,
             store_cv_values=False):  # Add parameter
    super(RidgeClassifierCV, self).__init__(
        alphas=alphas,
        fit_intercept=fit_intercept,
        normalize=normalize,
        scoring=scoring,
        cv=cv,
        store_cv_values=store_cv_values  # Pass to parent class
    )
   ```

## 2. Practical Feature Implementation Example: File Processing System

### Requirements

- Directory exploration
- File content modification
- Change validation

### Claude's Implementation Process

1. **Directory Exploration**

   ```
   def explore_directory(path):
    """
    Function to explore directory structure
    """
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f'{subindent}{f}')
   ```

2. **File Modification**

   ```
   def modify_file(file_path, old_str, new_str):
    """
    Safely modify file content
    """
    with open(file_path, 'r') as file:
        content = file.read()

    # Verify exact match
    if content.count(old_str) != 1:
        raise ValueError("Unique matching required")

    # Create backup
    backup_path = f"{file_path}.bak"
    shutil.copy2(file_path, backup_path)

    # Modify content
    new_content = content.replace(old_str, new_str)

    with open(file_path, 'w') as file:
        file.write(new_content)
   ```

3. **Change Verification**

   ```
   def verify_changes(file_path, test_function):
    """
    Verify changes
    """
    try:
        result = test_function()
        print(f"Verification success: {file_path}")
        return True
    except Exception as e:
        print(f"Verification failed: {str(e)}")
        # Restore from backup
        if os.path.exists(f"{file_path}.bak"):
            shutil.copy2(f"{file_path}.bak", file_path)
        return False
   ```

## 3. Real-World Scenarios

### Scenario 1: Configuration File Update

```
# Configuration file modification example
def update_config():
    file_path = "/repo/config.py"
    old_config = """
    DEBUG = False
    MAX_RETRIES = 3
    """
    new_config = """
    DEBUG = True
    MAX_RETRIES = 5
    """

    modify_file(file_path, old_config, new_config)
    verify_changes(file_path, run_tests)
```

### Scenario 2: API Endpoint Modification

```
# API route update example
def update_api_route():
    file_path = "/repo/api/routes.py"
    old_route = """
    @app.route('/users', methods=['GET'])
    def get_users():
        return jsonify(users)
    """
    new_route = """
    @app.route('/users', methods=['GET'])
    def get_users():
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        return jsonify(paginate_users(users, page, per_page))
    """

    modify_file(file_path, old_route, new_route)
    verify_changes(file_path, test_api)
```

## Conclusion

Through real-world examples of Claude 3.5 Sonnet usage, we learned the following:

1. **Systematic Approach**

   - Problem analysis
   - Solution design
   - Implementation and verification

2. **Safe Code Modification**

   - Create backups
   - Verify changes
   - Rollback mechanism

3. **Efficient Debugging**

   - Clear error messages
   - Step-by-step verification
   - Automated testing

## References

1. Anthropic Technical Blog
2. sklearn Documentation
3. Python Software Engineering Best Practices
