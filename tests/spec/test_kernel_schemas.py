import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "kernel"


def load_schema(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def test_kernel_schemas_are_valid_json():
    schema_paths = sorted(SCHEMA_DIR.glob("*.schema.json"))
    assert schema_paths, "expected Kernel schemas"
    for schema_path in schema_paths:
        schema = load_schema(schema_path)
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["$id"].startswith("https://careerforge.dev/schemas/kernel/")


def test_kernel_schemas_use_provider_neutral_version():
    for schema_path in SCHEMA_DIR.glob("*.schema.json"):
        schema = load_schema(schema_path)
        assert schema["properties"]["schema_version"]["const"] == "careerforge.kernel.v0.1"
        serialized = json.dumps(schema).lower()
        for provider_name in ("openai", "anthropic", "gemini", "claude", "llama"):
            assert provider_name not in serialized


def test_approved_output_requires_validation_and_provenance():
    schema = load_schema(SCHEMA_DIR / "approved-output.schema.json")
    required = set(schema["required"])
    assert {"validation", "explanations", "provenance"}.issubset(required)
    assert schema["properties"]["validation"]["properties"]["status"]["const"] == "passed"
