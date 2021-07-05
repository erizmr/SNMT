import os
from a2c_ppo_acktr.arguments import get_args
from multitask.config_sim import ConfigSim
from RL_trainer import RLTrainer

if __name__ == "__main__":
    args = get_args()
    print('args', args)
    config_file = args.config_file
    config = ConfigSim.from_file(config_file)
    rl_trainer = RLTrainer(args, config=config)
    print(config)
    if args.train:
        rl_trainer.train(start_iter=0, max_iter=10000)
    if args.validate:
        rl_trainer.validate()
    if args.evaluate:
        eval_path = args.evaluate_path
        rl_trainer.evaluate(eval_path)