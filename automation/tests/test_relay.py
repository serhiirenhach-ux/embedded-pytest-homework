import pytest



def test_led_on_off(device):
    assert device.command("SET LED ON")["led"] is True
    assert device.command("SET LED OFF")["led"] is False

def test_reset_restores_safe_state(device):
    device.command("SET LED ON")
    device.command("RESET")
    status = device.command("STATUS")
    assert status["pwm"] == 0
    assert status["led"] is False
    
@pytest.mark.parametrize("commands", [
    "SET LED",         
    "SET LED MAYBE",    
    "SET LED on",       
    "SET LED 1",        
    "SET LEDON"])
def test_led_without_argument_is_unknown(device, commands):
    r = device.command(commands)
    assert r["status"] == "ERROR"
    assert r["code"] == "UNKNOWN_COMMAND"

