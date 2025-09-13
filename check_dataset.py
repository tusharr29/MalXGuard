import os

data_dir = r"C:\Users\Tushar Deshmukh\OneDrive\Desktop\MalXGuard\dataSample"

asm_files = [f for f in os.listdir(data_dir) if f.endswith(".asm")]
bytes_files = [f for f in os.listdir(data_dir) if f.endswith(".bytes")]

print("📂 Dataset check:")
print(f"  .asm files  : {len(asm_files)}")
print(f"  .bytes files: {len(bytes_files)}")

if len(asm_files) > 0:
    print("Example .asm file:", asm_files[0])
if len(bytes_files) > 0:
    print("Example .bytes file:", bytes_files[0])
