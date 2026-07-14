import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "resume"


def load_schema(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def test_resume_schemas_are_valid_json():
    schema_paths = sorted(SCHEMA_DIR.glob("*.schema.json"))
    assert schema_paths, "expected Resume schemas"
    for schema_path in schema_paths:
        schema = load_schema(schema_path)
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["$id"].startswith("https://careerforge.dev/schemas/resume/")


def test_resume_schemas_use_provider_neutral_version():
    for schema_path in SCHEMA_DIR.glob("*.schema.json"):
        schema = load_schema(schema_path)
        assert schema["properties"]["schema_version"]["const"] == "careerforge.resume.v0.1"
        serialized = json.dumps(schema).lower()
        for provider_name in ("openai", "anthropic", "gemini", "claude", "llama"):
            assert provider_name not in serialized


def test_verified_resume_sections_require_provenance_refs():
    schema = load_schema(SCHEMA_DIR / "resume-section.schema.json")
    required = set(schema["required"])
    assert {"section_id", "section_type", "fact_state", "content", "source_entity_ids", "explanation"}.issubset(required)
    verified_rule = schema["allOf"][0]
    assert verified_rule["if"]["properties"]["fact_state"]["const"] == "verified"
    assert "provenance_refs" in verified_rule["then"]["required"]


def test_resume_recommendations_include_explanations_and_sources():
    schema = load_schema(SCHEMA_DIR / "resume-recommendation.schema.json")
    required = set(schema["required"])
    assert {"source_entity_ids", "recommendation_type", "rationale", "expected_impact", "improvement_category"}.issubset(required)
    assert schema["properties"]["source_entity_ids"]["minItems"] == 1
