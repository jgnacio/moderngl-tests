import moderngl_window as mglw
import math

class Test(mglw.WindowConfig):
    window_size = (800, 600)
    resource_dir = 'basics/shaders'
    move = [0, 0]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.quad = mglw.geometry.quad_fs()
        self.program = self.load_program(vertex_shader="vertex.glsl", fragment_shader="fragment.glsl")
        self.set_uniform('resolution', self.window_size)
        

    def set_uniform(self, u_name, u_value):
        try:
            self.program[u_name] = u_value
        except KeyError:
            #print(f"Uniform: {u_name} - not used in this shader")
            pass

    def key_event(self, key, action, modifiers):
        if action == self.wnd.keys.ACTION_PRESS:
            if key == self.wnd.keys.A:
                self.move[0] -= 0.1
                print("A")
            if key == self.wnd.keys.D:
                self.move[0] += 0.1
                print("D")
            if key == self.wnd.keys.W:
                self.move[1] += 0.1
                print("W")
            if key == self.wnd.keys.S:
                self.move[1] -= 0.1
                print("S")
    
    def mouse_position_event(self, x, y, dx, dy):
        # To convert the pixels of the screen in a range
        # 0 to 1 I divide the x into window_size, to get
        # the range 1 to 0, substract 1 from the entire
        # calculation before and finally to get all range
        # in x axis: (1, -1)
        # in y axis: (-1, 1)
        self.move[0] = 1 - x / self.window_size[0] * 2
        self.move[1] = -(1 - y / self.window_size[1] * 2)
        print(self.move[0], self.move[1])

    def render(self, time, frametime):
        # This method is called every frame
        self.ctx.clear()
        self.set_uniform('time', math.sin(time))
        self.set_uniform('move', self.move)
        self.quad.render(self.program)

# Blocking call entering rendering/event loop
if __name__ == "__main__":
    mglw.run_window_config(Test)