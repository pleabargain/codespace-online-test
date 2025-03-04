import math
import sys

class MoonLander:
    def __init__(self):
        self.altitude = 1000.0  # meters
        self.velocity = 0.0     # meters per second
        self.fuel = 100.0       # liters
        self.gravity = 1.62     # moon gravity in m/s^2
        self.thrust = 0.0       # thrust force

    def apply_thrust(self, thrust):
        if thrust > self.fuel:
            thrust = self.fuel
        self.fuel -= thrust
        self.thrust = thrust

    def update(self, time):
        # Calculate acceleration
        acceleration = self.thrust - self.gravity
        # Update velocity
        self.velocity += acceleration * time
        # Update altitude
        self.altitude += self.velocity * time - 0.5 * acceleration * time ** 2

        # Ensure altitude does not go below zero
        if self.altitude < 0:
            self.altitude = 0

    def display_status(self):
        print(f"Altitude: {self.altitude:.2f} m, Velocity: {self.velocity:.2f} m/s, Fuel: {self.fuel:.2f} L")

    def has_landed(self):
        return self.altitude == 0

    def has_crashed(self):
        return self.altitude == 0 and self.velocity < -2.0

def main():
    lander = MoonLander()
    time_step = 1.0  # one second time step

    print("Welcome to the Moon Lander Simulator!")
    print("Control the thrust to land the lunar module safely on the moon.")
    print("Thrust consumes fuel. If fuel runs out, you can't control the descent anymore.")
    print("Safe landing requires a velocity of less than 2 m/s on contact with the moon's surface.")
    print("Good luck!\n")

    while not lander.has_landed():
        lander.display_status()
        try:
            thrust = float(input("Enter thrust amount (0-10): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")
            continue

        if thrust < 0 or thrust > 10:
            print("Invalid thrust amount. Please enter a value between 0 and 10.")
            continue

        lander.apply_thrust(thrust)
        lander.update(time_step)

    lander.display_status()
    if lander.has_crashed():
        print("You have crashed on the moon's surface.")
    else:
        print("Congratulations! You have landed safely on the moon.")

if __name__ == "__main__":
    main()