import asyncio

from konnect.http import Session, Request, Method
from konnect.http.authenticators import BasicAuth, BearerTokenAuth


async def run() -> None:
	async with Session() as session:
		session.add_authentication("http://localhost:8110", BearerTokenAuth("foobarbaz"))
		resp = await session.get("http://localhost:8110/bearer")
		body = await resp.stream.read()
		print(body)
		assert resp.code == 200


asyncio.run(run())
