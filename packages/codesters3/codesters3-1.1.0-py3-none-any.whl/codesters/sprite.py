import math
from PIL import Image, ImageTk
from .manager import Manager
from .hitbox import Hitbox
import inspect
import json
import os
import sys
from threading import Timer


DATA_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_DIR = os.path.dirname(os.path.realpath(sys.argv[0]))

METADATA_PATH = os.path.join(os.path.dirname(__file__), "sprites.json")
IMAGE_DICTIONARY = json.loads(open(METADATA_PATH).read())
for name, path in IMAGE_DICTIONARY.items():
    IMAGE_DICTIONARY[name] = os.path.join(DATA_DIR, path)
DEFAULT_SPRITE = IMAGE_DICTIONARY["codester"]


class SpriteClass(object):
    """The base class of the Sprite class
    This defines all methods of the Sprite class

    """
    ## PIVOTAL FUNCTIONS ##
    def __init__(self, image, x=0, y=0, **kwargs):
        self.canvas = Manager.canvas

        # Default values
        self.type = Sprite

        self.xcor = x
        self.ycor = y
        self.xspeed = 0
        self.yspeed = 0
        self.speed = 1
        self.modes = []
        self.size = 1
        self.future_size = 1
        self.color = 'black'
        self.heading = 0
        self.future_heading = self.heading
        self.width = 50
        self.height = 50

        if kwargs.get('shape') is None:
            self.photo = Image.open(IMAGE_DICTIONARY["codesters"])
            self.base_photo = Image.open(IMAGE_DICTIONARY["codesters"])
            self.base_photo_width = self.photo.size[0]
            self.base_photo_height = self.photo.size[1]
            self.height = self.base_photo_height
            self.width = self.base_photo_width

        self.forever_function = None

        self.hidden = False

        self.animation_duration = 1000
        self.animation_x_coords = []
        self.animation_y_coords = []
        self.animation_rotation_degrees = []
        self.animation_index = 0
        self.rotation_direction = 1
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.angle = 0
        self.step_size = 0

        self.wait_list = []
        self.total_wait_time = 0
        self.future_most_recent_wait_time = 0

        self.say_text = ""
        self.say_color = ""
        self.say_size = 0
        self.say_time = 0
        self.say_font = ""
        self.say_plans = []
        self.say_queue = []

        self.paused = False

        self.gravity = 1
        self.gravity_override = False
        self.gravity_true = Manager.default_gravity
        self.physics_true = True

        self.goal = False
        self.hazard = False
        self.collision = True
        self.drag = False

        self.key_functions = {}

        self.have_clicked = False

        # def click_on_sprite(event):
        #     hit = self.get_hitbox_edges()
        #     top = hit[0]
        #     right = hit[1]
        #     bottom = hit[2]
        #     left = hit[3]
        #     ex = self.canvas.winfo_pointerx()
        #     ey = self.canvas.winfo_pointery()
        #     if left < ex < right and bottom < ey < top:
        #         self.have_clicked = True
        #
        # def release_sprite(event):
        #     self.have_clicked = False
        # self.canvas.bind("<Button-1>", click_on_sprite, add="+")
        # self.canvas.bind("<ButtonRelease-1>", release_sprite, add="+")

        self.event_bindings = {}

        self.opacity = 255

        self.x_flip_plans = []
        self.y_flip_plans = []
        self.x_flipped = False
        self.y_flipped = False
        self.future_x_flipped = False
        self.future_y_flipped = False
        self.dilate_plans = []
        self.scale_plans = []

        self.pen = False
        self.pen_color_var = self.color
        self.pen_size_var = 1
        self.lines = []

        self.pen_plans = []
        self.pen_color_plans = []
        self.pen_size_plans = []

        self.fill = False
        self.fill_color_var = self.pen_color_var
        self.fill_color_plans = []
        self.fill_plans = []
        self.polygons = []

        if image and kwargs.get('shape') is None:
            if os.path.isfile(image):
                # An explicit user-supplied path.
                self.image_path = image
            elif os.path.isfile(SCRIPT_DIR + image):
                # A user-supplied path relative to the script directory.
                self.image_path = SCRIPT_DIR + image
            elif image in IMAGE_DICTIONARY:
                # A library-supplied image.
                self.image_path = IMAGE_DICTIONARY[image]
            else:
                # A default for invalid input.
                self.image_path = DEFAULT_SPRITE

            self.base_photo = Image.open(self.image_path)
            self.photo = Image.open(self.image_path)

            im2 = self.photo.convert('RGBA')
            rot = im2.rotate(self.heading, expand=1)
            fff = Image.new("RGBA", rot.size, (0,)*4)
            self.photo = Image.composite(rot, fff, rot)

            self.base_photo_width = self.photo.size[0]
            self.base_photo_height = self.photo.size[1]
            self.height = self.base_photo_height
            self.width = self.base_photo_width
            self.image_name = image
            self.name = image

        self.shape = ''
        if kwargs.get('shape') is not None:
            self.shape = kwargs.get('shape')
            self.name = self.shape
            
        self.base_top_left = [-self.width/2, self.height/2]
        self.base_top_right = [self.width/2, self.height/2]
        self.base_bottom_right = [self.width/2, -self.height/2]
        self.base_bottom_left = [-self.width/2, -self.height/2]
        self.hitbox = Hitbox(self.base_top_right,
                             self.base_top_left,
                             self.base_bottom_right,
                             self.base_bottom_left, self)
        self.top_left = [self.xcor-self.width/2, self.ycor+self.height/2]
        self.top_right = [self.xcor+self.width/2, self.ycor+self.height/2]
        self.bottom_right = [self.xcor+self.width/2, self.ycor-self.height/2]
        self.bottom_left = [self.xcor-self.width/2, self.ycor-self.height/2]
        self.corners = [self.top_right, self.top_left, self.bottom_left, self.bottom_right]

        self.collision_function = None
        self.collision_goal_function = None
        self.collision_hazard_function = None

        Manager.elements.append(self)

    def draw(self):
        if self.forever_function is not None:
            self.forever_function()
        if self.photo is not None and not self.hidden:
            self.bg_photoimg = ImageTk.PhotoImage(self.photo)
            self.canvas.create_image((self.xcor + Manager.width,
                                      Manager.height - self.ycor),
                                     image=self.bg_photoimg)
        elif not self.hidden:
            self.canvas.create_oval((self.xcor-(self.size/2),
                                     self.ycor-(self.size/2),
                                     self.xcor+(self.size/2),
                                     self.ycor+(self.size/2)),
                                    fill=self.color)
        for p in self.polygons:
            self.canvas.create_polygon(tuple(p[0]), fill=p[1])
        for l in self.lines:
            self.canvas.create_line(l[0], fill=l[1], width=l[2])
        if self.say_time != 0:
            self.canvas.create_text(self.xcor + Manager.width,
                                    Manager.height - self.ycor - 100,
                                    text=self.say_text, font=(self.say_font, self.say_size),
                                    fill=self.say_color)
            self.say_time -= 1
        if self.say_time <= 0 < len(self.say_queue):
            # This is a really weird expression to chain like this, but it works, and pycharm keeps bugging me about it.

            self.say_text = self.say_queue[0][0]
            self.say_time = self.say_queue[0][1]
            self.say_color = self.say_queue[0][2]
            self.say_size = self.say_queue[0][3]
            self.say_font = self.say_queue[0][4]
            self.say_queue.pop(0)

    def update_physics(self):
        prevx = self.xcor
        prevy = self.ycor
        self.xcor += self.xspeed
        self.ycor += self.yspeed
        self.future_x += self.xspeed
        self.future_y += self.yspeed
        for i in range(len(self.animation_x_coords)):
            if not isinstance(self.animation_x_coords[i], str):
                self.animation_x_coords[i] += self.xspeed
            if not isinstance(self.animation_y_coords[i], str):
                self.animation_y_coords[i] += self.yspeed
        if self.gravity_true:
            self.yspeed -= self.gravity

        if self.pen:
            newline = []
            newline.append((Manager.width + prevx, Manager.height - prevy, Manager.width + self.xcor, Manager.height - self.ycor))
            newline.append(self.pen_color_var)
            newline.append(self.pen_size_var)
            self.lines.append(newline)
        if self.fill and self.pen:
            self.polygons[-1][0].append(Manager.width + self.xcor)
            self.polygons[-1][0].append(Manager.height - self.ycor)

        # self.hitbox.update_corners()

        hit = self.get_hitbox_edges()
        top = hit[0]
        right = hit[1]
        bottom = hit[2]
        left = hit[3]

        tempheight = top-bottom
        tempwidth = right-left

        if self.xspeed != 0 or self.yspeed != 0:
            if Manager.stage.wall_bottom_on:  # and self.gravity_true:
                if bottom < -Manager.height:
                    self.ycor = -Manager.height + tempheight/2
                    self.yspeed = abs(self.yspeed * Manager.stage.bounce)

            if Manager.stage.wall_top_on:  # and self.gravity_true:
                if top > Manager.height:
                    self.ycor = Manager.height - tempheight/2
                    self.yspeed = -abs(self.yspeed * Manager.stage.bounce)

            if Manager.stage.wall_left_on:  # and self.gravity_true:
                if left < -Manager.width:
                    self.xcor = -Manager.width + tempwidth/2
                    self.xspeed = abs(self.xspeed * Manager.stage.bounce)

            if Manager.stage.wall_right_on:  # and self.gravity_true:
                if right > Manager.width:
                    self.xcor = Manager.width - tempwidth/2
                    self.xspeed = -abs(self.xspeed * Manager.stage.bounce)

        self.hitbox.update_corners()

    def clear_queue(self):
        # This function clears whatever the sprite has left to do, excepting some certain specific things.
        # Some instantaneous actions it out to finish up.
        # It's mostly continuous motion that has to be stopped.
        # To be called in case of a collision or event that would interfere with motion.
        skips = ['say', 'wait']  # ,'pen', 'pen_color', 'pen_size', 'pen_clear', 'fill', 'fill_color', 'print_corners']
        while (len(self.animation_x_coords) > 1 and isinstance(self.animation_x_coords[1], str)) or\
                (len(self.animation_rotation_degrees) > 1 and isinstance(self.animation_rotation_degrees[1], str)) or\
                (len(self.scale_plans) > 1 and isinstance(self.scale_plans[1], str)) or\
                (len(self.dilate_plans) > 1 and isinstance(self.dilate_plans[1], str)) or\
                (len(self.modes) > 0 and self.modes[0] in skips):
            self.update_animation()
            self.update_animation()
        self.future_x = self.xcor
        self.future_y = self.ycor
        self.future_heading = self.heading
        self.future_size = self.size
        self.future_y_flipped = self.y_flipped
        self.future_x_flipped = self.x_flipped
        self.animation_x_coords = []
        self.animation_y_coords = []
        self.animation_rotation_degrees = []
        # self.wait_list = []
        # self.say_plans = []
        self.pen_size_plans = []
        self.pen_plans = []
        self.pen_color_plans = []
        self.dilate_plans = []
        self.fill_color_plans = []
        self.fill_plans = []
        self.scale_plans = []
        self.x_flip_plans = []
        self.y_flip_plans = []

        for i in self.modes:
            if i not in skips:
                self.modes.remove(i)

    def update_collision(self, i):
        if self.collision or self.hazard or self.goal:
            for e in Manager.elements[i:]:
                if isinstance(e, SpriteClass):
                    if self.check_two_sprites_for_collision(e):
                        if e.goal or e.hazard or e.collision:
                            #  self.clear_queue()
                            e.clear_queue()

                        # TODO we're double checking some elements here, this can be more efficiecnt

                        if e.goal and self.collision_goal_function is not None:
                            if len(inspect.signature(self.collision_goal_function).parameters) == 2:
                                self.collision_goal_function(self, e)
                            elif len(inspect.signature(self.collision_goal_function).parameters) == 1:
                                self.collision_goal_function(Manager.elements.index(e))
                            else:
                                self.collision_goal_function()
                        elif e.hazard and self.collision_hazard_function is not None:
                            if len(inspect.signature(self.collision_hazard_function).parameters) == 2:
                                self.collision_hazard_function(self, e)
                            elif len(inspect.signature(self.collision_hazard_function).parameters) == 1:
                                self.collision_hazard_function(Manager.elements.index(e))
                            else:
                                self.collision_hazard_function()
                        elif e.collision and self.collision_function is not None:
                            if len(inspect.signature(self.collision_function).parameters) >= 2:
                                self.collision_function(self, e)
                            elif len(inspect.signature(self.collision_function).parameters) == 1:
                                self.collision_function(Manager.elements.index(e))
                            else:
                                self.collision_function()

                        if self.goal and e.collision_goal_function is not None:
                            if len(inspect.signature(e.collision_goal_function).parameters) == 2:
                                e.collision_goal_function(e, self)
                            elif len(inspect.signature(e.collision_goal_function).parameters) == 1:
                                e.collision_goal_function(Manager.elements.index(self))
                            else:
                                e.collision_goal_function()
                        elif self.hazard and e.collision_hazard_function is not None:
                            if len(inspect.signature(e.collision_hazard_function).parameters) == 2:
                                e.collision_hazard_function(e, self)
                            elif len(inspect.signature(e.collision_hazard_function).parameters) == 1:
                                e.collision_hazard_function(Manager.elements.index(self))
                            else:
                                self.collision_hazard_function()
                        elif self.collision and e.collision_function is not None:
                            if len(inspect.signature(e.collision_function).parameters) >= 2:
                                e.collision_function(e, self)
                            elif len(inspect.signature(e.collision_function).parameters) == 1:
                                e.collision_function(Manager.elements.index(self))
                            else:
                                e.collision_function()

                        self.update_animation()
                        e.update_animation()

    def update_events(self):
        for key in Manager.keys_pressed:
            if key in list(self.key_functions.keys()) and Manager.frame_number % Manager.event_delay == 0:
                #  self.clear_queue()
                for i in self.key_functions[key]:
                    if len(inspect.signature(i).parameters) == 0:
                        i()
                    elif len(inspect.signature(i).parameters) == 1:
                        i(self)
        if self.drag:
            if Manager.mouse_down and self.have_clicked:
                hit = self.get_hitbox_edges()
                top = hit[0]
                right = hit[1]
                bottom = hit[2]
                left = hit[3]
                ex = self.canvas.winfo_pointerx()
                ey = self.canvas.winfo_pointery()
                if left < ex < right and bottom < ey < top:
                    #  self.clear_queue()
                    changex = ex - self.xcor
                    changey = ey - self.ycor
                    self.xcor = ex
                    self.ycor = ey
                    self.future_x = ex
                    self.future_y = ey
                    self.set_x_speed(0)
                    self.set_y_speed(0)
                    for i in range(len(self.animation_x_coords)):
                        if not isinstance(self.animation_x_coords[i], str):
                            self.animation_x_coords[i] += changex
                        if not isinstance(self.animation_y_coords[i], str):
                            self.animation_y_coords[i] += changey

    def check_two_sprites_for_collision(self, sprite):
        this_edges = self.get_hitbox_edges()
        sprite_edges = sprite.get_hitbox_edges()
        if this_edges[0] > sprite_edges[2] and this_edges[2] < sprite_edges[0]:
            if this_edges[1] > sprite_edges[3] and this_edges[3] < sprite_edges[1]:
                if self != sprite:
                    return True
        return False

    def get_hitbox_edges(self):
        hit_x = [self.hitbox.top_left[0], self.hitbox.top_right[0], self.hitbox.bottom_left[0], self.hitbox.bottom_right[0]]
        hit_y = [self.hitbox.top_left[1], self.hitbox.top_right[1], self.hitbox.bottom_left[1], self.hitbox.bottom_right[1]]
        return [max(hit_y), max(hit_x), min(hit_y), min(hit_x)]

    def update_image(self):
        if self.shape != '':
            pass
        else:
            im2 = self.base_photo.convert('RGBA')
            if (self.x_flipped) != (self.width < 0):
                im2 = im2.transpose(Image.FLIP_LEFT_RIGHT)
            if (self.y_flipped) != (self.height < 0):
                im2 = im2.transpose(Image.FLIP_TOP_BOTTOM)
            if self.size < 0:
                im2 = im2.transpose(Image.FLIP_LEFT_RIGHT)
                im2 = im2.transpose(Image.FLIP_TOP_BOTTOM)
            if self.opacity < 255:
                im2.putalpha(self.opacity)
            width = abs(int(self.size * self.width))
            height = abs(int(self.size * self.height))
            scale = im2.resize((width, height), Image.NEAREST)
            rot = scale.rotate(self.heading, expand=1)
            final = Image.new("RGBA", rot.size, (0,)*4)
            self.photo = Image.composite(rot, final, rot)

    def update_animation(self):
        try:
            if isinstance(self.future_x, str):
                self.future_x = self.xcor
            if isinstance(self.future_y, str):
                self.future_y = self.ycor
        except AttributeError:
            self.future_x = None
            self.future_y = None

        if len(self.modes) > 0 and not self.paused:
            if self.modes[0] == "wait":
                # print 'waiting'
                if len(self.wait_list) > 0:
                    if isinstance(self.wait_list[0], str):
                        self.wait_list.pop(0)
                        self.modes.pop(0)
                    elif self.wait_list[0] == 0:
                        self.wait_list.pop(0)
                    else:
                        self.wait_list[0] = self.wait_list[0] - 1
            elif self.modes[0] == "translate":
                if len(self.animation_y_coords) > 0 and len(self.animation_x_coords) > 0:
                    if isinstance(self.animation_x_coords[0], str) \
                            and isinstance(self.animation_y_coords[0], str):
                        self.animation_x_coords.pop(0)
                        self.animation_y_coords.pop(0)
                        self.modes.pop(0)
                    else:
                        prevx = self.xcor
                        prevy = self.ycor
                        self.xcor = (self.animation_x_coords.pop(0))
                        self.ycor = (self.animation_y_coords.pop(0))
                        if isinstance(self.xcor, str) or isinstance(self.ycor, str):
                            self.xcor = prevx
                            self.ycor = prevy
                        if self.pen:
                            newline = []
                            newline.append((Manager.width + prevx,
                                            Manager.height - prevy,
                                            Manager.width + self.xcor,
                                            Manager.height - self.ycor))
                            newline.append(self.pen_color_var)
                            newline.append(self.pen_size_var)
                            self.lines.append(newline)
                        if self.fill and self.pen:
                            self.polygons[-1][0].append(Manager.width + self.xcor)
                            self.polygons[-1][0].append(Manager.height - self.ycor)
                        if len(self.animation_x_coords) > 1:
                            self.future_x = self.animation_x_coords[-2]
                        if len(self.animation_y_coords) > 1:
                            self.future_y = self.animation_y_coords[-2]
                        if not self.physics_true:
                            self.hitbox.update_corners()
                else:
                    self.modes.pop(0)
            elif self.modes[0] == "rotate":
                if len(self.animation_rotation_degrees) > 0:
                    if isinstance(self.animation_rotation_degrees[0], str):
                        self.animation_rotation_degrees.pop(0)
                        self.modes.pop(0)
                    else:
                        self.heading = self.animation_rotation_degrees.pop(0)
                        if not self.physics_true:
                            self.hitbox.update_corners()
                        self.update_image()
            elif self.modes[0] == "xflip":
                if len(self.x_flip_plans) > 0:
                    state = self.x_flip_plans.pop(0)
                    self.x_flipped = state
                    self.update_image()
                    self.modes.pop(0)
            elif self.modes[0] == "yflip":
                if len(self.y_flip_plans) > 0:
                    state = self.y_flip_plans.pop(0)
                    self.y_flipped = state
                    self.update_image()
                    self.modes.pop(0)
            elif self.modes[0] == "scale":
                if len(self.scale_plans) > 0:
                    if isinstance(self.scale_plans[0], str):
                        self.modes.pop(0)
                        self.scale_plans.pop(0)
                    else:
                        self.size = self.scale_plans.pop(0)
                        self.update_image()
            elif self.modes[0] == "pen":
                if len(self.pen_plans) > 0:
                    self.pen = self.pen_plans.pop(0)
                    self.modes.pop(0)
            elif self.modes[0] == "pen_color":
                if len(self.pen_color_plans) > 0:
                    self.pen_color_var = self.pen_color_plans.pop(0)
                    self.modes.pop(0)
            elif self.modes[0] == "pen_size":
                if len(self.pen_size_plans) > 0:
                    self.pen_size_var = self.pen_size_plans.pop(0)
                    self.modes.pop(0)
            elif self.modes[0] == "pen_clear":
                self.lines = []
                self.polygons = []
                self.modes.pop(0)
            elif self.modes[0] == "fill":
                if len(self.fill_plans) > 0:
                    state = self.fill_plans.pop(0)
                    self.modes.pop(0)
                    if state and not self.fill:
                        color = self.fill_color_var
                        self.polygons.append([[Manager.width + self.xcor,
                                               Manager.height - self.ycor], color])
                    self.fill = state
            elif self.modes[0] == "fill_color":
                if len(self.fill_color_plans) > 0:
                    self.fill_color_var = self.fill_color_plans.pop(0)
                    self.modes.pop(0)
            elif self.modes[0] == "print_corners":
                print(self.get_name())
                print(self.hitbox.top_left, "top_left")
                print(self.hitbox.top_right, "top_right")
                print(self.hitbox.bottom_right, "bottom_right")
                print(self.hitbox.bottom_left, "bottom_left")
                self.modes.pop(0)
            elif self.modes[0] == "dilate":
                if len(self.dilate_plans) > 0:
                    self.set_size(self.dilate_plans[0])
                    self.xcor = self.future_x * self.dilate_plans[0]
                    self.dilate_plans.pop(0)
                self.modes.pop(0)
            elif self.modes[0] == "say":
                if len(self.say_plans) > 0:
                    # print'saying'
                    self.say_queue.append(self.say_plans[0])
                    self.say_plans.pop(0)
                self.modes.pop(0)

    def print_corners(self):
        self.hitbox.printCorners()

    ## END OF PIVOTAL FUNCTIONS ##

    def hide(self):
        self.hidden = True

    def show(self):
        self.hidden = False

    # Basic motion
    def move_right(self, amount):
        self.glide_to(self.future_x+amount, self.future_y)

    def move_left(self, amount):
        self.glide_to(self.future_x-amount, self.future_y)

    def move_down(self, amount):
        self.glide_to(self.future_x, self.future_y-amount)

    def move_up(self, amount):
        self.glide_to(self.future_x, self.future_y+amount)

    def move_forward(self, amount):
        angle = self.future_heading * (math.pi/180)
        if len(self.x_flip_plans) >= 1 and not self.x_flip_plans[-1]:
            desired_x = amount * math.cos(angle) + self.future_x
            desired_y = amount * math.sin(angle) + self.future_y
        elif not self.future_x_flipped and len(self.x_flip_plans) < 1:
            desired_x = amount * math.cos(angle) + self.future_x
            desired_y = amount * math.sin(angle) + self.future_y
        else:
            desired_x = -amount * math.cos(angle) + self.future_x
            desired_y = -amount * math.sin(angle) + self.future_y
        self.glide_to(desired_x, desired_y)

    def forward(self, amount):
        self.move_forward(amount)

    def move_backward(self, amount):
        self.move_forward(-1 * amount)

    def backward(self, amount):
        self.move_backward(amount)

    def move_back(self, amount):
        self.move_backward(amount)

    def back(self, amount):
        self.move_backward(amount)

    def movex(self, amount):
        self.glide_to(self.future_x+amount, self.future_y)

    def move_x(self, amount):
        self.glide_to(self.future_x+amount, self.future_y)

    def movey(self, amount):
        self.glide_to(self.future_x, self.future_y+amount)

    def move_y(self, amount):
        self.glide_to(self.future_x, self.future_y+amount)

    def translate_y(self, amount):
        self.glide_to(self.future_x, self.future_y+amount)

    def translate_x(self, amount):
        self.glide_to(self.future_x+amount, self.future_y)

    # More complex motion
    def go_to(self, newx, newy):
        if len(self.animation_x_coords) > 1:
            self.animation_x_coords[-2] = newx
            self.animation_y_coords[-2] = newy
        else:
            self.animation_x_coords.append(newx)
            self.animation_y_coords.append(newy)
            self.animation_x_coords.append("Finished current animation")
            self.animation_y_coords.append("Finished current animation")
            self.modes.append("translate")
        self.future_x = newx
        self.future_y = newy

    def goto(self, newx, newy):
        self.go_to(newx, newy)

    def glide_to(self, newx, newy):
        xdist = float(newx - self.future_x)
        ydist = float(newy - self.future_y)
        dist = math.sqrt(xdist**2 + ydist**2)
        frames_needed = ((dist/self.speed) / 12)
        if frames_needed == 0:
            frames_needed = 1
        x_step_size = xdist/frames_needed
        y_step_size = ydist/frames_needed
        tempx = self.future_x
        tempy = self.future_y
        for n in range(int(frames_needed)):
            self.animation_x_coords.append(tempx+(x_step_size+(x_step_size * n)))
            self.animation_y_coords.append(tempy+(y_step_size+(y_step_size * n)))
        self.animation_x_coords.append(newx)
        self.animation_y_coords.append(newy)
        self.animation_x_coords.append("Finished current animation")
        self.animation_y_coords.append("Finished current animation")
        self.modes.append("translate")
        self.future_x = newx
        self.future_y = newy

    def set_direction(self, tox, toy):
        if tox - self.future_x == 0:
            tox += 0.000001
        destination = math.atan(float(toy - self.future_y)/float(tox - self.future_x))*(180/math.pi)
        if tox - self.future_x < 0:
            destination += 180
        frames_needed = 12 / self.speed
        # frames_needed = (abs(self.future_heading - destination) / (self.speed*22))
        if frames_needed == 0:
            frames_needed = 1
        degree_rot = destination - self.future_heading
        self.step_size = float(degree_rot)/float(frames_needed)
        for n in range(int(frames_needed)):
            self.animation_rotation_degrees.append(self.step_size+(self.step_size*n)+self.future_heading)
        self.animation_rotation_degrees[-1] = destination
        self.animation_rotation_degrees.append("Finished current animation")
        self.modes.append("rotate")
        self.future_heading = destination

    def point_towards(self, tox, toy):
        self.set_direction(tox, toy)

    def turn_clockwise(self, degrees):
        destination = self.future_heading - degrees
        frames_needed = 12 / self.speed
        if frames_needed == 0:
            frames_needed = 1
        degree_rot = destination - self.future_heading
        self.step_size = float(degree_rot)/float(frames_needed)
        for n in range(int(frames_needed)):
            self.animation_rotation_degrees.append(self.step_size+(self.step_size*n)+self.future_heading)
        self.animation_rotation_degrees[-1] = destination
        self.animation_rotation_degrees.append("Finished current animation")
        self.modes.append("rotate")
        self.future_heading = destination

    def turn_right(self, degrees):
        self.turn_clockwise(degrees)

    def right(self, degrees):
        self.turn_clockwise(degrees)

    def turn_counterclockwise(self, degrees):
        destination = self.future_heading + degrees
        frames_needed = 12 * self.speed
        if frames_needed == 0:
            frames_needed = 1
        degree_rot = destination - self.future_heading
        self.step_size = float(degree_rot)/float(frames_needed)
        for n in range(int(frames_needed)):
            self.animation_rotation_degrees.append(self.step_size+(self.step_size*n)+self.future_heading)
        self.animation_rotation_degrees[-1] = destination
        self.animation_rotation_degrees.append("Finished current animation")
        self.modes.append("rotate")
        self.future_heading = destination

    def turn_left(self, degrees):
        self.turn_counterclockwise(degrees)

    def left(self, degrees):
        self.turn_counterclockwise(degrees)

    def wait(self, seconds):
        self.modes.append("wait")
        self.wait_list.append(seconds*50)
        self.wait_list.append("Finished current animation")
        self.total_wait_time += seconds
        self.future_most_recent_wait_time = seconds

    def get_wait_time(self):
        return self.future_most_recent_wait_time

    def get_total_wait_time(self):
        return self.total_wait_time

    def say(self, text, seconds=-1, color="#000000", size=12, font="Helvetica"):
        # print text
        self.modes.append('say')
        self.say_plans.append([text, seconds*50, color, size, font])

    def ask(self, text):
        return input(text+'\n')

    def reset_animation(self):
        self.clear_queue()
        '''
        self.animation_rotation_degrees = []
        self.animation_x_coords = []
        self.animation_y_coords = []
        self.modes = []
        '''

    def pause(self):
        self.paused = True

    def stop(self):
        self.reset_animation()

    def reset(self):
        self.reset_animation()

    def play(self):
        self.paused = False

    # Physics

    def jump(self, newspeed):
        self.yspeed = newspeed

    def gravity_on(self):
        self.gravity_override = True
        self.gravity_true = True

    def gravity_off(self):
        self.gravity_override = True
        self.gravity_true = False

    def physics_on(self):
        self.physics_true = True
        self.gravity_on()

    def physics_off(self):
        self.physics_true = False
        self.gravity_off()

    def set_gravity_on(self):
        self.gravity_on()

    def set_gravity_off(self):
        self.gravity_off()

    def set_physics_on(self):
        self.physics_on()

    def set_physics_off(self):
        self.physics_off()

    def is_goal(self):
        self.goal = True

    def collision_goal_on(self):
        self.goal = True

    def collision_goal_off(self):
        self.goal = False

    def is_hazard(self):
        self.hazard = True

    def collision_hazard_on(self):
        self.hazard = True

    def collision_hazard_off(self):
        self.hazard = False

    def cannot_collide(self):
        self.collision = False

    def collision_on(self):
        self.collision = True

    def collision_off(self):
        self.collision = False

    def set_drag_on(self):
        self.drag = True

    def set_drag_off(self):
        self.drag = False

    # the speed in the following functions refers to animations, NOT physics

    def set_speed(self, newspeed):
        self.speed = newspeed
        self.animation_duration = 1000/newspeed

    def speed(self, newspeed):
        self.set_speed(newspeed)

    def get_speed(self):
        return self.speed

    # Setters
    def set_width(self, newsize):
        self.width = newsize
        self.update_image()
    def set_height(self, newsize):
        self.height = newsize
        self.update_image()
    # Old setters
    def set_velx(self, amount):
        self.set_x_speed(amount)
    def set_vely(self, amount):
        self.set_y_speed(amount)
    def set_x_speed(self, newspeed):
        self.xspeed = newspeed
    def set_y_speed(self, newspeed):
        self.yspeed = newspeed
    def set_y(self, newy):
        self.animation_y_coords.append(newy)
        self.animation_y_coords.append("Finished current animation")
        self.animation_x_coords.append(self.future_x)
        self.animation_x_coords.append("Finished current animation")
        self.modes.append("translate")
        self.future_y = newy
    def set_x(self, newx):
        self.animation_x_coords.append(newx)
        self.animation_x_coords.append("Finished current animation")
        self.animation_y_coords.append(self.future_y)
        self.animation_y_coords.append("Finished current animation")
        self.modes.append("translate")
        self.future_x = newx
    def set_position(self, to_x, to_y):
        self.go_to(to_x, to_y)
    def set_rotation(self, rot):
        self.animation_rotation_degrees.append(rot)
        self.future_heading = rot
        self.modes.append("rotate")
        self.animation_rotation_degrees.append("Finished current animation")
    def set_heading(self, rot):
        self.set_rotation(rot)
    def set_opacity(self, opacity):
        self.opacity = int(opacity * 255)
        self.update_image()
    def set_left(self, amount):
        self.set_x(self.width/2 + amount)
    def set_right(self, amount):
        self.set_x(-self.width/2 + amount)
    def set_top(self, amount):
        self.set_y(-self.height/2 + amount)
    def set_bottom(self, amount):
        self.set_y(self.height/2 + amount)

    # Old getters

    def velx(self):
        return self.xspeed
    def vely(self):
        return self.yspeed
    def y(self):
        return self.ycor
    def x(self):
        return self.xcor
    def rotation(self):
        return self.heading
    def direction(self):
        return self.heading

    # Getters

    def get_x_speed(self):
        return self.xspeed
    def get_y_speed(self):
        return self.yspeed
    def get_composite_speed(self):
        return math.sqrt(self.xspeed**2 + self.yspeed**2)
    def get_y(self):
        return self.future_y
    def get_x(self):
        return self.future_x
    def get_rotation(self):
        return self.future_heading
    def get_direction(self):
        return self.future_heading
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_left(self):
        return self.future_x-self.width/2
    def get_right(self):
        return self.future_x+self.width/2
    def get_top(self):
        return self.future_y+self.height/2
    def get_bottom(self):
        return self.future_y-self.height/2
    def get_sides(self):
        return 0
    def get_x_scale(self):
        pass
    def get_size(self):
        return self.future_size
    def get_scale(self):
        return self.future_size
    def get_y_scale(self):
        pass
    def get_type(self):
        # print self.type
        return self.type
    def get_text(self):
        pass
    def get_name(self):
        # print self.name
        return self.name
    def get_image_name(self):
        # print self.image_name
        return self.image_name

    def set_size(self, newsize):
        self.scale_plans.append(newsize)
        self.modes.append("scale")
        self.scale_plans.append("Finished current animatoin")
        self.future_size = newsize

    # flippers
    def flip_horizontal(self):
        self.future_x_flipped = not self.future_x_flipped
        if len(self.x_flip_plans) == 0:
            self.x_flip_plans.append(not self.x_flipped)
        else:
            self.x_flip_plans.append(not self.x_flip_plans[-1])
        self.modes.append("xflip")
    def flip_right_left(self):
        self.flip_horizontal()
    def flip_left_right(self):
        self.flip_horizontal()
    def flip_vertical(self):
        self.future_y_flipped = not self.future_y_flipped
        if len(self.y_flip_plans) == 0:
            self.y_flip_plans.append(not self.y_flipped)
        else:
            self.y_flip_plans.append(not self.y_flip_plans[-1])
        self.modes.append("yflip")
    def flip_up_down(self):
        self.flip_vertical()
    def flip_down_up(self):
        self.flip_vertical()
    def face_forward(self):
        self.x_flip_plans.append(False)
        self.modes.append("xflip")
    def face_backward(self):
        self.x_flip_plans.append(True)
        self.modes.append("xflip")
    def face_upside_down(self):
        self.y_flip_plans.append(True)
        self.modes.append("yflip")
    def face_rightside_up(self):
        self.y_flip_plans.append(False)
        self.modes.append("yflip")

    ##### EVENTS #####

    def event_left_key(self, function):
        def f(event):
            #  self.clear_queue()
            function()
        if "Left" not in list(self.key_functions.keys()):
            self.key_functions['Left'] = [f]
        else:
            self.key_functions['Left'].append(f)

    def event_right_key(self, function):
        def f(event):
            #  self.clear_queue()
            function()
        if "Right" not in list(self.key_functions.keys()):
            self.key_functions['Right'] = [f]
        else:
            self.key_functions['Right'].append(f)

    def event_up_key(self, function):
        def f(event):
            #  self.clear_queue()
            function()
        if "Up" not in list(self.key_functions.keys()):
            self.key_functions['Up'] = [f]
        else:
            self.key_functions['Up'].append(f)

    def event_down_key(self, function):
        def f(event):
            #  self.clear_queue()
            function()
        if "Down" not in list(self.key_functions.keys()):
            self.key_functions['Down'] = [f]
        else:
            self.key_functions['Down'].append(f)

    def event_space_key(self, function):
        def f(event):
            #  self.clear_queue()
            function()
        if "space" not in list(self.key_functions.keys()):
            self.key_functions['space'] = [f]
        else:
            self.key_functions['space'].append(f)

    def event_key(self, key, function):
        newkey = key
        if newkey.upper() == "DOWN":
            newkey = "Down"
        if newkey.upper() == "UP":
            newkey = "Up"
        if newkey.upper() == "LEFT":
            newkey = "Left"
        if newkey.upper() == "RIGHT":
            newkey = "Right"
        if newkey.upper() == "RETURN":
            newkey = "Return"
        if newkey.upper() == "ENTER":
            newkey = "Return"
        if newkey.upper() == "SPACE":
            newkey = "space"

        def f(event):
            #  self.clear_queue()
            if len(inspect.signature(function).parameters) == 0:
                function()
            elif len(inspect.signature(function).parameters) == 1:
                function(self)
        if newkey not in list(self.key_functions.keys()):
            self.key_functions[newkey] = [f]
        else:
            self.key_functions[newkey].append(f)

    def event_click(self, function):
        def click(event):
            hit = self.get_hitbox_edges()
            top = hit[0]
            right = hit[1]
            bottom = hit[2]
            left = hit[3]
            ex = event.x - Manager.width
            ey = Manager.height - event.y
            if left < ex < right and bottom < ey < top:
                #  self.clear_queue()
                function()
        id = self.canvas.bind("<Button-1>", click, add='+')
        self.event_bindings[id] = "<Button-1>"

    def event_forever(self, function):
        self.forever_function = function

    def event_collision(self, function):
        self.collision_function = function

    def event_collision_goal(self, function):
        self.collision_goal_function = function

    def event_collision_hazard(self, function):
        self.collision_hazard_function = function

    def event_delay(self, function, seconds):
        self.event_delay_timer = Timer(seconds, function, (self,))
        self.event_delay_timer.start()

    ##### END OF EVENTS #####

    def pen_down(self):
        self.pen_plans.append(True)
        self.modes.append("pen")

    def pen_up(self):
        self.pen_plans.append(False)
        self.modes.append("pen")

    def pen_toggle(self):
        if len(self.pen_plans) >= 1:
            self.pen_plans.append(not self.pen_plans[-1])
        else:
            self.pen_plans.append(not self.pen)
        self.modes.append("pen")

    def draw_hitbox(self):
        self.debug()

    def fill_on(self):
        self.fill_plans.append(True)
        self.modes.append("fill")

    def fill_off(self):
        self.fill_plans.append(False)
        self.modes.append("fill")

    def fill_toggle(self):
        if len(self.fill_plans) >= 1:
            self.fill_plans.append(not self.fill_plans[-1])
        else:
            self.fill_plans.append(not self.fill)
        self.modes.append("fill")

    def pen_clear(self):
        self.modes.append("pen_clear")

    def pen_width(self, newwidth):
        self.pen_size(newwidth)

    def pen_size(self, newsize):
        self.pen_size_plans.append(newsize)
        self.modes.append("pen_size")

    def _rgb_to_hex(self, r, g, b):
        color = None
        if g and b:
            color = "#{0:02x}{1:02x}{2:02x}".format(max(0, min(r, 255)),
                                                    max(0, min(g, 255)),
                                                    max(0, min(b, 255)))
        else:
            color = r
        return color

    def set_color(self, newcolor_or_r, g=None, b=None):
        self.color = self._rgb_to_hex(newcolor_or_r, g, b)
        self.pen_color_var = self.color

    def pen_color(self, newcolor):
        self.pen_color_plans.append(newcolor)
        self.modes.append("pen_color")
        self.fill_toggle()
        self.fill_toggle()

    def set_fill_color(self, newcolor):
        self.fill_color_plans.append(newcolor)
        self.modes.append("fill_color")
        self.fill_toggle()
        self.fill_toggle()

    def get_color(self):
        return self.color

    def debug(self):
        self.hitbox.draw()

    def dilate(self, amount):
        self.dilate_plans.append(amount)
        self.modes.append("dilate")
        self.goto(amount * self.future_x, amount * self.future_y)

    def rotate_about(self, degrees, x, y):
        theta = degrees*math.pi/180
        costhe = math.cos(theta)
        sinthe = math.sin(theta)
        x1 = costhe * (self.xcor-x) - sinthe * (self.ycor-y) + x
        y1 = sinthe * (self.xcor-x) + costhe * (self.ycor-y) + y
        self.set_heading(self.future_heading+degrees)
        self.go_to(x1, y1)

    def rotate_origin(self, degrees):
        self.rotate_about(degrees, 0, 0)

    def reflect_x(self, x):
        self.go_to(x - (self.future_x-x), self.future_y)
        self.flip_left_right()

    def reflect_y(self, y):
        self.go_to(self.future_x, y - (self.future_y-y))
        self.flip_up_down()

    def reflect_x_axis(self):
        self.reflect_y(0)

    def reflect_y_axis(self):
        self.reflect_x(0)

    def get_flip(self):
        return self.future_x_flipped != self.future_y_flipped

    def get_fill_on(self):
        return self.fill
    def get_fill_off(self):
        return not self.fill

    def get_pen_up(self):
        return not self.pen
    def get_pen_down(self):
        return self.pen

    def clean_up(self):
        for id in self.event_bindings:
            event_string = self.event_bindings[id]
            self.canvas.unbind(event_string, id)

class Sprite(SpriteClass):

    def __init__(self, image="", x=0, y=0, **kwargs):
        if not isinstance(image, str):
            y = x
            x = image
            image = ''
        if 'shape' in kwargs:
            super(Sprite, self).__init__(image, x, y, shape=kwargs['shape'])
        else:
            super(Sprite, self).__init__(image, x, y)
