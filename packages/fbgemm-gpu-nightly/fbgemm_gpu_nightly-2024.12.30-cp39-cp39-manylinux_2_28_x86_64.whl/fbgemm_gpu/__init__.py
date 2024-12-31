#!/usr/bin/env python3
# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import logging
import os

import torch


def _load_library(filename: str) -> None:
    """Load a shared library from the given filename."""
    try:
        torch.ops.load_library(os.path.join(os.path.dirname(__file__), filename))
        logging.info(f"Successfully loaded: '{filename}'")
    except Exception as error:
        logging.error(f"Could not load the library '{filename}': {error}")
        raise error


# Since __init__.py is only used in OSS context, we define `open_source` here
# and use its existence to determine whether or not we are in OSS context
open_source: bool = True

# Trigger the manual addition of docstrings to pybind11-generated operators
import fbgemm_gpu.docs  # noqa: F401, E402

try:
    # Export the version string from the version file auto-generated by setup.py
    from fbgemm_gpu.docs.version import __variant__, __version__  # noqa: F401, E402
except Exception:
    __variant__: str = "INTERNAL"
    __version__: str = "INTERNAL"

fbgemm_gpu_libraries = [
    "fbgemm_gpu_config",
    "fbgemm_gpu_tbe_utils",
    "fbgemm_gpu_tbe_index_select",
    "fbgemm_gpu_tbe_optimizers",
    "fbgemm_gpu_tbe_inference",
    "fbgemm_gpu_tbe_training_forward",
    "fbgemm_gpu_tbe_training_backward",
    "fbgemm_gpu_py",
]

libraries_to_load = {
    "cpu": fbgemm_gpu_libraries,
    "cuda": fbgemm_gpu_libraries
    + [
        "experimental/gen_ai/fbgemm_gpu_experimental_gen_ai_py",
    ],
    "genai": [
        "experimental/gen_ai/fbgemm_gpu_experimental_gen_ai_py",
    ],
    "rocm": fbgemm_gpu_libraries,
}

for library in libraries_to_load.get(__variant__, []):
    _load_library(f"{library}.so")

try:
    # Trigger meta operator registrations
    from . import sparse_ops  # noqa: F401, E402
except Exception:
    pass
