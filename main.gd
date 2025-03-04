extends Node2D

var lander: KinematicBody2D
var velocity: Vector2 = Vector2.ZERO
var gravity: float = 10.0
var thrust: float = -20.0
var terrain: Array

func _ready():
    lander = $Lander
    randomize_moonscape()

func _process(delta):
    velocity.y += gravity * delta
    
    if Input.is_action_pressed("ui_up"):
        velocity.y += thrust * delta
    
    velocity = lander.move_and_slide(velocity, Vector2.UP)
    
    if lander.position.y > 600:
        lander.position.y = 100
        velocity = Vector2.ZERO

func randomize_moonscape():
    var terrain_node = $MoonScape
    var terrain = Line2D.new()
    terrain.width = 2
    var points = []
    var x = 0
    while x < 800:
        var y = randi() % 400 + 200
        points.append(Vector2(x, y))
        x += 50
    points.append(Vector2(800, 600))
    points.append(Vector2(0, 600))
    terrain.points = points
    terrain_node.add_child(terrain)