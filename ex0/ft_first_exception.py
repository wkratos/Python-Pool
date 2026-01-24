"""Check temperature suitability for plants with exception handling."""


def check_temperature(temp_str) -> str:
    """Function to check if the temperature is suitable for plants."""
    try:
        temp = int(temp_str)
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"
    if 0 <= temp <= 40:
        return f"Temperature {temp}°C is perfect for plants!"
    elif temp < 0:
        return f"Error: {temp}°C is too cold for plants (min 0°C)"
    else:
        return f"Error: {temp}°C is too hot for plants (max 40°C)"


def test_temperature_input() -> None:
    """Function to test various temperature inputs."""
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    print(check_temperature("25"))
    print("\nTesting temperature: abc")
    print(check_temperature("abc"))
    print("\nTesting temperature: 100")
    print(check_temperature("100"))
    print("\nTesting temperature: -50")
    print(check_temperature("-50"))
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
