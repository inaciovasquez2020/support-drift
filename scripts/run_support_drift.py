import json
import hashlib

def main():
    data = {
        "claim": "support-drift",
        "model": "synthetic-bounded",
        "parameters": {
            "max_steps": 10,
            "capacity_bound": 1
        },
        "observation": "support_changes_detected"
    }

    payload = json.dumps(data, sort_keys=True).encode()
    digest = hashlib.sha256(payload).hexdigest()

    out = {
        "data": data,
        "sha256": digest
    }

    with open("artifacts/support_drift_result.json", "w") as f:
        json.dump(out, f, indent=2)

    print("ok", digest)

if __name__ == "__main__":
    main()
