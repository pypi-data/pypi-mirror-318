import pyglet
from typing import Dict, Optional, Callable, Any, Union

class Player(pyglet.window.Window):
    def __init__(self, 
                 width: int, 
                 height: int, 
                 frame_generator: Callable[[Dict[int, bool], Dict[str, Union[bool, float]]], Any], 
                 fps: int = 30, 
                 mouse_sensitivity: float = 1.0) -> None:
        super().__init__(width, height, caption="Player")
        self.frame_generator: Callable = frame_generator
        self.keyboard_state: Dict[int, bool] = {}
        self.mouse_state: Dict[str, Union[bool, float]] = {}
        self.mouse_sensitivity: float = mouse_sensitivity
        self.fps: int = fps
        
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

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        self.keyboard_state[symbol] = True

    def on_key_release(self, symbol: int, modifiers: int) -> None:
        self.keyboard_state[symbol] = False

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button == pyglet.window.mouse.LEFT:
            self.mouse_state["LEFT_CLICK"] = True
        elif button == pyglet.window.mouse.MIDDLE:
            self.mouse_state["MIDDLE_CLICK"] = True
        elif button == pyglet.window.mouse.RIGHT:
            self.mouse_state["RIGHT_CLICK"] = True

    def on_mouse_release(self, x: int, y: int, button: int, modifiers: int) -> None:
        if button == pyglet.window.mouse.LEFT:
            self.mouse_state["LEFT_CLICK"] = False
        elif button == pyglet.window.mouse.MIDDLE:
            self.mouse_state["MIDDLE_CLICK"] = False
        elif button == pyglet.window.mouse.RIGHT:
            self.mouse_state["RIGHT_CLICK"] = False

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> None:
        self.mouse_state["MOVE_X"] = dx * self.mouse_sensitivity
        self.mouse_state["MOVE_Y"] = dy * self.mouse_sensitivity

    def update(self, dt: float) -> None:
        frame = self.frame_generator(self.keyboard_state, self.mouse_state)
        if frame is None:
            pyglet.app.exit()
            return
        
        self.render_frame(frame)

    def run(self) -> bool:
        self.activate()
        pyglet.app.run()
        return False