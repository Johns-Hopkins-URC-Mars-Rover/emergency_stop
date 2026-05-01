# Rover Base Signal Monitor

This package provides a ROS2-based monitoring system for a rover that listens for periodic signals from a base station. If the signal is lost for more than 3 seconds, the rover is automatically stopped.

## Overview

The system consists of two nodes:

- **`signal_publisher`** – Simulates a base station by publishing a continuous signal.
- **`signal_subscriber`** – Listens for the signal and stops the rover if the signal is lost.

---

## Files

### `signal_publisher.py`

Publishes a `String` message to the `base_signal` topic every second.

```python
msg.data = "base station signal"
```

This simulates a heart‑beat signal from a base station.

### `signal_subscriber.py`

Subscribes to the `base_signal` topic. It:

1. Records the timestamp of every received signal.
2. Runs a timer that checks how much time has passed since the last signal.
3. If **3 seconds or more** elapse without a signal, it publishes a stop command to the rover’s motor controller.

The stop command is a JSON string:

```json
{"speed": 0, "heading": 0}
```

The actual sending is handled by an external `base_motor.PublisherSubscriber.publisher` module.

---

## Dependencies

- ROS2 (tested with Humble / Foxy / Galactic)
- `rclpy`
- `std_msgs`
- Custom module: `base_motor.PublisherSubscriber.publisher` (must provide a `Publisher` class with a `publish()` method)

---

## Running the System

**Terminal 1 – Start the base station signal publisher:**

```bash
ros2 run package signal_publisher
```

**Terminal 2 – Start the signal subscriber (rover node):**

```bash
ros2 run package signal_subscriber
```

---

## Expected Behavior

- The publisher sends a signal every second.
- The subscriber logs:  
  `Received signal`  
  `Time since last message: X.XX seconds`
- If the publisher is stopped or loses connection, the subscriber will log:  
  `No signal received! Stopping rover.`  
  and send the stop command to the motors.

---

## Customization

- **Signal loss timeout** – Change `3.0` seconds in `timer_callback()` if needed.
- **Publishing rate** – Modify the timer interval in `signal_publisher.py` (default: 1.0 second).
- **Stop command** – Edit the `stop_rover()` method to match your motor driver’s expected message format.

---

## Notes

- The `base_motor` module is not included – you must provide or adapt the motor publisher according to your rover’s hardware interface.
- For real‑world use, the publisher would run on a base station computer, and the subscriber on the rover’s onboard computer, communicating over a wireless network.
