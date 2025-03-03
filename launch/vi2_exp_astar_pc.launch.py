import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():

#    emcl2_params_file = os.path.join(
#        get_package_share_directory('emcl2'),
#        'config',
#        'emcl2.param.yaml',
#    )
    map_file = os.path.join(
        get_package_share_directory('value_iteration2_exp'),
        'map',
#        'cit_19th.yaml',
        'map_tsudanuma.yaml',
    )
#    vi2_params_file = os.path.join(
#        get_package_share_directory('value_iteration2'),
#        'config',
#        'params.yaml',
#    )
    rviz2_config_file = os.path.join(
        get_package_share_directory('value_iteration2_exp'),
        'config',
        'config.rviz',
    )
    use_sim_time = 'false'

    exec_emcl2 = ExecuteProcess(
        cmd=[ 'ros2', 'launch', 'emcl2', 'emcl2.launch.py',
              f'params_file:={emcl2_params_file}',
              f'map:={map_file}',
              f'use_sim_time:={use_sim_time}' ],
        output='screen',
    )
#    vi2_node = Node(
#        package='value_iteration2',
#        namespace='value_iteration2',
#        executable='vi_node',
#        name='vi2_node',
#        parameters=[ vi2_params_file ],
#        output='screen',
#    )
    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        name='vi2_exp_rviz2',
        arguments=[ '-d', rviz2_config_file ],
        output='screen',
    )

    ld = LaunchDescription()
    ld.add_action(exec_emcl2)
#    ld.add_action(vi2_node)
    ld.add_action(rviz2)

    return ld
