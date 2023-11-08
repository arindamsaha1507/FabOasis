# -*- coding: utf-8 -*-
#
# This source file is part of the FabSim software toolkit, which is distributed under the BSD 3-Clause license.
# Please refer to LICENSE for detailed information regarding the licensing.
#
# This file contains FabSim definitions specific to FabDummy.

from fabsim.base.fab import (
    add_local_paths,
    env,
    execute,
    find_config_file_path,
    job,
    load_plugin_env_vars,
    put_configs,
    run_ensemble,
    task,
    update_environment,
    with_config,
)

# Add local script, blackbox and template path.
add_local_paths("FabOasis")


@task
@load_plugin_env_vars("FabOasis")
def eve(config, **args):
    """Submit a job to the remote queue.
    The job results will be stored with a name pattern as defined in the environment,
    e.g. cylinder-abcd1234-legion-256
    config : config directory to use to define input files, e.g. config=cylinder
    Keyword arguments:
            cores : number of compute cores to request
            images : number of images to take
            steering : steering session i.d.
            wall_time : wall-time job limit
            memory : memory per node
    """

    print(env)

    # update_environment(args, {"eco_script": eco_script})

    set_eco_args_list(args)

    with_config(config)
    execute(put_configs, config)
    print(args)
    job(dict(script="eve", wall_time="0:15:0", memory="2G"), args)

