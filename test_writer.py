# test_writer.py
import os, sys, json

messages = [{"id": i, "text": f"Message {i}"} for i in range(5)]

with open("C:/Users/PC/Desktop/test_output.json", "w") as f:
    f.write("[\n")
    for idx, msg in enumerate(messages):
        json.dump(msg, f)
        if idx < len(messages)-1:
            f.write(",\n")
    f.write("\n]")
    f.flush()
    os.fsync(f.fileno())

sys.stdout.flush()
print("✅ Done")

# Read back
with open("C:/Users/PC/Desktop/test_output.json") as f:
    content = f.read()
    print("Start:", repr(content[:10]))
    print("End:", repr(content[-10:]))
