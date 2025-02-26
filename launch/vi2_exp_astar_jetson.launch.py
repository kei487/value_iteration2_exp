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
    planner_config = os.path.join(
      get_package_share_directory('value_iteration2_exp'),
      'config',
      'vi2_planner_params.yaml'
    )
    map_file = os.path.join(
        get_package_share_directory('value_iteration2_exp'),
        'map/tsudanuma/navigation',
        #'cit_19th.yaml',
        'map_tsudanuma.yaml',
    )
    vi2_params_file = os.path.join(
        get_package_share_directory('value_iteration2'),
        'config',
        'params.yaml',
    )
#    rviz2_config_file = os.path.join(
#        get_package_share_directory('value_iteration2_exp'),
#        'config',
#        'config.rviz',
#    )
    lifecycle_nodes = ['map_server_nav']
    use_sim_time = 'false'
#    exec_emcl2 = ExecuteProcess(
#        cmd=[ 'ros2', 'launch', 'emcl2', 'emcl2.launch.py',
#              f'params_file:={emcl2_params_file}',
#              f'map:={map_file}',
#              f'use_sim_time:={use_sim_time}' ],
#        output='screen',
#    )
    map_server = Node(
        package='nav2_map_server',
        executable='map_server',
        name='map_server_nav',
        parameters=[{'yaml_filename': map_file}],
        output='screen',
    )
    vi2_node = Node(
        package='value_iteration2',
        namespace='value_iteration2',
        executable='vi_node',
        name='vi2_node',
        parameters=[ vi2_params_file ],
        output='screen',
    )
#    rviz2 = Node(
#        package='rviz2',
#        executable='rviz2',
#        name='vi2_exp_rviz2',
#        arguments=[ '-d', rviz2_config_file ],
#        output='screen',
#    )
    planner_node = Node(
        package='value_iteration2',
        namespace='value_iteraion2',
        executable='planner',
        #output='screen'
        parameters=[planner_config],
#       {
#            'use_dijkstra': False,
#            'publish_searched_map': True,
#            'update_path_weight': 0.05,
#            'smooth_path_weight': 0.8,
#            'iteration_delta_threshold': 1.e-6,
#        }
#        extra_arguments=[{'use_intra_process_comms': False}],
    )
    lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_localization',
        output='screen',
        parameters=[{'autostart': True},
                    {'node_names': lifecycle_nodes}]
    )


    ld = LaunchDescription()
#    ld.add_action(exec_emcl2)
    ld.add_action(map_server)
    ld.add_action(vi2_node)
#    ld.add_action(rviz2)
    ld.add_action(planner_node)
    ld.add_action(lifecycle_manager)

    return ld
