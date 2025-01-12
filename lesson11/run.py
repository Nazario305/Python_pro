import asyncio
import time
import random
import requests
import httpx
import argparse

BASE_URL = "https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

def http_request(url: str) -> str:
    print(f"requesting {url}")
    response: dict = requests.get(url).json()
    return response["name"]

async def ahttp_request(url: str, library: str) -> str:
    print(f"requesting {url}")
    if library == "httpx":
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            return response.json()["name"]
    elif library == "aiohttp":
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return (await response.json())["name"]


def get_urls(n: int) -> list[str]:
    return [BASE_URL.format(pokemon_id=random.randint(1, 500)) for _ in range(n)]

def sync_pokemons():
    urls: list[str] = get_urls(n=50)
    results = [http_request(url) for url in urls]

    return results

async def async_pokemons(library: str):
    urls: list[str] = get_urls(n=50)
    tasks = [ahttp_request(url, library) for url in urls]
    results = await asyncio.gather(*tasks)

    return results

def main():
    parser = argparse.ArgumentParser(description="Fetch Pokemon names synchronously or asynchronously.")
    parser.add_argument("library", choices=["httpx", "requests"], help="Choose the library to use for requests.")
    args = parser.parse_args()

    start = time.perf_counter()

    if args.library == "requests":
        data = sync_pokemons()
    else:
        data = asyncio.run(async_pokemons(args.library))

    end = time.perf_counter()

    print(data)
    print(f"the len of the collection: {len(data)}")
    print(f"execution time: {end - start}")

if __name__ == "__main__":
    raise SystemExit(main())
