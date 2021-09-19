from random import random, choice, randint

import ba
from bastd.actor.bomb import Bomb, Blast
from bastd.actor.playerspaz import PlayerSpaz
from bastd.actor.spazbot import SpazBotSet, BrawlerBotLite
from bastd.actor.powerupbox import PowerupBoxFactory, PowerupBox

from tools.objects import CompanionCube
from core.register import register_powerups


class Test:
    DIST = {
        "speed": {"frequency": 1, "texture": "powerupSpeed", "bomb": None},
        "jetpack": {"frequency": 2, "texture": "buttonJump", "bomb": None},
        "companion_cube": {"frequency": 1, "texture": "landMineLit", "bomb": None},
        "lucky_block": {"frequency": 2, "texture": "achievementEmpty", "bomb": None},
    }

    def speed(self, msg):
        powerup_expiration_time = 10_000
        tex = ba.gettexture("powerupSpeed")
        self._flash_billboard(tex)
        if self.powerups_expire:
            self.node.mini_billboard_1_texture = tex
            t = ba.time(timeformat=ba.TimeFormat.MILLISECONDS)
            self.node.mini_billboard_1_start_time = t
            self.node.mini_billboard_1_end_time = t + powerup_expiration_time

            def _speed_wear_off_flash() -> None:
                if self.node:
                    self.node.billboard_texture = tex
                    self.node.billboard_opacity = 1.0
                    self.node.billboard_cross_out = True

            def _speed_wear_off() -> None:
                if self.node:
                    ba.playsound(
                        PowerupBoxFactory.get().powerdown_sound,
                        position=self.node.position,
                    )
                    self.node.billboard_opacity = 0.0
                    self.node.hockey = False

            self._jetpack_wear_off_flash_timer = ba.Timer(
                powerup_expiration_time - 2000,
                _speed_wear_off_flash,
                timeformat=ba.TimeFormat.MILLISECONDS,
            )
            self._jetpack_wear_off_timer = ba.Timer(
                powerup_expiration_time,
                _speed_wear_off,
                timeformat=ba.TimeFormat.MILLISECONDS,
            )

        if self.node.hockey:
            return

        self.node.hockey = True

    def jetpack(self, msg) -> None:
        powerup_expiration_time = 10_000

        tex = ba.gettexture("buttonJump")

        self._flash_billboard(tex)
        if self.powerups_expire:
            self.node.mini_billboard_2_texture = tex
            t = ba.time(timeformat=ba.TimeFormat.MILLISECONDS)
            self.node.mini_billboard_2_start_time = t
            self.node.mini_billboard_2_end_time = t + powerup_expiration_time

            def _jetpack_wear_off_flash() -> None:
                if self.node:
                    self.node.billboard_texture = tex
                    self.node.billboard_opacity = 1.0
                    self.node.billboard_cross_out = True

            def _jetpack_wear_off() -> None:
                if self.node:
                    ba.playsound(
                        PowerupBoxFactory.get().powerdown_sound,
                        position=self.node.position,
                    )
                    self.node.billboard_opacity = 0.0
                    self.node.getdelegate(PlayerSpaz).connect_controls_to_player()

            self._jetpack_wear_off_flash_timer = ba.Timer(
                powerup_expiration_time - 2000,
                _jetpack_wear_off_flash,
                timeformat=ba.TimeFormat.MILLISECONDS,
            )
            self._jetpack_wear_off_timer = ba.Timer(
                powerup_expiration_time,
                _jetpack_wear_off,
                timeformat=ba.TimeFormat.MILLISECONDS,
            )

        def _jetpack_wrapper():
            if not self.node.exists():
                return

            if self.node.knockout <= 0 and self.node.frozen <= 0:
                self.node.jump_pressed = True
                ba.emitfx(
                    position=(
                        self.node.position[0],
                        self.node.position[1] - 0.5,
                        self.node.position[2],
                    ),
                    velocity=(0, -10, 0),
                    count=75,
                    spread=0.25,
                    chunk_type="spark",
                )

        def jetpack_wrapper():
            self.node.handlemessage(
                "impulse",
                self.node.position[0],
                self.node.position[1] + 10,
                self.node.position[2],
                0,
                0,
                0,
                150,
                20,
                0,
                0,
                0,
                150,
                0,
            )

            for i in range(0, 200, 50):
                ba.timer(i, _jetpack_wrapper, timeformat=ba.TimeFormat.MILLISECONDS)

            # self._turboFilterAddPress('jump')  # Это че?

        self.node.getdelegate(PlayerSpaz).getplayer(ba.Player).assigninput(
            ba.InputType.JUMP_PRESS, jetpack_wrapper
        )

    def companion_cube(self, msg):
        CompanionCube(
            position=(
                self.node.position[0],
                self.node.position[1] + 1,
                self.node.position[2],
            ),
            velocity=(0, 5, 0),
        ).autoretain()

    def lucky_block(self, msg):
        event_number = randint(1, 15)

        if event_number in (1, 2, 3):
            powerup_type = PowerupBoxFactory().get_random_powerup_type()

            self.node.handlemessage(ba.PowerupMessage(poweruptype=powerup_type))
        elif event_number == 4:
            ba.camerashake(1)
            ba.emitfx(
                position=(
                    self.node.position[0],
                    self.node.position[1] + 4,
                    self.node.position[2],
                ),
                velocity=(0, 0, 0),
                count=700,
                spread=0.7,
                chunk_type="spark",
            )

            powerup_type = PowerupBoxFactory.get().get_random_powerup_type()

            PowerupBox(
                position=(
                    self.node.position[0],
                    self.node.position[1] + 4,
                    self.node.position[2],
                ),
                poweruptype=powerup_type,
                expire=True,
            ).autoretain()

            powerup_type = PowerupBoxFactory.get().get_random_powerup_type()

            PowerupBox(
                position=(
                    self.node.position[0],
                    self.node.position[1] + 4,
                    self.node.position[2],
                ),
                poweruptype=powerup_type,
                expire=True,
            ).autoretain()

            powerup_type = PowerupBoxFactory.get().get_random_powerup_type()

            PowerupBox(
                position=(
                    self.node.position[0],
                    self.node.position[1] + 4,
                    self.node.position[2],
                ),
                poweruptype=powerup_type,
                expire=True,
            ).autoretain()
        elif event_number == 5:
            Bomb(
                position=(
                    self.node.position[0],
                    self.node.position[1] + 3,
                    self.node.position[2],
                ),
                source_player=self.source_player,
                owner=self.node,
                blast_radius=6,
            ).autoretain()
        elif event_number == 6:
            self.node.handlemessage(ba.FreezeMessage())
        elif event_number == 7:
            chunk_type = ("ice", "rock", "metal", "spark", "splinter", "slime")

            ba.emitfx(
                position=self.node.position,
                velocity=(
                    random() * 2,
                    random() * 2,
                    random() * 2,
                ),
                count=600,
                spread=random(),
                chunk_type=choice(chunk_type),
            )

            ba.camerashake(1)
            ba.playsound(ba.getsound("corkPop"))  # position=self.node.position?
        elif event_number == 8:
            position = self.node.position

            def rain_wrapper():
                p_type = PowerupBoxFactory.get().get_random_powerup_type()

                new_position = (
                    -10 + position[0] + random() * 20,
                    position[1] + 6,
                    -10 + position[2] + random() * 20,
                )

                PowerupBox(poweruptype=p_type, position=new_position).autoretain()

                if random() > 0.04:
                    ba.timer(0.1, rain_wrapper)

            rain_wrapper()
        elif event_number == 9:
            Blast(
                position=self.node.position,
                velocity=self.node.velocity,
                blast_radius=1.0,
                blast_type="normal",
                source_player=None,
                hit_type="punch",
                hit_subtype="normal",
            )
        elif event_number == 10:  # Blast-square under spaz
            x = self.node.position[0] - 2
            while x < self.node.position[0] + 2:
                y = self.node.position[2] - 2
                while y < self.node.position[2] + 2:
                    Blast(
                        position=(x, self.node.position[1], y),
                        velocity=(
                            self.node.velocity[0],
                            self.node.velocity[1] + 10,
                            self.node.velocity[2],
                        ),
                        blast_radius=0.5,
                        blast_type="normal",
                        source_player=None,
                        hit_type="punch",
                        hit_subtype="normal",
                    )

                    y += 1

                x += 1
        elif event_number == 11:
            offset = -15
            case = 1 if random.random() < 0.5 else -1
            while offset < 15:
                velocity = (case * (12 + 8 * random.random()), -0.1, 0)
                Bomb(
                    bomb_type="tnt",
                    position=(
                        self.node.position[0] - case * 10,
                        self.node.position[1] + 3,
                        self.node.position[2] + offset,
                    ),
                    velocity=velocity,
                ).autoretain()

                offset += 1.5
        elif event_number == 12:
            color = {0.0: (0, 0, 3), 0.5: (0, 3, 0), 1.0: (3, 0, 0), 1.5: (0, 0, 3)}
            ba.animate_array(self.node, "color", 3, color, True)
            self.node.handlemessage("celebrate", 100000000)
        elif event_number == 13:
            CompanionCube(
                position=(
                    self.node.position[0],
                    self.node.position[1] + 1,
                    self.node.position[2],
                ),
                velocity=(0, 10, 0),
            ).autoretain()
        elif event_number == 14:
            ba.emitfx(
                position=self.node.position,
                count=100,
                emit_type="tendrils",
                tendril_type="smoke",
            )

        elif event_number == 15:

            def drop_man():
                botset: SpazBotSet
                activity = ba.getactivity()
                if not hasattr(activity, "botset"):
                    activity.botset = botset = SpazBotSet()
                botset = activity.botset
                aoi_bounds = self.activity.globalsnode.area_of_interest_bounds
                botset.spawn_bot(
                    BrawlerBotLite,
                    (
                        random.randrange(int(aoi_bounds[0]), int(aoi_bounds[3]) + 1),
                        aoi_bounds[4] - 1,
                        random.randrange(int(aoi_bounds[2]), int(aoi_bounds[5]) + 1),
                    ),
                    spawn_time=0.001,
                )

            def lightning_bolt(position, radius=1):
                ba.camerashake(4)
                vignette_outer = self.activity.globalsnode.vignette_outer
                # if ba.getactivity().tint is None:
                #     ba.getactivity().std_tint = ba.sharedobj('globals').vignette_outer
                #     vignette_outer = ba.sharedobj('globals').vignette_outer
                # else:
                #     vignette_outer = ba.getactivity().tint

                light = ba.newnode(
                    "light",
                    attrs={
                        "position": position,
                        "color": (0.4, 0.4, 0.8),
                        "volume_intensity_scale": 1.0,
                        "radius": radius,
                    },
                )

                ba.animate(
                    light,
                    "intensity",
                    {
                        0: 1,
                        50: radius,
                        150: radius / 2,
                        250: 0,
                        260: radius,
                        410: radius / 2,
                        510: 0,
                    },
                    timeformat=ba.TimeFormat.MILLISECONDS,
                    suppress_format_warning=True,
                )

                ba.animate_array(
                    self.activity.globalsnode,
                    "vignette_outer",
                    3,
                    {0: vignette_outer, 0.2: (0.2, 0.2, 0.2), 0.51: vignette_outer},
                )

                # ba.playsound(
                #     ba.getsound('grom'),
                #     volume=10,
                #     position=(0, 10, 0))

            lightning_bolt(self.node.position)

            for time in range(15):
                ba.timer(time, drop_man)


register_powerups(Test)
