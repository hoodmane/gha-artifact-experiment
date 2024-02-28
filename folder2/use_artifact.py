from pathlib import Path

dist_path = Path(__file__).parent / "dist"
artifact_path = Path(__file__).parent.parent / "folder1/dist/artifact.txt"
text = artifact_path.read_text()
text += "def\n"

(dist_path/"output.txt").write_text(text)
