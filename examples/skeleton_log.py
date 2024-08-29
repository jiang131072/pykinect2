import csv

import pygame

from pykinect import api, runtime
from pykinect.api import *

# 初始化Pygame
pygame.init()

# 设置窗口尺寸
width, height = 960, 540
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyKinect2 Body Tracking")

# 创建Kinect实例
kinect = runtime.PyKinectRuntime(api.FrameSourceTypes_Body)

# 创建CSV文件
with open("tmp/skeleton_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    joint_ids = [joint_id for joint_id in range(0, api.JointType_Count)]
    header = (
        ["Frame"]
        + [f"Joint {joint_id+1} X" for joint_id in joint_ids]
        + [f"Joint {joint_id+1} Y" for joint_id in joint_ids]
        + [f"Joint {joint_id+1} Z" for joint_id in joint_ids]
    )
    writer.writerow(header)  # 写入表头

    # 游戏主循环
    running = True
    frame_count = 0
    frame_rate = 30  # 帧率设定为30帧/秒
    interval = 1.0 / frame_rate  # 计算每帧的时间间隔
    last_time = pygame.time.get_ticks() / 1000.0  # 上一帧的时间戳
    tracked_body_index = None  # 跟踪的人体索引

    while running:
        # 处理事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 获取骨架数据
        if kinect.has_new_body_frame():
            bodies = kinect.get_last_body_frame().bodies

            if bodies is not None:
                # 寻找正在跟踪的人体
                for i in range(0, kinect.max_body_count):
                    body = bodies[i]
                    if body.is_tracked:
                        tracked_body_index = i
                        break

        # 跟踪到人体后才进行数据记录
        if tracked_body_index is not None:
            # 计算当前时间戳
            current_time = pygame.time.get_ticks() / 1000.0

            # 根据时间间隔记录数据
            if current_time - last_time >= interval:
                body = bodies[tracked_body_index]
                frame_data = []

                # 存储关节坐标数据
                for joint_id in range(0, api.JointType_Count):
                    joint = body.joints[joint_id]
                    frame_data.extend(
                        [joint.Position.x, joint.Position.y, joint.Position.z]
                    )

                # 调整关节坐标数据的排列顺序
                rearranged_data = []
                for joint_id in range(1, api.JointType_Count + 1):
                    rearranged_data.extend(
                        frame_data[(joint_id - 1) * 3 : joint_id * 3]
                    )

                # 写入CSV文件
                writer.writerow([frame_count + 1] + rearranged_data)

                # 打印关节数据
                print(f"Frame: {frame_count+1}, Joint Positions: {rearranged_data}")

                # 更新上一帧的时间戳
                last_time = current_time

                # 帧数加1
                frame_count += 1

        # 清空屏幕
        screen.fill((0, 0, 0))

        # 绘制骨架连线图
        if tracked_body_index is not None:
            joints = bodies[tracked_body_index].joints

            # 定义骨架连线关系
            bone_connections = [
                (JointType_Head, JointType_Neck),
                (JointType_Neck, JointType_SpineShoulder),
                (JointType_SpineShoulder, JointType_SpineMid),
                (JointType_SpineMid, JointType_SpineBase),
                (JointType_SpineShoulder, JointType_ShoulderRight),
                (JointType_SpineShoulder, JointType_ShoulderLeft),
                (JointType_ShoulderRight, JointType_ElbowRight),
                (JointType_ElbowRight, JointType_WristRight),
                (JointType_WristRight, JointType_HandRight),
                (JointType_ShoulderLeft, JointType_ElbowLeft),
                (JointType_ElbowLeft, JointType_WristLeft),
                (JointType_WristLeft, JointType_HandLeft),
                (JointType_SpineBase, JointType_HipRight),
                (JointType_SpineBase, JointType_HipLeft),
                (JointType_HipRight, JointType_KneeRight),
                (JointType_KneeRight, JointType_AnkleRight),
                (JointType_AnkleRight, JointType_FootRight),
                (JointType_HipLeft, JointType_KneeLeft),
                (JointType_KneeLeft, JointType_AnkleLeft),
                (JointType_AnkleLeft, JointType_FootLeft),
            ]

            # 绘制骨架连线
            for connection in bone_connections:
                joint1 = joints[connection[0]]
                joint2 = joints[connection[1]]
                if (
                    joint1.TrackingState == TrackingState_Tracked
                    and joint2.TrackingState == TrackingState_Tracked
                ):
                    joint1_pos = kinect.body_joint_to_color_space(joint1)
                    joint2_pos = kinect.body_joint_to_color_space(joint2)
                    pygame.draw.line(
                        screen,
                        (255, 0, 0),
                        (joint1_pos.x, joint1_pos.y),
                        (joint2_pos.x, joint2_pos.y),
                        5,
                    )

        # 更新屏幕显示
        pygame.display.flip()

    # 退出Pygame
    pygame.quit()

# 释放Kinect资源
kinect.close()
