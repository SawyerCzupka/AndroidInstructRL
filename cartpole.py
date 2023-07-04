import gymnasium as gym
from stable_baselines3 import DQN, PPO
from stable_baselines3.common.evaluation import evaluate_policy

# Create environment
env = gym.make("CartPole-v1", render_mode='rgb_array')


def train():
    # Instantiate Agent
    model = PPO('MlpPolicy', env, verbose=1)

    model.learn(total_timesteps=int(2e5), progress_bar=True)

    model.save('ppo_cartpole')


def evaluate():
    # Load the trained agent
    model = PPO.load("ppo_cartpole", env=env)

    print(model)

    # Evaluate the agent
    mean_reward, std_reward = evaluate_policy(model, model.get_env(), n_eval_episodes=10)

    # Enjoy trained agent
    vec_env = model.get_env()
    obs = vec_env.reset()
    for i in range(1000):
        action, _states = model.predict(obs, deterministic=True)
        obs, rewards, dones, info = vec_env.step(action)
        vec_env.render('human')


if __name__ == "__main__":
    evaluate()
