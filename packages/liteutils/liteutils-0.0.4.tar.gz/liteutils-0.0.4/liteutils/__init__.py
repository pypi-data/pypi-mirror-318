#!/usr/bin/env python
# coding=utf-8

# Copyright 2024 Your Name. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__version__ = "1.1.0.dev0"

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._pymupdf import read_pdf, read_pdf_with_pages

_read_pdf = None
_read_pdf_with_pages = None

def _ensure_imported():
    global _read_pdf, _read_pdf_with_pages
    if _read_pdf is None or _read_pdf_with_pages is None:
        pymupdf_module = importlib.import_module(
            name='._pymupdf',
            package='liteutils'
        )
        _read_pdf = pymupdf_module.read_pdf
        _read_pdf_with_pages = pymupdf_module.read_pdf_with_pages

def read_pdf(*args, **kwargs):
    _ensure_imported()
    return _read_pdf(*args, **kwargs)

def read_pdf_with_pages(*args, **kwargs):
    _ensure_imported()
    return _read_pdf_with_pages(*args, **kwargs)

# Optionally, you can expose the functions directly
__all__ = ['read_pdf', 'read_pdf_with_pages']