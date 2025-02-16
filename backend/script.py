import pickle

with open("label_encoders.pkl", "rb") as f:
    label_encoders = pickle.load(f)

print("🧐 Type of label_encoders:", type(label_encoders))

if isinstance(label_encoders, dict):
    for key, encoder in label_encoders.items():
        print(f"🔍 Label Encoder for '{key}': {encoder.classes_}")
else:
    print("❌ label_encoders is not a dictionary. Found:", label_encoders)
