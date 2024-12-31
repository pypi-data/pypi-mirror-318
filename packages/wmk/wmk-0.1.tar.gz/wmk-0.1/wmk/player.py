import pyglet
import os
from typing import Dict, Optional, Callable, Any, Union

class Player(pyglet.window.Window):
    streamer_key_codes: Dict[str, int] = {
        "KEY_1": pyglet.window.key._1,
        "KEY_2": pyglet.window.key._2,
        "KEY_3": pyglet.window.key._3,
        "KEY_W": pyglet.window.key.W,
        "KEY_E": pyglet.window.key.E,
        "KEY_R": pyglet.window.key.R, 
        "KEY_ENTER": pyglet.window.key.ENTER,
        "KEY_LEFTCTRL": pyglet.window.key.LCTRL,
        "KEY_A": pyglet.window.key.A,
        "KEY_S": pyglet.window.key.S,
        "KEY_D": pyglet.window.key.D,
        "KEY_LEFTSHIFT": pyglet.window.key.LSHIFT,
        "KEY_M": pyglet.window.key.M,
        "KEY_DOT": pyglet.window.key.PERIOD,
        "KEY_SPACE": pyglet.window.key.SPACE,
        "KEY_UP": pyglet.window.key.UP,
        "KEY_LEFT": pyglet.window.key.LEFT,
        "KEY_RIGHT": pyglet.window.key.RIGHT,
        "KEY_DOWN": pyglet.window.key.DOWN,
    }

    def __init__(self, 
                 width: int, 
                 height: int, 
                 frame_generator: Callable[[Dict[int, bool], Dict[str, Union[bool, float]]], Any], 
                 fps: int = 30, 
                 mouse_sensitivity: float = 1.0,
                 input_device_name: Optional[str] = None) -> None:
        super().__init__(width, height, caption="Player")
        self.frame_generator: Callable = frame_generator
        self.keyboard_state: Dict[int, bool] = {}
        self.mouse_state: Dict[str, Union[bool, float]] = {}
        self.mouse_sensitivity: float = mouse_sensitivity
        self.fps: int = fps
        self.input_device_name: Optional[str] = input_device_name if os.name == "posix" else None
        self.input_device: Optional[Any] = None

        # If no input device is specified, set up local input handlers
        if not self.input_device_name:
            self.set_handlers(
                on_key_press=self.local_key_press,
                on_key_release=self.local_key_release,
                on_mouse_press=self.local_mouse_press,
                on_mouse_release=self.local_mouse_release,
                on_mouse_motion=self.local_mouse_motion
            )

        # Set up the sprite for frame display
        self.sprite: Optional[pyglet.sprite.Sprite] = None

        # Schedule the update function
        pyglet.clock.schedule_interval(self.update, 1.0/fps)

    def render_frame(self, frame: Any) -> None:
        # Convert numpy array to pyglet image
        height, width = frame.shape[:2]
        img = pyglet.image.ImageData(width, height, 'RGB', frame.tobytes())
        scale_x = self.width / width
        scale_y = self.height / height
        # Create or update sprite
        if self.sprite:
            self.sprite.delete()
        self.sprite = pyglet.sprite.Sprite(img)
        self.sprite.scale = min(scale_x, scale_y)

    def on_draw(self) -> None:
        self.clear()
        if self.sprite:
            self.sprite.draw()

    def local_key_press(self, symbol: int, modifiers: int) -> None:
        self.keyboard_state[symbol] = True

    def local_key_release(self, symbol: int, modifiers: int) -> None:
        self.keyboard_state[symbol] = False

    def local_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button == pyglet.window.mouse.LEFT:
            self.mouse_state["LEFT_CLICK"] = True
        elif button == pyglet.window.mouse.MIDDLE:
            self.mouse_state["MIDDLE_CLICK"] = True
        elif button == pyglet.window.mouse.RIGHT:
            self.mouse_state["RIGHT_CLICK"] = True

    def local_mouse_release(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button == pyglet.window.mouse.LEFT:
            self.mouse_state["LEFT_CLICK"] = False
        elif button == pyglet.window.mouse.MIDDLE:
            self.mouse_state["MIDDLE_CLICK"] = False
        elif button == pyglet.window.mouse.RIGHT:
            self.mouse_state["RIGHT_CLICK"] = False

    def local_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> None:
        self.mouse_state["MOVE_X"] = dx * self.mouse_sensitivity
        self.mouse_state["MOVE_Y"] = dy * self.mouse_sensitivity

    def remote_key_event(self, name: str, is_pressed: bool) -> None:
        if name.startswith("KEY"):
            key = self.streamer_key_codes.get(name)
            if key is not None:
                self.keyboard_state[key] = is_pressed
        elif name == "BTN_LEFT":
            self.mouse_state["LEFT_CLICK"] = is_pressed
        elif name == "BTN_RIGHT":
            self.mouse_state["RIGHT_CLICK"] = is_pressed
        elif name == "BTN_MIDDLE":
            self.mouse_state["MIDDLE_CLICK"] = is_pressed

    def remote_mouse_motion(self, name: str, value: float) -> None:
        if name == "REL_X":
            self.mouse_state["MOVE_X"] = value * self.mouse_sensitivity
        elif name == "REL_Y":
            self.mouse_state["MOVE_Y"] = -value * self.mouse_sensitivity
    

    def initialize_input_device(self) -> None:
        if not self.input_device_name:
            return

        devices = pyglet.input.get_devices()
        for device in devices:
            if device.name == self.input_device_name and device.__class__.__name__ == "EvdevDevice":
                print(f'Input device found: {device.name}')
                try:
                    device.open(window=self, exclusive=True)
                    controls = device.get_controls()
                    for control in controls:
                        print(f'Control: {control}')
                        if control.__class__.__name__ == "Button":
                            control.on_press = lambda c=control: self.remote_key_event(c.raw_name, True)
                            control.on_release = lambda c=control: self.remote_key_event(c.raw_name, False)
                        elif control.__class__.__name__ == "RelativeAxis":
                            control.on_change = lambda value, c=control: self.remote_mouse_motion(c.raw_name, value)

                    self.input_device = device
                    print("Input Device Initialized")
                except Exception as e:
                    print("Error Initializing Input Device")
                    print(e)
                    self.input_device = None
                break
        
        if self.input_device is None:
            print("Input Device not Found")

    def update(self, dt: float) -> None:
        if self.input_device_name and self.input_device is None:
            self.initialize_input_device()
 
        frame = self.frame_generator(self.keyboard_state, self.mouse_state)
        if frame is None:
            pyglet.app.exit()
            return
        
        self.render_frame(frame)

    def run(self) -> bool:
        pyglet.app.run()
        return False