from sanic.testing import SanicTestClient


async def test_sanic_default_api(sanic_tester: SanicTestClient):
    response = await sanic_tester.get("/")
    assert response.status == 200
