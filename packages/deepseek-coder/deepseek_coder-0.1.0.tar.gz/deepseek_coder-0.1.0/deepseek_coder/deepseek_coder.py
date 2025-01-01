import os
import subprocess
import time

yellow = '\033[1;33m'
green = '\033[0;32m'
nc = '\033[0m'
VLLM_LOGS_PATH = '/tmp/deepseek_coder.log'
LONG_RUNNING_WARNING = 60

print(f"{yellow}Starting DeepSeek Coder. Please wait...{nc}")
vllm_logs = open(VLLM_LOGS_PATH, 'w+')
vllm_process = subprocess.Popen(
    ["vllm", "serve", "deepseek-ai/deepseek-coder-1.3b-instruct", "--trust-remote-code", "--max-model-len=8000", "--api-key=123"],
    stdout=vllm_logs,
    stderr=subprocess.STDOUT
)

try:
    subprocess.run(["which", "aider"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT).check_returncode()
except subprocess.CalledProcessError:
    print(f"{yellow}Installing Aider{nc}")
    subprocess.run(["aider-install"])
    print(f"{green}Aider installed{nc}")

start = time.time()
shown_long_running_disclaimer = False
vllm_logs_read = open(VLLM_LOGS_PATH, 'r')
while True:
    line = vllm_logs_read.readline()
    time.sleep(0.1)
    vllm_logs_read.seek(vllm_logs_read.tell())
    if "running on http://0.0.0.0:8000" in line:
        print(f"{green}DeepSeek Coder started{nc}")
        break
    if "RuntimeError" in line:
        print(f"{yellow}Failed to start DeepSeek Coder{nc}")
        print(f"{yellow}See Logs: {VLLM_LOGS_PATH} {nc}")
        vllm_process.kill()
        exit(1)
    if time.time() - start > LONG_RUNNING_WARNING and not shown_long_running_disclaimer:
        print("DeepSeek Coder is taking longer than usual to start. If this is the first time you're running this command, it's because the model weights are being downloaded.")
        print(f"Check progress by running `tail -f {VLLM_LOGS_PATH}`")
        shown_long_running_disclaimer = True


        

os.environ["OPENAI_API_KEY"] = "123"
os.environ["OPENAI_API_BASE"] = "http://0.0.0.0:8000/v1"
subprocess.run(["aider", "--model", "openai/deepseek-ai/deepseek-coder-1.3b-instruct"])
vllm_process.kill()
print(f"{green}DeepSeek Coder stopped{nc}")
