class Map(object):
    scenes=[
            'central_corridor':CentralCorridor(),
            'laser_weapon_armory':LaserWeaponArmory(),
            'the_brideg':TheBridge(),
            'escape_pod':EscapePod(),
            'death':Death()
            ]
    def __init__(self,start_scene):
        self.start_scene=start_scene
    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)
    def opening_scene(self):
        return self.next_scene(self.start_scene)

    a_map=Map('central_cooridor')
    a_game=Engine(a_map)
    a_game.play()
