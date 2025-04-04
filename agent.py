import agent from Agent,Runner
import asyncio

agent=Agent(
    name="Assistant",
)

runner=Runner(agent)

async def main():
    result=await runner.run(agent,"hello")
    print(result.final_output)

if __name__=="__main__":
    asyncio.run(main())
