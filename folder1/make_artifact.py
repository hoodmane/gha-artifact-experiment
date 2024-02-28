from pathlib import Path

dist_path = Path(__file__).parent / "dist"
dist_path.mkdir(exist_ok=True)
(dist_path / "artifact.txt").write_text("abc\n")
