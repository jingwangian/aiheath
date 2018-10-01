#!/usr/bin/env python3

import pytest
import os
import sys

print(sys.path)

from doctor.doctor import Doctor


class TestDoctor:
    def test_init(self):
        doctor = Doctor("Medius")
        assert doctor.name == "Medius"

    @pytest.mark.parametrize('description, symptom', (
        ("pain in stomach", "abdominal pain"),
        ("stomach pained", "abdominal pain"),
        ("head pained", "unknown"),
        ("feeling good", "unknown"),
    ))
    def test_analyze(self, description, symptom):
        doctor = Doctor("Medius")
        assert doctor.analyze(description) == symptom
