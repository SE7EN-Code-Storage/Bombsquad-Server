import ba
import math
import random
from core.internal import locale
import bastd.actor.bomb as stdbomb
from bastd.actor import playerspaz
from bastd.gameutils import SharedObjects

# ---------------------------------- POWERUP OBJECTS ---------------------------------------------------------------------


class Prefix(ba.Actor):
    def __init__(
        self,
        owner=None,
        prefix="",
        color=(1, 1, 1),
        position=(0, 1.55, 0),
        animation=(-65528, -16713473, -15335680),
        animate=False,
        emit="off",
        particle="spark",
    ):
        super().__init__()
        self.owner = owner
        self.prefix = prefix
        self.color = color
        self.position = position
        self.animation = animation
        self.emit = emit
        self.particle = particle

        self._offset = 0
        self._radius = 1

        emit_time = 0.06 if emit in ("sweat", "spark") else 0.11
        if emit != "off":
            self.type_selection_handler_timer = ba.Timer(
                emit_time, self._type_selection_handler, repeat=True
            )

        self.math_node = ba.newnode(
            "math", owner=self.owner, attrs={"input1": position, "operation": "add"}
        )

        self.owner.connectattr("torso_position", self.math_node, "input2")
        self.prefix_node = ba.newnode(
            "text",
            owner=self.owner,
            attrs={
                "text": prefix,
                "color": color,
                "scale": 0.01,
                "shadow": 0.5,
                "flatness": 0,
                "in_world": True,
                "h_align": "center",
            },
        )

        self.math_node.connectattr("output", self.prefix_node, "position")
        ba.animate(self.prefix_node, "scale", {0: 0.0, 1: 0.01})
        if animate:
            ba.animate_array(
                self.prefix_node,
                "color",
                3,
                self.animation,
                True,
                timeformat=ba.TimeFormat.MILLISECONDS,
            )

    def _first_type_handler(self):
        owner_torso_pos = self.owner.torso_position
        position = (
            owner_torso_pos[0] - 0.25 + random.random() * 0.5,
            owner_torso_pos[1] - 0.25 + random.random() * 0.5,
            owner_torso_pos[2] - 0.25 + random.random() * 0.5,
        )

        if self.particle in ("sweat", "spark"):
            spread = 0.1
            scale = random.random() * 0.8
            owner_vel = self.owner.velocity
            vel = 4 if not self.particle == "ice" else 0
            velocity = (
                (-vel + (random.random() * (vel * 2))) + owner_vel[0] * 2,
                (-vel + (random.random() * (vel * 2))) + owner_vel[1] * 4,
                (-vel + (random.random() * (vel * 2))) + owner_vel[2] * 2,
            )
        else:
            spread = 0.15
            velocity = (0, 0, 0)
            scale = random.random() * 0.6

        ba.emitfx(
            position=position,
            velocity=velocity,
            count=10,
            scale=scale,
            spread=spread,
            chunk_type=self.particle,
        )

    def _second_type_handler(self):
        position = (
            self.owner.position[0],
            self.owner.position[1] - 0.25,
            self.owner.position[2],
        )

        if self.particle == "splinter":
            ba.emitfx(
                position=position,
                count=1,
                scale=0.02 + random.random(),
                spread=0.15,
                chunk_type=self.particle,
            )
        else:
            ba.emitfx(
                position=position,
                count=10,
                scale=0.1 + random.random(),
                spread=0.15,
                chunk_type=self.particle,
            )

    def _third_type_handler(self):
        sin = math.sin(self._offset) * self._radius
        cos = math.cos(self._offset) * self._radius
        self._offset += 0.1
        position = (
            self.owner.position[0] + cos,
            self.owner.position[1],
            self.owner.position[2] + sin,
        )

        ba.emitfx(
            position=position, count=5, scale=1, spread=0, chunk_type=self.particle
        )

    def _fourth_type_handler(self):
        position = (
            self.owner.position[0],
            self.owner.position[1] - 0.5,
            self.owner.position[2],
        )

        ba.emitfx(
            position=position,
            count=10,
            scale=0.1 + random.random(),
            spread=0.001,
            chunk_type=self.particle,
            emit_type="stickers",
        )

    def _type_selection_handler(self):
        if self.owner and not self.owner.dead:
            if self.emit == "body":
                self._first_type_handler()
            elif self.emit == "legs":
                self._second_type_handler()
            elif self.emit == "around":
                self._third_type_handler()
            elif self.emit == "underfoot":
                self._fourth_type_handler()

    def handlemessage(self, msg):
        if isinstance(msg, ba.DieMessage):
            self.math_node.delete()
            self.prefix_node.delete()


class Airstrike(ba.Actor):
    """Bombing zone.
    Args:
        position (:obj:`tuple`, optional): Spawn position.
        velocity (:obj:`tuple`, optional): Speed and direction of travel.
        amount (:obj:`int`, optional): The number of bombs to be dropped.
        bomb_type (:obj:`str`, optional): Type of bombs to be dropped.
        highlight (:obj:`bool`, optional): To highlight the bombing zone.
    """

    def __init__(
        self,
        position=(0, 3, 0),
        velocity=(0, -5, 0),
        amount: int = 15,
        bomb_type: str = "impact",
        highlight: bool = True,
        source_player: ba.Player = None,
    ):
        ba.Actor.__init__(self)
        self.position = position
        self.velocity = velocity
        self.amount = amount
        self.bomb_type = bomb_type
        self._source_player = source_player

        self.drop_count = 0

        # highlight the bombing zone
        if highlight:
            self.area_highlight = ba.newnode(
                "light",
                attrs={
                    "color": (1, 0, 0),
                    "position": position,
                    "volume_intensity_scale": 1.0,
                },
            )

            ba.animate(
                self.area_highlight, "volume_intensity_scale", {0: 0, 0.5: 1.0, 1: 0}
            )

        def wrapper():
            self.drop_timer = ba.Timer(0.25, self._drop_bomb, repeat=True)

        ba.timer(1, wrapper)

    def _drop_bomb(self):
        """Drop a certain amount of bombs."""
        if self.drop_count < self.amount:
            activity = ba.getactivity()
            assert isinstance(activity, ba.GameActivity)
            highest_pos = activity.map.get_def_bound_box("map_bounds")[4]
            drop_position = (
                self.position[0] + random.uniform(1.5, -1.5),
                highest_pos,
                self.position[2] + random.uniform(1.5, -1.5),
            )

            stdbomb.Bomb(
                bomb_type=self.bomb_type,
                position=drop_position,
                blast_radius=3,
                velocity=self.velocity,
                source_player=self._source_player,
            ).autoretain()

            self.drop_count += 1
        else:
            self.drop_timer = None


class AutoAim:
    """Automatic item direction for player.
    Args:
        item (ba.Node): The node of the item.
        owner (ba.Node): The node of the player who used the item.
    """

    def __init__(self, item: ba.Node, owner: ba.Node):
        self.item = item
        self.owner = owner

        self.node: ba.Node
        self.target = None

        self.aim_zone: ba.Material = ba.Material()
        shared = SharedObjects.get()
        self.aim_zone.add_actions(
            conditions=(("they_have_material", shared.player_material)),
            actions=(
                ("modify_part_collision", "collide", True),
                ("modify_part_collision", "physical", False),
                ("call", "at_connect", self._touch_handler),
            ),
        )

        # raise the item a little
        self.item.extra_acceleration = (0, 20, 0)
        # if the item exists, then take its position,
        # else "turn the bench"
        if self.item.exists():
            position = self.item.position
        else:
            return

        self.node = ba.newnode(
            "region",
            attrs={
                "type": "sphere",
                "position": position,
                "materials": [self.aim_zone],
            },
        )

        # aiming effect
        ba.animate_array(self.node, "scale", 3, {0: (0.1, 0.1, 0.1), 1: (60, 60, 60)})

    def _touch_handler(self) -> None:
        """The action handler of an item if it touches a target."""
        node: ba.Node = ba.getcollision().opposingnode
        node_team: ba.Team = (
            node.getdelegate(playerspaz.PlayerSpaz).getplayer(ba.Player).team
            if hasattr(node.getdelegate(playerspaz.PlayerSpaz), "getplayer")
            else None
        )

        owner_team = (
            self.owner.getdelegate(playerspaz.PlayerSpaz).getplayer(ba.Player).team
        )
        if (
            node.exists()
            and self.owner.exists()
            and self.item.exists()
            and node_team is not None
            and node_team != owner_team
            and node.getdelegate(playerspaz.PlayerSpaz).is_alive()
        ):
            self.target = node
            self.node.delete()
            self.item.extra_acceleration = (0, 20, 0)
            self._move_item()

    def _move_item(self) -> None:
        """The movement of the item to the target."""
        if self.target and self.target.exists() and self.item.exists():
            item_velocity = self.item.velocity
            item_position = self.item.position
            target_position = self.target.position
            self.item.velocity = (
                item_velocity[0] + (target_position[0] - item_position[0]),
                item_velocity[1] + (target_position[1] - item_position[1]),
                item_velocity[2] + (target_position[2] - item_position[2]),
            )

            ba.timer(0.001, self._move_item)

    def off(self) -> None:
        """Deleting a target."""
        self.target = None


class CompanionCube(ba.Actor):
    """He will heal you if you take it in your hands.
    Args:
        position (:obj:`tuple`, optional): Spawn position.
        velocity (:obj:`tuple`, optional): Speed and direction of travel.
    """

    def __init__(self, position=(0, 1, 0), velocity=(0, 0, 0)):
        super().__init__()
        self.light: ba.Node
        self.picked: bool
        self.regen_timer = None
        self.phrase_text_node = None

        from . import core

        self.phrases = locale("objects.companion_cube_text")
        self.phrases_times = (10.0, 12.5, 15.0, 17.5, 20.0, 22.5, 25.0, 27.5, 30.0)

        self.phrases_time: float = random.choice(self.phrases_times)
        shared = SharedObjects.get()

        self.node: ba.Node = ba.newnode(
            "prop",
            delegate=self,
            attrs={
                "body": "crate",
                "model": ba.getmodel("tnt"),
                "light_model": ba.getmodel("tnt"),
                "color_texture": ba.gettexture("landMineLit"),
                "position": position,
                "velocity": velocity,
                "reflection": "soft",
                "reflection_scale": [0.25],
                "materials": (shared.object_material, shared.footing_material),
            },
        )
        ba.animate(self.node, "model_scale", {0: 0, 0.2: 1.3, 0.26: 1})

        self.spawn_random_phrase_timer: ba.Timer = ba.Timer(
            self.phrases_time, self._spawn_random_phrase, repeat=True
        )

    def _spawn_random_phrase(self) -> None:
        """Spawn a random phrase over a cube."""
        if self.node:
            self.phrases_time = random.choice(self.phrases_times)
            math: ba.Node = ba.newnode(
                "math",
                owner=self.node,
                attrs={"input1": (0, 0.6, 0), "operation": "add"},
            )

            self.node.connectattr("position", math, "input2")
            if self.phrase_text_node is not None:
                ba.animate(self.phrase_text_node, "scale", {0: 0.01, 0.5: 0})

                def wrapper():
                    self.phrase_text_node.delete()

                ba.timer(0.5, wrapper)

            def spawn_wrapper():
                if self.node.exists():
                    self.phrase_text_node = ba.newnode(
                        "text",
                        owner=self.node,
                        attrs={
                            "text": random.choice(self.phrases),
                            "scale": 0.0,
                            "in_world": True,
                            "h_align": "center",
                        },
                    )

                    math.connectattr("output", self.phrase_text_node, "position")

                    ba.animate(
                        self.phrase_text_node,
                        "scale",
                        {0: 0.0, 0.5: 0.01, 5: 0.01, 5.5: 0.0},
                    )

            ba.timer(1, spawn_wrapper)
        else:
            self.spawn_random_phrase_timer = None

    def handlemessage(self, msg):
        if isinstance(msg, ba.DieMessage):
            if self.node:
                self.node.delete()

        elif isinstance(
            msg, ba.OutOfBoundsMessage
        ):  # Hmm, what? DieMessage calls too, don't it?
            if self.node:
                self.node.delete()

        elif isinstance(msg, ba.PickedUpMessage):
            self.node.extra_acceleration = (0, 25, 0)

            def up():
                if self.node.exists():
                    self.node.extra_acceleration = (0, 35, 0)

            ba.timer(0.3, up)

            def check():
                if not msg or not msg.node.exists():
                    self.node.extra_acceleration = (0, 0, 0)

            ba.timer(0.1, check)

            def regen():
                if (
                    msg is not None
                    and msg.node.exists()
                    and msg.node.getdelegate(playerspaz.PlayerSpaz).hitpoints
                    < msg.node.getdelegate(playerspaz.PlayerSpaz).hitpoints_max
                ):
                    msg.node.getdelegate(playerspaz.PlayerSpaz).hitpoints += 1
                    msg.node.getdelegate(playerspaz.PlayerSpaz)._last_hit_time = None
                    msg.node.getdelegate(playerspaz.PlayerSpaz)._num_time_shit = 0
                    msg.node.hurt -= 0.001
                    ba.emitfx(
                        position=msg.node.position,
                        velocity=(0, 3, 0),
                        count=int(3.0 + random.random() * 5),
                        scale=1.5,
                        spread=0.3,
                        chunk_type="sweat",
                    )
                else:
                    self.regen_timer = None

            self.regen_timer = ba.Timer(0.01, regen, repeat=True)

        elif isinstance(msg, ba.DroppedMessage):
            self.regen_timer = None
            self.node.extra_acceleration = (0, 0, 0)

        elif isinstance(msg, ba.HitMessage):
            self.node.handlemessage(
                "impulse",
                *msg.pos,
                *msg.velocity,
                msg.magnitude,
                msg.velocity_magnitude,
                msg.radius,
                0,
                *msg.velocity,
            )


class Portals(ba.Actor):
    """Two portals.
    Args:
        color (:obj:`tuple`, optional): Portals colors.
        radius (:obj:`float`, optional): Portals volume radius.
        first_position (:obj:`tuple`, optional): First portal position.
        second_position (:obj:`tuple`, optional): Second portal position.
    """

    def __init__(
        self,
        color=(1, 1, 1),
        radius=1.25,
        first_position=(-3, 1, 0),
        second_position=(3, 1, 0),
    ):
        super().__init__()
        self.first_position = first_position
        self.second_position = second_position
        self.radius = radius

        # self.cooldown = False
        self.already_teleported = {}
        self.node_radius = radius / 1.75

        node_scale = {
            0: (0, 0, 0),
            0.5: (self.node_radius, self.node_radius, self.node_radius),
        }

        # portal materials
        self.first_portal_material = ba.Material()
        shared = SharedObjects.get()
        self.first_portal_material.add_actions(
            conditions=(("they_have_material", shared.player_material)),
            actions=(
                ("modify_part_collision", "collide", True),
                ("modify_part_collision", "physical", False),
                ("call", "at_connect", self._first_portal_teleportation),
            ),
        )

        self.first_portal_material.add_actions(
            conditions=(
                ("they_have_material", shared.player_material),
                "and",
                ("they_dont_have_material", shared.player_material),
            ),
            actions=(
                ("modify_part_collision", "collide", True),
                ("modify_part_collision", "physical", False),
                ("call", "at_connect", self._first_portal_handler),
            ),
        )

        self.second_portal_material = ba.Material()
        self.second_portal_material.add_actions(
            conditions=(("they_have_material", shared.player_material)),
            actions=(
                ("modify_part_collision", "collide", True),
                ("modify_part_collision", "physical", False),
                ("call", "at_connect", self._second_portal_teleportation),
            ),
        )

        self.second_portal_material.add_actions(
            conditions=(
                ("they_have_material", shared.object_material),
                "and",
                ("they_dont_have_material", shared.player_material),
            ),
            actions=(
                ("modify_part_collision", "collide", True),
                ("modify_part_collision", "physical", False),
                ("call", "at_connect", self._second_portal_handler),
            ),
        )

        # create a first portal
        self.first_node = ba.newnode(
            "region",
            attrs={
                "type": "sphere",
                "position": self.first_position,
                "materials": [self.first_portal_material],
            },
        )

        self.first_node_visualization = ba.newnode(
            "shield", attrs={"color": color, "position": self.first_position}
        )

        ba.animate(self.first_node_visualization, "radius", {0: 0, 0.5: radius})

        # ba.animate_array(self.first_node, 'scale', 3, node_scale)

        # create a second portal
        self.second_node = ba.newnode(
            "region",
            attrs={
                "type": "sphere",
                "position": self.second_position,
                "materials": [self.second_portal_material],
            },
        )

        self.second_node_visualization = ba.newnode(
            "shield", attrs={"color": color, "position": self.second_position}
        )

        ba.animate(self.second_node_visualization, "radius", {0: 0, 0.5: radius})

        # ba.animate_array(self.second_node, 'scale', 3, node_scale)

        # delete portals after some period
        ba.timer(10, self.delete)

    def delete(self):
        """Delete all portals and their visualization."""
        self.first_node.delete()
        self.second_node.delete()
        self.first_node_visualization.delete()
        self.second_node_visualization.delete()

    def _first_portal_teleportation(self):
        """Teleportation of a node that entered the first portal."""
        node = ba.getcollision().opposingnode
        name = node.getname()

        if self.already_teleported.get(name):
            return

        def wrapper(nodename):
            self.already_teleported[nodename] = False

        hold_node = node.hold_node

        node.handlemessage(ba.StandMessage(position=self.second_node.position))

        if hold_node:
            self._first_portal_handler(hold_node, offset=(0, 1, 0))
            node.hold_node = hold_node

        self.already_teleported[name] = True
        ba.timer(1, ba.Call(wrapper, name))

    def _second_portal_teleportation(self):
        """Teleportation of a node that entered the second portal."""
        node = ba.getcollision().opposingnode
        name = node.getname()

        if self.already_teleported.get(name):
            return

        def wrapper(nodename):
            self.already_teleported[nodename] = False

        hold_node = node.hold_node

        node.handlemessage(ba.StandMessage(position=self.first_node.position))

        if hold_node:
            self._second_portal_handler(hold_node, offset=(0, 1, 0))
            node.hold_node = hold_node

        self.already_teleported[name] = True
        ba.timer(1, ba.Call(wrapper, name))

    def _first_portal_handler(self, node=None, offset=(0, 0, 0)):
        """Checking a node before teleporting in the first portal."""
        if node is None:
            node = ba.getcollision().opposingnode
        name = node.getname()

        if self.already_teleported.get(name):
            return
        velocity = node.velocity
        node.position = (
            self.second_position[0] + offset[0],
            self.second_position[1] + offset[1],
            self.second_position[2] + offset[2],
        )

        def velocity_wrapper():
            if node:
                node.velocity = velocity

        ba.timer(0.001, velocity_wrapper)

        self.already_teleported[node.getname()] = True

        def wrapper(nodename):
            self.already_teleported[nodename] = False

        ba.timer(1, ba.Call(wrapper, name))

    def _second_portal_handler(self, node=None, offset=(0, 0, 0)):
        """Checking a node before teleporting in the second portal."""
        if node is None:
            node = ba.getcollision().opposingnode

        name = node.getname()

        if self.already_teleported.get(name):
            return

        velocity = node.velocity
        node.position = (
            self.first_position[0] + offset[0],
            self.first_position[1] + offset[1],
            self.first_position[2] + offset[2],
        )

        def velocity_wrapper():
            if node:
                node.velocity = velocity

        ba.timer(0.01, velocity_wrapper)

        self.already_teleported[name] = True

        def wrapper(nodename):
            self.already_teleported[nodename] = False

        ba.timer(1, ba.Call(wrapper, name))


class TreatmentArea(ba.Actor):
    """The area in which players receive health kit.
    Args:
        position (:obj:`tuple`, optional): Spawn position.
        lifetime (:obj:`int`, optional): Treatment area and highlight life.
        highlight (:obj:`bool`, optional): To highlight the treatment area.
    """

    def __init__(
        self, position=(0, 1, 0), lifetime: float = 0.5, highlight: bool = True
    ):
        super().__init__()
        # array of nodes that received health kit
        self.cured_nodes = []

        self.area_material: ba.Material = ba.Material()
        shared = SharedObjects.get()
        self.area_material.add_actions(
            conditions=(("they_have_material", shared.player_material)),
            actions=(
                ("modify_part_collision", "collide", True),
                ("modify_part_collision", "physical", False),
                ("call", "at_connect", self._touch_handler),
            ),
        )

        # the area itself...
        self.node: ba.Node = ba.newnode(
            "region",
            attrs={
                "type": "sphere",
                "scale": (2, 2, 2),
                "position": position,
                "materials": [self.area_material],
            },
        )

        ba.timer(lifetime, self.node.delete)

        # highlight the treatment area
        if highlight:
            self.area_highlight: ba.Node = ba.newnode(
                "light",
                attrs={
                    "color": (1, 1, 1),
                    "radius": 0.25,
                    "position": position,
                    "volume_intensity_scale": 1.0,
                },
            )

            # a little beautiful animation
            ba.animate(
                self.area_highlight, "intensity", {0: 0, lifetime / 2: 1.0, lifetime: 0}
            )

    def _touch_handler(self):
        """The action handler of an item if it touches a target."""
        node: ba.Node = ba.getcollision().opposingnode
        if node not in self.cured_nodes:
            node.handlemessage(ba.PowerupMessage(poweruptype="health"))

            self.cured_nodes.append(node)
