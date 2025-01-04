from synago.agent import Agent
from pydantic import BaseModel, Field
from typing import List
import random


async def test_stream():
    agent = Agent(
        name="test",
        instructions="You are a sci-fi fan, you can answer any sci-fi related questions.",
        model="gpt-4o-mini",
    )
    msgs = [{"role": "user", "content": "What is the meaning of life? Just give me a number without any other words and symbols."}]
    stream = agent.get_stream(msgs)
    print("")
    print("answer:")
    resp = await agent.run_stream(
        stream,
        lambda chunk: print(chunk.get("content", "") or "", end="", flush=True))
    assert len(resp.messages) == 1


async def test_tool_use():
    agent = Agent(
        name="test",
        instructions="You are a weather agent, you can use the weather API to get the weather of a city.",
        model="gpt-4o-mini",
    )

    @agent.tool
    def get_weather(city: str):
        """Get the weather of a city."""
        return {"weather": "sunny"}

    msgs = [{"role": "user", "content": "What is the weather in Palo Alto?"}]
    stream = agent.get_stream(msgs)
    resp = await agent.run_stream(stream)
    print()
    print(resp)
    call_id = resp.messages[0]["tool_calls"][0]["id"]
    assert resp.context_variables[call_id]["weather"] == "sunny"


async def test_structured_output():
    agent = Agent(
        name="test",
        instructions="You are a sci-fi fan, you can answer any sci-fi related questions.",
        model="gpt-4o-mini",
    )

    class SciFiBook(BaseModel):
        title: str
        author: str
        year: int

    class SciFiBookList(BaseModel):
        books: List[SciFiBook]

    stream = agent.get_stream(
        messages=[{"role": "user", "content": "Recommend me 5 sci-fi books."}],
        response_format=SciFiBookList,
    )

    def assert_chunk(chunk):
        assert isinstance(chunk, dict)

    resp = await agent.run_stream(stream, assert_chunk)
    print(resp)
    assert isinstance(resp.messages[0]["parsed"], SciFiBookList)
    assert len(resp.messages[0]["parsed"].books) == 5


async def test_structured_output_with_tool_use():
    agent = Agent(
        name="test",
        instructions="You are a sci-fi fan, you can answer any sci-fi related questions, and you can use the tool calls to get the rating of each book.",
        model="gpt-4o-mini",
    )

    class SciFiBook(BaseModel):
        title: str
        author: str
        year: int

    class SciFiBookList(BaseModel):
        books: List[SciFiBook]
        ratings: List[float] = Field(description="Use tool calls to get the rating of each book.")

    @agent.tool
    def get_book_rating(title: str) -> float:
        """Get the rating of a book."""
        print(title)
        return random.random()

    answer = await agent.run(
        "Recommend me 5 sci-fi books.",
        response_format=SciFiBookList,
    )
    print(answer)
    assert isinstance(answer.content, SciFiBookList)
    assert len(answer.content.books) == 5
    for r in answer.content.ratings:
        assert 0 <= r <= 1.0


async def test_agent_result_passing():
    scifi_fan = Agent(
        name="scifi_fan",
        instructions="You are a sci-fi fan, you can answer any sci-fi related questions.",
        model="gpt-4o-mini",
    )

    scifi_critic = Agent(
        name="scifi_critic",
        instructions="You are a scifi critic, you can review a sci-fi book and give a rating.",
        model="gpt-4o-mini",
    )

    summary_agent = Agent(
        name="summary_agent",
        instructions="You are a summary agent, you can summarize the answer of other agent give a human readable format.",
        model="gpt-4o-mini",
    )

    class SciFiBook(BaseModel):
        title: str
        author: str
        year: int

    class SciFiBookList(BaseModel):
        books: List[SciFiBook]

    answer_recommend = await scifi_fan.run(
        "Recommend me 5 sci-fi books.",
        response_format=SciFiBookList,
    )
    print(answer_recommend.content)

    class SciFiBookListWithRating(SciFiBookList):
        ratings: List[float] = Field(description="Rate the book from 0 to 10.")
        comments: List[str] = Field(description="Comment on the book.")

    answer_critic = await scifi_critic.run(
        answer_recommend,
        response_format=SciFiBookListWithRating,
    )
    print(answer_critic.content)

    assert isinstance(answer_critic.content, SciFiBookListWithRating)
    assert len(answer_critic.content.books) == 5
    assert len(answer_critic.content.ratings) == 5
    assert len(answer_critic.content.comments) == 5

    answer_summary = await summary_agent.run(
        answer_critic,
    )
    print(answer_summary.content)
