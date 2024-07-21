# value_iteration2_exp

## How to use the simulation
```
ros2 launch value_iteration2_exp value_iteration2_exp.launch.py
```
```
ros2 service call /motor_power std_srvs/SetBool '{data: true}'
```

## Licenses Used

The launch files in this package start nodes that are licensed under the following terms:

+ [raspicat_sim](https://github.com/rt-net/raspicat_sim.git) licensed under the [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) license
+ [emcl2_ros2](https://github.com/CIT-Autonomous-Robot-Lab/emcl2_ros2.git) licensed under the [LGPL-3.0](https://www.gnu.org/licenses/lgpl-3.0.html) license
+ [value_iteration2](https://github.com/ryuichiueda/value_iteration2.git) licensed under the [BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause) license

For more details on the specific licenses, please refer to the respective repositories or documentation of these nodes.
