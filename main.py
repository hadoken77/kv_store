from fastapi import FastAPI

app = FastAPI()
kv_store: dict = {}


@app.get("/")
async def root():
    return {"message": "Hello there. Go to http://localhost:8000/docs"}


@app.post("/retrieve")
async def retrieve(key: str) -> None:
    if key in kv_store.keys():
        return kv_store.get(key)
    return None


@app.post("/store")
async def store(key: str, value: str):
    kv_store[key] = value


@app.post("/delete")
async def delete(key: str):
    if key in kv_store.keys():
        kv_store.pop(key)


@app.get("/list")
async def list_all():
    return kv_store


@app.get("/test_client/test_deletion")
async def test_deletion():
    await store("foo", "bar")
    value = await retrieve("foo")
    if value != "bar":
        raise Exception(f"Expected: bar, got: {value}")
    await delete("foo")
    value = await retrieve("foo")
    if value is not None:
        raise Exception(f"Expected: None, got: {value}")
    return "Success"


@app.get("/test_client/test_overwrite")
async def test_overwrite():
    await store("foo", "bar")
    value = await retrieve("foo")
    if value != "bar":
        raise Exception(f"Expected: bar, got: {value}")
    await store("foo", "bar2")
    value = await retrieve("foo")
    if value != "bar2":
        raise Exception(f"Expected: bar2, got: {value}")
    return "Success"
