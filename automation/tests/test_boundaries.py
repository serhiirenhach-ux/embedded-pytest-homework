import pytest

@pytest.mark.parametrize("value", [0, 1, 50, 99, 100])
def test_pwm_valid_boundaries(device, value):
    r = device.command(f"SET PWM {value}")
    assert r["status"] == "OK"
    assert r["pwm"] == value

@pytest.mark.parametrize("value", [-1, 101, 999])
def test_pwm_invalid_boundaries(device, value):
    r = device.command(f"SET PWM {value}")
    assert r["status"] == "ERROR"
    assert r["code"] == "INVALID_VALUE"
    
@pytest.mark.parametrize("value_char", ["a", "o", "reset"])
def test_pwm_invalid_boundaries_chars(device, value_char):
    r = device.command(f"SET PWM {value_char}")
    assert r["status"] == "ERROR"
    assert r["code"] == "INVALID_VALUE"
