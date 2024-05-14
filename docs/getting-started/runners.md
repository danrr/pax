# Runners 

## Evo Runner

The Evo Runner optimizes the first agent using evolutionary learning. 

See [this experiment](https://github.com/akbir/pax/blob/9a01bae33dcb2f812977be388751393f570957e9/pax/conf/experiment/cg/mfos.yaml) for an example of how to configure it.

## Weight sharing Runner

A simple baseline for MARL experiments is having one agent assume multiple roles and share the weights between them (but not the memory).
In order for this approach to work the observation vector needs to include one entry that indicates the role of the agent (see [Terry et al.](https://arxiv.org/abs/2005.13625v7).

See [this experiment](https://github.com/akbir/pax/blob/9d3fa62e34279a338c07cffcbf208edc8a95e7ba/pax/conf/experiment/rice/weight_sharing.yaml) for an example of how to configure it.

## Evo Hardstop

The Evo Runner optimizes the first agent using evolutionary learning. 
This runner stops the learning of an opponent during training, corresponds to the hardstop challenge of Shaper.

See [this experiment](https://github.com/akbir/pax/blob/9a01bae33dcb2f812977be388751393f570957e9/pax/conf/experiment/ipd/shaper_att_v_tabular.yaml) for an example of how to configure it.

## Evo Scanned

The Evo Runner optimizes the first agent using evolutionary learning. 
Here we also scan over the evolutionary steps, which makes compilation longer, training shorter and logging stats is not possible.

See [this experiment](https://github.com/akbir/pax/blob/9a01bae33dcb2f812977be388751393f570957e9/pax/conf/experiment/ipd/shaper_att_v_tabular.yaml) for an example of how to configure it.


