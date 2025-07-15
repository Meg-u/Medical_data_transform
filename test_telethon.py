import json

# Fake list of messages
messages = [{"id": i, "text": f"Message {i}"} for i in range(5)]

# Save with bulletproof brackets
with open("test_output.json", "w", encoding="utf-8") as f:
    f.write("[\n")
    for idx, msg in enumerate(messages):
        json.dump(msg, f, ensure_ascii=False)
        if idx < len(messages) - 1:
            f.write(",\n")
    f.write("\n]")

print(" JSON written.")
