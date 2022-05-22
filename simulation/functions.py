import math

def collide(p1, p2):
    #collide two particles
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    
    distance = math.hypot(dx, dy)
    if distance < p1.size + p2.size:
        tangent = math.atan2(dy, dx)
        angle = 0.5 * math.pi + tangent

        angle1 = 2*tangent - p1.angle
        angle2 = 2*tangent - p2.angle
        speed1 = p2.speed
        speed2 = p1.speed

        (p1.angle, p1.speed) = (angle1, speed1)
        (p2.angle, p2.speed) = (angle2, speed2)

        p1.x += math.sin(angle)
        p1.y -= math.cos(angle)
        p2.x -= math.sin(angle)
        p2.y += math.cos(angle)