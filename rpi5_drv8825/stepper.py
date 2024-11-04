from typing import Literal
import gpiozero as GPIO
import time

class StepperMotor:
    def __init__(self, direction_pin: int, step_pin: int, enable_pin: int) -> None:
        self.direction = GPIO.DigitalOutputDevice(direction_pin)
        self.step = GPIO.DigitalOutputDevice(step_pin)
        self.enable = GPIO.DigitalOutputDevice(enable_pin)

    def enable(self) -> None:
        """Enables the motor driver (active low)."""
        self.enable.value = False

    def disable(self) -> None:
        """Disables the motor driver (active low)."""
        self.enable.value = True

    def forward(self, steps: int, step_delay: float) -> None:
        """Moves the motor forward (clockwise).

        Args:
            steps (int): Number of steps to move forward.
            step_delay (float): Delay between steps in seconds.
        """
        self._set_direction('forward')
        self._step(steps, step_delay)

    def backward(self, steps: int, step_delay: float) -> None:
        """Moves the motor backward (counterclockwise).

        Args:
            steps (int): Number of steps to move backward.
            step_delay (float): Delay between steps in seconds.
        """
        self.set_direction('backward')
        self._step(steps, step_delay)
  
    def _set_direction(self, direction: Literal['forward', 'backward']) -> None:
        """Sets the motor direction.

        Args:
            direction (str): 'forward' or 'backward'
        """
        if direction.lower() == 'forward':
            self.direction.value = False  # Assuming low for forward
        elif direction.lower() == 'backward':
            self.direction.value = True   # Assuming high for backward
        else:
            raise ValueError("Direction must be 'forward' or 'backward'")

    def _step(self, steps: int, step_delay: float) -> None:
        """Performs the given number of steps.

        Args:
            steps (int): Number of steps to move.
            step_delay (float): Delay between steps in seconds.
        """
        if steps <= 0:
            raise ValueError("Number of steps must be positive")

        for _ in range(steps):
            self.step.value = True
            time.sleep(step_delay)
            self.step.value = False
            time.sleep(step_delay)
