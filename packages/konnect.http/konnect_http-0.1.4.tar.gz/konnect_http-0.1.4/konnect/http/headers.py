# Copyright 2023  Dom Sekotill <dom.sekotill@kodo.org.uk>

"""

"""

def encode_header(name: str|bytes, value: bytes) -> bytes:
	if isinstance(name, str):
		name = name.encode("ascii")
	return b":".join((name, value))
