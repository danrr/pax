import os

import pytest
from hydra import compose, initialize_config_dir

from pax.experiment import main

shared_overrides = [
    "++wandb.mode=disabled",
    "++num_iters=1",
    "++popsize=2",
    "++num_outer_steps=1",
    "++num_inner_steps=8",  # required for ppo minibatch size
    "++num_devices=1",
    "++num_envs=1",
    "++num_epochs=1",
]


@pytest.fixture(scope="module", autouse=True)
def setup_hydra():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../../pax/conf"
    )
    initialize_config_dir(config_dir=path)


def _test_runner(overrides):
    cfg = compose(
        config_name="config.yaml", overrides=shared_overrides + overrides
    )
    main(cfg)

def test_runner_evo_runs():
    _test_runner(["+experiment/cg=mfos"])

def test_runner_marl_runs():
    _test_runner(["+experiment/cg=tabular"])



def test_runner_evo_hardstop():
    _test_runner(["+experiment/ipd=shaper_att_v_tabular", "++runner=evo_hardstop"])

def test_runner_evo_scanned():
    _test_runner(["+experiment/ipd=shaper_att_v_tabular", "++runner=evo_scanned"])
