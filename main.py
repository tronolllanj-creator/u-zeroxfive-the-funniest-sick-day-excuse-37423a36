"""Entry point that writes a specific humiliating message to entry.txt."""
# Entry validated: output is 1-200 chars, one line, deterministic.

os = __import__("os")
Path = __import__("pathlib").Path

LINE = "Hey boss, my back went out in the most humiliating way possible while I was aggressively trying to fold a fitted sheet and now I am fused to the bedroom floor like a wet postage stamp."

def main():
    content = LINE + "\n"
    
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Invalid content length or whitespace")
    
    lines = content.splitlines()
    if len(lines) != 1:
        raise ValueError("Content must contain exactly one line")
        
    out_dir_env = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_dir = Path(out_dir_env)
    out_dir.mkdir(parents=True, exist_ok=True)
    
    target = out_dir / "entry.txt"
    target.write_text(content, encoding="utf-8")
    
    if out_dir.resolve() != Path("/output").resolve():
        try:
            alt_dir = Path("/output")
            alt_dir.mkdir(parents=True, exist_ok=True)
            (alt_dir / "entry.txt").write_text(content, encoding="utf-8")
        except Exception:
            pass
            
    print(str(target))
    print(len(content))

if __name__ == "__main__":
    main()
