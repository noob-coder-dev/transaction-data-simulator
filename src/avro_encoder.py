import io
import avro.schema
import avro.io

from transaction_metadata.loader import load_schema


class AvroEncoder:
    def __init__(self, entity: str, version: str = "v1"):
        """
        entity: "transaction" or "user"
        version: schema version (default v1)
        """
        self.schema_dict = load_schema(entity, version)
        self.schema = avro.schema.parse(str(self.schema_dict))

    def encode(self, record: dict) -> bytes:
        """Convert dict → Avro binary."""
        bytes_writer = io.BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        writer = avro.io.DatumWriter(self.schema)
        writer.write(record, encoder)
        return bytes_writer.getvalue()