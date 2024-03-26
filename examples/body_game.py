import ctypes

import pygame

# from pykinect.wincom import *
from pykinect import runtime, wincom

# colors for drawing different bodies
SKELETON_COLORS = [
    pygame.color.THECOLORS["red"],
    pygame.color.THECOLORS["blue"],
    pygame.color.THECOLORS["green"],
    pygame.color.THECOLORS["orange"],
    pygame.color.THECOLORS["purple"],
    pygame.color.THECOLORS["yellow"],
    pygame.color.THECOLORS["violet"],
]


class BodyGameRuntime(object):
    def __init__(self):
        pygame.init()

        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

        # Set the width and height of the screen [width, height]
        self._infoObject = pygame.display.Info()
        self._screen = pygame.display.set_mode(
            (self._infoObject.current_w >> 1, self._infoObject.current_h >> 1),
            pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE,
            32,
        )

        pygame.display.set_caption("Kinect for Windows v2 Body Game")

        # Loop until the user clicks the close button.
        self._done = False

        # Used to manage how fast the screen updates
        self._clock = pygame.time.Clock()

        # Kinect runtime object, we want only color and body frames
        self._kinect = runtime.PyKinectRuntime(
            wincom.FrameSourceTypes_Color | wincom.FrameSourceTypes_Body
        )

        # back buffer surface for getting Kinect color frames, 32bit color, width and height equal to the Kinect color frame size
        self._frame_surface = pygame.Surface(
            (self._kinect.color_frame_desc.Width, self._kinect.color_frame_desc.Height),
            0,
            32,
        )

        # here we will store skeleton data
        self._bodies = None

    def draw_body_bone(self, joints, jointPoints, color, joint0, joint1):
        joint0State = joints[joint0].TrackingState
        joint1State = joints[joint1].TrackingState
        # both joints are not tracked
        if (joint0State == wincom.TrackingState_NotTracked) or (
            joint1State == wincom.TrackingState_NotTracked
        ):
            return

        # both joints are not *really* tracked
        if (joint0State == wincom.TrackingState_Inferred) and (
            joint1State == wincom.TrackingState_Inferred
        ):
            return

        # ok, at least one is good
        start = (jointPoints[joint0].x, jointPoints[joint0].y)
        end = (jointPoints[joint1].x, jointPoints[joint1].y)

        try:
            pygame.draw.line(self._frame_surface, color, start, end, 8)
        except:  # need to catch it due to possible invalid positions (with inf)
            pass

    def draw_body(self, joints, jointPoints, color):
        # Torso
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_Head,
            wincom.JointType_Neck,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_Neck,
            wincom.JointType_SpineShoulder,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_SpineShoulder,
            wincom.JointType_SpineMid,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_SpineMid,
            wincom.JointType_SpineBase,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_SpineShoulder,
            wincom.JointType_ShoulderRight,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_SpineShoulder,
            wincom.JointType_ShoulderLeft,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_SpineBase,
            wincom.JointType_HipRight,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_SpineBase,
            wincom.JointType_HipLeft,
        )
        # Right Arm
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_ShoulderRight,
            wincom.JointType_ElbowRight,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_ElbowRight,
            wincom.JointType_WristRight,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_WristRight,
            wincom.JointType_HandRight,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_HandRight,
            wincom.JointType_HandTipRight,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_WristRight,
            wincom.JointType_ThumbRight,
        )
        # Left Arm
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_ShoulderLeft,
            wincom.JointType_ElbowLeft,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_ElbowLeft,
            wincom.JointType_WristLeft,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_WristLeft,
            wincom.JointType_HandLeft,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_HandLeft,
            wincom.JointType_HandTipLeft,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_WristLeft,
            wincom.JointType_ThumbLeft,
        )
        # Right Leg
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_HipRight,
            wincom.JointType_KneeRight,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_KneeRight,
            wincom.JointType_AnkleRight,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_AnkleRight,
            wincom.JointType_FootRight,
        )
        # Left Leg
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_HipLeft,
            wincom.JointType_KneeLeft,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_KneeLeft,
            wincom.JointType_AnkleLeft,
        )
        self.draw_body_bone(
            joints,
            jointPoints,
            color,
            wincom.JointType_AnkleLeft,
            wincom.JointType_FootLeft,
        )

    def draw_color_frame(self, frame, target_surface):
        target_surface.lock()
        address = self._kinect.surface_as_array(target_surface.get_buffer())
        ctypes.memmove(address, frame.ctypes.data, frame.size)
        del address
        target_surface.unlock()

    def run(self):
        # -------- Main Program Loop -----------
        while not self._done:
            # --- Main event loop
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self._done = True  # Flag that we are done so we exit this loop

                elif event.type == pygame.VIDEORESIZE:  # window resized
                    self._screen = pygame.display.set_mode(
                        event.dict["size"],
                        pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE,
                        32,
                    )

            # --- Game logic should go here

            # --- Getting frames and drawing
            # --- Woohoo! We've got a color frame! Let's fill out back buffer surface with frame's data
            if self._kinect.has_new_color_frame():
                frame = self._kinect.get_last_color_frame()
                self.draw_color_frame(frame, self._frame_surface)
                frame = None

            # --- Cool! We have a body frame, so can get skeletons
            if self._kinect.has_new_body_frame():
                self._bodies = self._kinect.get_last_body_frame()

            # --- draw skeletons to _frame_surface
            if self._bodies is not None:
                for i in range(0, self._kinect.max_body_count):
                    body = self._bodies.bodies[i]
                    if not body.is_tracked:
                        continue

                    joints = body.joints
                    # convert joint coordinates to color space
                    joint_points = self._kinect.body_joints_to_color_space(joints)
                    self.draw_body(joints, joint_points, SKELETON_COLORS[i])

            # --- copy back buffer surface pixels to the screen, resize it if needed and keep aspect ratio
            # --- (screen size may be different from Kinect's color frame size)
            h_to_w = (
                float(self._frame_surface.get_height())
                / self._frame_surface.get_width()
            )
            target_height = int(h_to_w * self._screen.get_width())
            surface_to_draw = pygame.transform.scale(
                self._frame_surface, (self._screen.get_width(), target_height)
            )
            self._screen.blit(surface_to_draw, (0, 0))
            surface_to_draw = None
            pygame.display.update()

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            self._clock.tick(60)

        # Close our Kinect sensor, close the window and quit.
        self._kinect.close()
        pygame.quit()


__main__ = "Kinect v2 Body Game"
game = BodyGameRuntime()
game.run()
