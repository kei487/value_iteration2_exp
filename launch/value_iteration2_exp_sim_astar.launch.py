import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():

    emcl2_params_file = os.path.join(
        get_package_share_directory('emcl2'),
        'config',
        'emcl2.param.yaml',
    )
    map_file_nav = os.path.join(
        get_package_share_directory('value_iteration2_exp'),
        'map/tsudanuma/navigation',
        'map_tsudanuma.yaml',
    )
    map_file_loc = os.path.join(
        get_package_share_directory('value_iteration2_exp'),
        'map/yoshigoe',
        'map_tsudanuma_campus.yaml',
    )
    vi2_params_file = os.path.join(
        get_package_share_directory('value_iteration2'),
        'config',
        'params.yaml',
    )
    rviz2_config_file = os.path.join(
        get_package_share_directory('value_iteration2_exp'),
        'config',
        'config.rviz',
    )
    use_sim_time = 'true'

    exec_gazebo = ExecuteProcess(
        cmd=[ 'ros2', 'launch', 'raspicat_gazebo',
              'raspicat_with_tsudanuma_campus.launch.py' ],#, 'rviz:=false' ],
        output='screen',
    )
    exec_emcl2 = ExecuteProcess(
        cmd=[ 'ros2', 'launch', 'emcl2', 'emcl2.launch.py',
              f'params_file:={emcl2_params_file}',
              f'map:={map_file_loc}',
              f'use_sim_time:={use_sim_time}' ],
        output='screen',
    )
    vi2_node = Node(
        package='value_iteration2',
        namespace='value_iteration2',
        executable='vi_node',
        name='vi_node',
        parameters=[ vi2_params_file ],
        #output='screen',
    )
    rviz2 = Node(
        package='rviz2',
        executable='rviz2',
        name='vi2_exp_rviz2',
        arguments=[ '-d', rviz2_config_file ],
        output='screen',
    )
    planner_node = Node(
        package='value_iteration2',
        namespace='ike_nav',
        executable='planner',
        #output='screen'
        parameters=[{
            'use_dijkstra': False,
            'publish_searched_map': True,
            'update_path_weight': 0.05,
            'smooth_path_weight': 0.8,
            'iteration_delta_threshold': 1.e-6,
        }],
        #extra_arguments=[{'use_intra_process_comms': False}],
    )

    ld = LaunchDescription()
    ld.add_action(exec_gazebo)
    ld.add_action(exec_emcl2)
    ld.add_action(vi2_node)
    ld.add_action(rviz2)
    ld.add_action(planner_node)

    return ld