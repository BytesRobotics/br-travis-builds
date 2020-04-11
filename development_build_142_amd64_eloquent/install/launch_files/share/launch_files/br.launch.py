import launch
import launch.actions
import launch.substitutions
import launch_ros.actions
from launch_ros.actions import Node


def generate_launch_description():
    return launch.LaunchDescription([
        Node(
            package='ros1_bridge',
            node_executable='dynamic_bridge',
            node_namespace='',
            output='screen',
            arguments=[]
        ),
    ])