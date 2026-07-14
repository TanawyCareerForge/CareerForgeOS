import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_DIR = ROOT / "schemas" / "ontology"


def load_schema(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def test_ontology_schemas_are_valid_json():
    schema_paths = sorted(SCHEMA_DIR.glob("*.schema.json"))
    assert schema_paths, "expected Ontology schemas"
    for schema_path in schema_paths:
        schema = load_schema(schema_path)
        assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
        assert schema["$id"].startswith("https://careerforge.dev/schemas/ontology/")


def test_ontology_schemas_use_provider_neutral_version():
    for schema_path in SCHEMA_DIR.glob("*.schema.json"):
        schema = load_schema(schema_path)
        assert schema["properties"]["schema_version"]["const"] == "careerforge.ontology.v0.1"
        serialized = json.dumps(schema).lower()
        for provider_name in ("openai", "anthropic", "gemini", "claude", "llama"):
            assert provider_name not in serialized


def test_verified_ontology_entities_require_provenance():
    schema = load_schema(SCHEMA_DIR / "ontology-entity.schema.json")
    required = set(schema["required"])
    assert {"entity_id", "entity_type", "fact_state", "sensitivity", "properties", "relationships"}.issubset(required)
    verified_rule = schema["allOf"][0]
    assert verified_rule["if"]["properties"]["fact_state"]["const"] == "verified"
    assert "provenance" in verified_rule["then"]["required"]


def test_ontology_relationships_include_explanation_evidence():
    schema = load_schema(SCHEMA_DIR / "ontology-relationship.schema.json")
    required = set(schema["required"])
    assert {"source_entity_id", "target_entity_id", "relationship_type", "evidence", "explanation"}.issubset(required)
    assert schema["properties"]["evidence"]["minItems"] == 1
    assert set(schema["properties"]["explanation"]["required"]) == {"path", "rationale"}
