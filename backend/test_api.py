"""Quick integration test for the Flask API."""
import json
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from app import app

client = app.test_client()

# Test 1: Normal request
r = client.get('/api/cargo')
print(f"[1] Normal GET /api/cargo  => Status: {r.status_code}")
data = json.loads(r.data)
print(f"    Records returned: {len(data)}")
assert r.status_code == 200, "Expected 200"
assert len(data) == 10, f"Expected 10 records, got {len(data)}"
print(f"    First record: {data[0]['cargo_id']} - {data[0]['destination']} - {data[0]['final_weight']}kg")

# Test 2: System Override header -> 418
r2 = client.get('/api/cargo', headers={'X-System-Override': 'true'})
print(f"\n[2] GET /api/cargo with X-System-Override: true")
print(f"    Status: {r2.status_code}")
print(f"    Body:   {r2.data.decode()}")
assert r2.status_code == 418, "Expected 418"
assert r2.data.decode() == "System override denied.", "Wrong body"

# Test 3: Health check
r3 = client.get('/api/health')
print(f"\n[3] GET /api/health => Status: {r3.status_code}")
print(f"    Body: {r3.data.decode()}")
assert r3.status_code == 200

# Test 4: 404 for unknown route
r4 = client.get('/api/nonexistent')
print(f"\n[4] GET /api/nonexistent => Status: {r4.status_code}")
assert r4.status_code == 404

print("\n=== ALL TESTS PASSED ===")
