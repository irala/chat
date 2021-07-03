from __future__ import print_function

import os
import time
from pathlib import Path
from pprint import pprint
from typing import Any, Dict

import connexion
import prance


def get_bundled_specs(main_file: Path) -> Dict[str, Any]:
    parser = prance.ResolvingParser(
        str(main_file.absolute()), lazy=False, backend="openapi-spec-validator"
    )
    parser.parse()
    return parser.specification

print(f"{'identity'} starting..." )

if __name__ == "__main__" or __name__ == "identity":

    options = {"swagger_ui": False}
    app = connexion.App(
        __name__,
        specification_dir="",
        options=options,
    )
    app.add_api(
        get_bundled_specs(
            Path(
                "openapi/api_chat/identity/login.v1.yaml"
            )
        ),
    )

    # only run manually if main, don't do it if running from gunicorn
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5001, debug=True)
