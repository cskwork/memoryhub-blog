---
title: "Hugging Face Models & Ollama - Complete Guide to Running LLMs on Your Computer!"
date: 2025-04-29T08:26:49+09:00
slug: "565-Hugging-Face-모델-Ollama-내-컴퓨터에서-LLM-실행-완전-정복"
original_url: "https://memoryhub.tistory.com/565"
tistory_id: 565
draft: false
categories: ["Dev Library"]
tags: ["GPT"]
---

Hello! Today, I'd like to introduce you to the `num_ctx` parameter, the core of Ollama `Modelfile` configuration, and a magical script that downloads Hugging Face models and registers them to Ollama with just a few clicks. Say goodbye to complicated processes! Let's build your own powerful local LLM environment more easily and smartly!

## Background

In the past, using powerful AI models required expensive cloud services or complex setups. However, with tools like Ollama, you can now run various LLMs on your own computer relatively easily! Especially with Hugging Face Hub's vast collection of models, combining these two opens up endless possibilities. It's like assembling LEGO blocks - bringing the models you want and configuring them for your environment!

## Advantages of Ollama + Hugging Face: Why Use Them Together?

1. **Incredible Selection**: Hugging Face has tons of models converted to GGUF format, from the latest like Llama and Mistral to models specialized for specific tasks. The fun of choosing the model you want!
2. **Private on Your Computer**: Run models on your PC without worrying about cloud costs or data security. No internet connection needed!
3. **Easy Customization**: You can fine-tune how the model works through `Modelfile`. Like the `num_ctx` you'll learn today!

## Core Principles: How to Use It? (Modelfile Update!)

There are two main ways to bring Hugging Face models to Ollama.

1. **Using Ollama Library**: A convenient way like `ollama run llama3` to directly run models Ollama has prepared!
2. **Direct Import (GGUF + Modelfile)**: Download `.gguf` files directly from Hugging Face Hub and create a `Modelfile` instruction manual so Ollama can understand this file. Today, let's focus on this second method, especially `Modelfile` configuration!

### Step 1: Install Ollama (Skip if you already have it!)

Don't have Ollama yet? Download and install it from the [Ollama official website](https://ollama.com/) matching your operating system. It's quick!

### Step 2: Run Model from Ollama Library (The Basics!)

The easiest way! Just open a terminal and enter the model name you want!

```
# Example: Run Llama 3 model
ollama run llama3
```

Ollama will automatically download and run the model. Easy, right?

### Step 3: Find GGUF Model on Hugging Face and Import to Ollama (Customization!)

Now for real customization! Let's bring a specific model directly.

1. **Find and Download GGUF Model from Hugging Face Hub:**
   - Go to [Hugging Face Hub](https://huggingface.co/) and search for your desired model name along with `GGUF` (e.g., `Llama 3 8B Instruct GGUF`).
   - You'll see various GGUF file versions (quantization levels). Filenames will have `Q4_K_M`, `Q5_K_M` etc. Higher numbers usually mean better quality but larger file size and more RAM requirements. Choose the file that matches your computer specs. (e.g., `Meta-Llama-3-8B-Instruct.Q4_K_M.gguf`)
2. **Create `Modelfile` (Update!)**: Create a configuration file (`Modelfile`) so Ollama can use the downloaded GGUF file. Open a text editor and refer to the content below. Be sure to save the filename as `Modelfile` (without extension)!
   - **Complete `PARAMETER num_ctx <number>` Guide!**:
     - **What is it?** This value determines how much content the model can remember and process at once when reading or writing conversations or text. Think of it as your 'working memory capacity'!
     - **Unit is 'tokens'**: A token is roughly a word or character fragment. `4096` means you can remember about 4096 tokens (roughly 3000 words or so)!
     - **Why is it important?** With larger `num_ctx`, the model can summarize longer text or remember multiple conversations and provide consistent answers. However, this uses more computer memory (RAM).
     - **How to set it?**
       1. **Check Model Specs:** Verify the maximum `num_ctx` value your GGUF model supports (usually in the model name or description. e.g., 8K, 32K, etc.).
       2. **Check Your PC RAM:** Consider your computer's RAM capacity. You need to handle model size itself + memory usage based on `num_ctx`.
       3. **Find Appropriate Value:** Set it lower than the model's maximum, at a level your RAM can handle. Set too high and you'll get memory shortage errors (`Error: failed to load model: out of memory`)! Start with `2048` or `4096` and adjust as needed.
3. `# Specify GGUF file path to use (modify to your downloaded file path!) FROM ./Meta-Llama-3-8B-Instruct.Q4_K_M.gguf # (Optional) Model parameter settings ⚙️ # temperature: Controls answer creativity (value between 0 ~ 1) # Lower = consistent and predictable answers, higher = diverse and creative answers PARAMETER temperature 0.7 # num_ctx: Set the model's 'memory'! # The maximum number of tokens (words or character fragments) the model can process and remember at once. # Larger values let you understand longer conversations or documents, but RAM usage increases too! # For example, 4096 can be thought of as remembering about 3000 words of context. # Set considering the maximum context length your model supports (check specs!) and your computer RAM. PARAMETER num_ctx 4096 # <-- Try adjusting this value! # (Optional) System prompt setting # The part that tells the model its role or instructions beforehand. SYSTEM """You are a helpful AI assistant. Always respond kindly and clearly.""" # (Optional) Specify prompt template (Check model documentation!) # Defines how the model exchanges conversations with users. # Different models have different formats, so check the Hugging Face page or documentation! # Below is an example for Llama 3 Instruct model. TEMPLATE """<|begin_of_text|><|start_header_id|>user<|end_header_id|> {{ .Prompt }}<|eot_id|><|start_header_id|>assistant<|end_header_id|> {{ .Response }}<|eot_id|>"""`
4. **Create Ollama Model:** Now go to the folder with `Modelfile` in the terminal and create your own model with the command below! Name `<my_model_name>` as you like (e.g., `my-llama3`).
5. `ollama create <my_model_name> -f Modelfile`
6. **Run Generated Model:** Once model creation is complete, you can run it immediately!
7. `ollama run <my_model_name>`

Now your model will work with the `num_ctx` value you set!

## More Easily! Hugging Face Model Installation Script

Every time you go to Hugging Face, find GGUF files, download them, create `Modelfile`, type `ollama create` commands... it gets tedious, right? So I've prepared a great shell script (Bash) that solves all these steps in one go!

**Script (`ollama_hf_import.sh`):**

```bash
#!/bin/bash

# Hugging Face Model GGUF Download and Ollama Model Creation Script

# --- Configuration Values ---
# Directory to download and save GGUF files
MODEL_DOWNLOAD_DIR="$HOME/ollama_gguf_models"
# Modelfile default template (modify as needed for model)
DEFAULT_TEMPLATE='<|begin_of_text|><|start_header_id|>user<|end_header_id|>

{{ .Prompt }}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{{ .Response }}<|eot_id|>'
# Modelfile default parameters (modify as needed)
DEFAULT_PARAMS=(
  "PARAMETER temperature 0.5"
  "PARAMETER num_ctx 32768"
)
# --- Configuration End ---

# Usage guide function
usage() {
  echo "Usage: $0 <huggingface_repo_id> <gguf_filename> <ollama_model_name>"
  echo "Example: $0 QuantFactory/Meta-Llama-3-8B-Instruct-GGUF Meta-Llama-3-8B-Instruct.Q4_K_M.gguf my-llama3-8b"
  exit 1
}

# Check number of arguments
if [ "$#" -ne 3 ]; then
  usage
fi

# Assign arguments to variables
HF_REPO_ID="$1"
GGUF_FILENAME="$2"
OLLAMA_MODEL_NAME="$3"

# Generate download URL
DOWNLOAD_URL="https://huggingface.co/${HF_REPO_ID}/resolve/main/${GGUF_FILENAME}"
# Full path of file to download
LOCAL_GGUF_PATH="${MODEL_DOWNLOAD_DIR}/${GGUF_FILENAME}"

# Create download directory (if doesn't exist)
mkdir -p "$MODEL_DOWNLOAD_DIR"

echo "--------------------------------------------------"
echo " Hugging Face Model Ollama Import Start"
echo "--------------------------------------------------"
echo "[1/4] Target Model Information:"
echo "  - Hugging Face Repository: ${HF_REPO_ID}"
echo "  - GGUF File: ${GGUF_FILENAME}"
echo "  - Ollama Model Name to Create: ${OLLAMA_MODEL_NAME}"
echo "  - Download Path: ${LOCAL_GGUF_PATH}"
echo "--------------------------------------------------"

# Download GGUF file (skip if already exists)
if [ -f "$LOCAL_GGUF_PATH" ]; then
  echo "[2/4] GGUF file already exists. Skipping download."
else
  echo "[2/4] Starting GGUF file download... (may take time depending on file size)"
  # Use wget or curl (wget preferred)
  if command -v wget &> /dev/null; then
    wget -O "$LOCAL_GGUF_PATH" "$DOWNLOAD_URL"
  elif command -v curl &> /dev/null; then
    curl -L -o "$LOCAL_GGUF_PATH" "$DOWNLOAD_URL"
  else
    echo "Error: wget or curl is required for file download."
    exit 1
  fi

  # Verify download success
  if [ $? -ne 0 ]; then
    echo "Error: Failed to download GGUF file. Check URL and filename."
    # Delete partially downloaded file (optional)
    rm -f "$LOCAL_GGUF_PATH"
    exit 1
  fi
  echo "Download complete!"
fi
echo "--------------------------------------------------"

# Create temporary Modelfile
MODEL_FILE=$MODEL_DOWNLOAD_DIR/Modelfile
echo "[3/4] Creating Modelfile..."
{
  echo "# GGUF file path"
  echo "FROM \"${GGUF_FILENAME}\"" # Add quotes for paths with spaces
  echo ""
  echo "# Parameter settings"
  for param in "${DEFAULT_PARAMS[@]}"; do
    echo "$param"
  done
  # echo ""
  # echo "# Prompt template"
  # echo "TEMPLATE \"\"\"${DEFAULT_TEMPLATE}\"\"\"" # Use """ for multi-line strings
} > "$MODEL_FILE"
echo "Generated Modelfile preview:"
echo "File path: $MODEL_FILE"
cat "$MODEL_FILE"
echo "--------------------------------------------------"

# Create Ollama model
echo "[4/4] Creating Ollama model '${OLLAMA_MODEL_NAME}'..."
ollama create "${OLLAMA_MODEL_NAME}" -f "./${MODEL_FILE}"

echo "--------------------------------------------------"
echo "Success! Ollama model '${OLLAMA_MODEL_NAME}' creation complete."
echo "You can now run the model with the following command:"
echo "ollama run ${OLLAMA_MODEL_NAME}"
echo "--------------------------------------------------"

exit 0
```

**How to Use the Script:**

1. **Save Script:** Copy the code above and save it with a name like `ollama_hf_import.sh` wherever you want.
2. **Grant Execution Permission:** Open terminal, navigate to the folder where you saved the script, and enter `chmod +x ollama_hf_import.sh` to grant execution permission. (Only need to do once!)
3. **Run Script:** Execute in terminal with the following format:

   - `<HuggingFace_Repository_ID>`: Where the model is located (e.g., `QuantFactory/Meta-Llama-3-8B-Instruct-GGUF`)
   - `<GGUF_Filename>`: Name of file to download (e.g., `Meta-Llama-3-8B-Instruct.Q4_K_M.gguf`)
   - `<Create_Ollama_Model_Name>`: Your custom Ollama model name (e.g., `my-llama3-8b`)
   - `[Template_Type]`: (Optional) Type `llama3` to use template for Llama 3 model. Omit to use default template for most models.

   **Example:** To download `Llama-3-8B-Instruct` from `QuantFactory` in `Q4_K_M` version, creating Ollama model name `my-llama3-8b` (using Llama 3 template):

   When you run the script, it magically automatically downloads the GGUF file to `$HOME/ollama_gguf_models` folder (or path specified by `OLLAMA_MODELS` environment variable) (install `wget` or `curl` if not available!), temporarily creates the necessary `Modelfile` and then runs the `ollama create` command. Once all steps complete, you can immediately use the model with `ollama run my-llama3-8b`! Really convenient, right?

4. **Note:** You can also modify the `DEFAULT_PARAMS` array at the top of the script to change default `num_ctx` values, etc.!
5. `./ollama_hf_import.sh QuantFactory/Meta-Llama-3-8B-Instruct-GGUF Meta-Llama-3-8B-Instruct.Q4_K_M.gguf my-llama3-8b llama3`
6. `./ollama_hf_import.sh <HuggingFace_Repository_ID> <GGUF_Filename> <Create_Ollama_Model_Name> [Template_Type]`

## Important Cautions and Tips (Additional `num_ctx` Info)

⚠️ **Pay Attention to These!**

1. **Hardware Requirements (Especially RAM!):** Increasing `num_ctx` improves the model's memory, but RAM usage increases sharply! You must check your computer's RAM capacity, refer to the recommended `num_ctx` range and maximum value in the model documentation, and set it without overextending. Otherwise, model loading failure!
2. **Model File Size:** GGUF file sizes vary greatly depending on quantization level. Verify you have enough storage space before downloading.
3. **`Modelfile` Template Accuracy:** The `TEMPLATE` section has different formats for each model. You must check the model's Hugging Face page or documentation and set it accurately so the model responds correctly. (Using the script handles Llama 3 and typical cases automatically!)

💡 **Pro Tips**

- **Check Installed Models List:** Use `ollama list` command to see Ollama models installed on your computer.
- **Delete Model:** Remove models you no longer use with `ollama rm <model_name>` to free up storage space.
- **Explore Various GGUFs:** Hugging Face Hub has so many GGUF models! Search with "GGUF" keyword and find treasures matching your purpose!

## Conclusion

Now you know how to tune the model's memory by adjusting `num_ctx` in `Modelfile` and how to use a convenient script that solves the tedious installation process in one go! I hope this script and knowledge become a reliable companion on your journey to building a local LLM environment. Try installing various models yourself and experience performance changes by adjusting `num_ctx` values. Enjoy exploring AI's infinite possibilities!

If you have any questions or run into issues, please leave comments!

## References

- [Ollama Official Website](https://ollama.com/)
- [Ollama GitHub Repository](https://github.com/ollama/ollama)
- [Ollama Model Library](https://ollama.com/library)
- [Hugging Face Hub](https://huggingface.co/)
- [Ollama Modelfile Documentation](https://github.com/ollama/ollama/blob/main/docs/modelfile.md) - Detailed `Modelfile` parameter explanations (English)
- [Importing models into Ollama (Ollama Blog)](https://www.google.com/search?q=https://ollama.com/blog/importing-models) - Model import blog (English, Google search required)

---

#Ollama #HuggingFace #LLM #LocalLLM #AI #GGUF #num_ctx #Script #Automation #AIModelInstall
