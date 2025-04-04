from agents import Agent, Runner
import sys
import io

# Windows環境での文字化けを防ぐためにUTF-8出力を設定
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant"
)

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.