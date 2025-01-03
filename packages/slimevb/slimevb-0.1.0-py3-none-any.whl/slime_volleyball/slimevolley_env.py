"""
Port of Neural Slime Volleyball to Python Gym Environment

David Ha (2020)

Original version:

https://otoro.net/slimevolley
https://blog.otoro.net/2015/03/28/neural-slime-volleyball/
https://github.com/hardmaru/neuralslimevolley

No dependencies apart from Numpy and Gym
"""

import typing

import gymnasium as gym
from gymnasium import spaces
from gymnasium.envs.registration import register
import numpy as np
import cv2  # installed with gym anyways

from slime_volleyball.core import constants
from slime_volleyball.core import game
from slime_volleyball.baseline_policy import BaselinePolicy
from slime_volleyball.core import utils


try:
    from slime_volleyball import rendering
except ImportError as e:
    print(
        f"Unable to import rendering. This means you won't be able to render the game: {e}"
    )

np.set_printoptions(threshold=20, precision=3, suppress=True, linewidth=200)


class Actions:
    Noop = 0
    Left = 1
    UpLeft = 2
    Up = 3
    UpRight = 4
    Right = 5


class SlimeVolleyEnv(gym.Env):
    """
    Gym wrapper for Slime Volley game.

    By default, the agent you are training controls the right agent
    on the right. The agent on the left is controlled by the baseline
    RNN policy.

    Game ends when an agent loses 5 matches (or at t=3000 timesteps).

    Note: Optional mode for MARL experiments, like self-play which
    deviates from Gym env. Can be enabled via supplying optional action
    to override the default baseline agent's policy:

    obs1, reward, done, info = env.step(action1, action2)

    the next obs for the right agent is returned in the optional
    fourth item from the step() method.

    reward is in the perspective of the right agent so the reward
    for the left agent is the negative of this number.
    """

    metadata = {
        "render.modes": ["human", "rgb_array", "state"],
        "video.frames_per_second": 50,
    }

    action_table = [
        [0, 0, 0],  # NOOP
        [1, 0, 0],  # LEFT (forward)
        [1, 0, 1],  # UPLEFT (forward jump)
        [0, 0, 1],  # UP (jump)
        [0, 1, 1],  # UPRIGHT (backward jump)
        [0, 1, 0],  # RIGHT (backward)
    ]

    default_config = {
        "from_pixels": False,
        "survival_reward": False,
        "max_steps": 3000,
        # if true, LHS actions are swapped to be intuitive for humans, otherwise directions are swapped
        "human_inputs": False,
    }

    def __init__(
        self,
        config: dict[str, typing.Any] | None = None,
        render_mode: str | None = None,
    ):
        """
        Reward modes:

        net score = right agent wins minus left agent wins

        0: returns net score (basic reward)
        1: returns 0.01 x number of timesteps (max 3000) (survival reward)
        2: sum of basic reward and survival reward

        0 is suitable for evaluation, while 1 and 2 may be good for training

        Setting multiagent to True puts in info (4th thing returned in stop)
        the otherObs, the observation for the other agent. See multiagent.py

        Setting self.from_pixels to True makes the observation with multiples
        of 84, since usual atari wrappers downsample to 84x84
        """
        if config is None:
            config = self.default_config

        self._agent_ids = set(["agent_left", "agent_right"])
        self.t = 0
        self.max_steps = config.get("max_steps", 3000)
        self.from_pixels = config.get(
            "from_pixels", self.default_config["from_pixels"]
        )
        self.survival_reward = config.get(
            "survival_reward", self.default_config["survival_reward"]
        )
        self.human_inputs = config.get(
            "human_inputs", self.default_config["human_inputs"]
        )

        if self.from_pixels:
            constants.setPixelObsMode()
            observation_space = spaces.Box(
                low=0,
                high=255,
                shape=(constants.PIXEL_HEIGHT, constants.PIXEL_WIDTH, 3),
                dtype=np.uint8,
            )
        else:
            high = np.array([np.finfo(np.float32).max] * 12)
            observation_space = spaces.Dict(
                {"obs": spaces.Box(-high, high, shape=(12,))}
            )

        self.action_space = spaces.Dict(
            {
                agent_id: spaces.Discrete(len(self.action_table))
                for agent_id in self._agent_ids
            }
        )
        self.observation_space = spaces.Dict(
            {agent_id: observation_space for agent_id in self._agent_ids}
        )

        self.canvas = None
        self.previous_rgbarray = None

        self.game = game.SlimeVolleyGame(self.np_random)
        self.ale = (
            self.game.agent_right
        )  # for compatibility for some models that need the self.ale.lives() function

        self.policy = BaselinePolicy()  # the “bad guy”

        self.viewer = None

        # another avenue to override the built-in AI's action, going past many env wraps:
        self.otherAction = None

        self.render_mode = render_mode

        super(SlimeVolleyEnv, self).__init__()

    def seed(self, seed=None):
        self.ale = (
            self.game.agent_right
        )  # for compatibility for some models that need the self.ale.lives() function

    def get_obs(self):
        if self.from_pixels:
            obs = self.render(mode="state")
            self.canvas = obs
            return {
                "agent_left": cv2.flip(obs, 1),
                "agent_right": obs,
            }  # always observe from the same angle

        return {
            "agent_left": {"obs": self.game.agent_left.get_observation()},
            "agent_right": {"obs": self.game.agent_right.get_observation()},
        }

    def discrete_to_box(self, n):
        # convert discrete action n into the actual triplet action
        if n is None:
            return n
        if isinstance(
            n, (list, tuple, np.ndarray)
        ):  # original input for some reason, just leave it:
            if len(n) == 3:
                return n
        assert (int(n) == n) and (n >= 0) and (n < 6)
        return self.action_table[n]

    @staticmethod
    def invert_action(action: list) -> list:
        left, right, up = action
        return [right, left, up]

    def step(self, actions):
        """
        note: although the action space is multi-binary, float vectors
        are fine (refer to setAction() to see how they get interpreted)
        """
        self.t += 1

        # If it's being treated as a single agent env, right agent is being
        # controlled and self.policy will control the left.
        if isinstance(actions, int):
            actions = {"agent_right": actions}

        left_agent_action = self.discrete_to_box(actions.get("agent_left"))
        right_agent_action = self.discrete_to_box(actions.get("agent_right"))

        if left_agent_action is None:  # override baseline policy
            obs = self.game.agent_left.get_observation()
            left_agent_action = self.policy.predict(obs)

        if self.human_inputs:
            left_agent_action = self.invert_action(left_agent_action)

        self.game.agent_left.set_action(left_agent_action)
        self.game.agent_right.set_action(right_agent_action)

        reward_right = self.game.step()
        survival_reward = 0.01 if self.survival_reward else 0.0

        # include survival bonus
        rewards = {
            "agent_left": -reward_right + survival_reward,
            "agent_right": reward_right + survival_reward,
        }

        obs = self.get_obs()

        terminateds, truncateds = self.get_terminateds_truncateds()

        return obs, rewards, terminateds, truncateds, {}

    def get_terminateds_truncateds(
        self,
    ) -> tuple[dict[str, bool], dict[str, bool]]:
        terminateds = {a_id: False for a_id in self._agent_ids}
        truncateds = {a_id: False for a_id in self._agent_ids}

        if self.t >= self.max_steps:
            truncateds = {a_id: True for a_id in self._agent_ids}
            truncateds["__all__"] = True
        else:
            truncateds["__all__"] = False

        if self.game.agent_left.life <= 0 or self.game.agent_right.life <= 0:
            terminateds = {a_id: True for a_id in self._agent_ids}
            terminateds["__all__"] = True
        else:
            terminateds["__all__"] = False

        return terminateds, truncateds

    def init_game_state(self):
        self.t = 0
        self.game.reset()

    def reset(
        self,
        seed: int | None = None,
        options: dict[str, typing.Any] | None = None,
    ) -> tuple[dict[str, np.array], dict[str, typing.Any]]:
        self.init_game_state()
        return self.get_obs(), {}

    def checkViewer(self):
        # for opengl viewer
        if self.viewer is None:
            from slime_volleyball import rendering

            self.viewer = rendering.SimpleImageViewer(
                # maxwidth=2160
            )  # macbook pro resolution

    def render(self):
        mode = self.render_mode
        if constants.PIXEL_MODE:
            if self.canvas is not None:  # already rendered
                rgb_array = self.canvas
                self.canvas = None
                if mode == "rgb_array" or mode == "human":
                    self.checkViewer()
                    larger_canvas = utils.upsize_image(rgb_array)
                    # self.viewer.imshow(larger_canvas)  # TODO: re-enable to play
                    if mode == "rgb_array":
                        return larger_canvas
                    else:
                        return

            self.canvas = self.game.display(self.canvas)
            # scale down to original res (looks better than rendering directly to lower res)
            self.canvas = utils.downsize_image(self.canvas)

            if mode == "state":
                return np.copy(self.canvas)

            # upsampling w/ nearest interp method gives a retro "pixel" effect look
            larger_canvas = utils.upsize_image(self.canvas)
            self.checkViewer()
            self.viewer.imshow(larger_canvas)
            if mode == "rgb_array":
                return larger_canvas

        else:  # pyglet renderer
            if self.viewer is None:
                self.viewer = rendering.Viewer(
                    constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT
                )

            self.game.display(self.viewer)
            return self.viewer.render(return_rgb_array=mode == "rgb_array")

    def close(self):
        if self.viewer:
            self.viewer.close()


class SlimeVolleyPixelEnv(SlimeVolleyEnv):
    from_pixels = True


register(
    id="SlimeVolley-v0", entry_point="slimevolleygym.slimevolley:SlimeVolleyEnv"
)
register(
    id="SlimeVolleyPixel-v0",
    entry_point="slimevolleygym.slimevolley:SlimeVolleyPixelEnv",
)
