yellow='\033[1;33m'
green='\033[0;32m'
nc='\033[0m'

echo "$yellow Starting DeepSeek Coder$nc"
nohup vllm serve deepseek-ai/deepseek-coder-1.3b-instruct --trust-remote-code --max-model-len=8000 --api-key=123  > /dev/null 2>&1 &
$! > /tmp/deepseek-coder.pid
echo "$green DeepSeek Coder is running$nc"

if ! command -v aider &> /dev/null
then
    echo "$yellow Installing Aider$nc"
    aider-install
fi

export OPENAI_API_KEY=123
export OPENAI_API_BASE="http://0.0.0.0:8000/v1"
aider --model openai/deepseek-ai/deepseek-coder-1.3b-instruct

# not working, how to catch signal from aider sigint?
trap 'echo "$yellow Stopping DeepSeek Coder$nc"; kill $(cat /tmp/deepseek-coder.pid); echo "$green DeepSeek Coder stopped$nc"; exit' SIGINT