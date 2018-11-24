from sanic.testing import SanicTestClient


async def test_sanic_default_api(sanic_tester: SanicTestClient):
    response = await sanic_tester.get("/health/status")
    assert response.status == 200
    json_response = await response.json()
    assert json_response["status"] == "OK"
