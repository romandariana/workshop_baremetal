
import pygame
import time
import adi

def clamp(val, min, max):
	return min if val < min else max if val > max else val

def done(x, y, expected_x, expected_y, tolerance):
	return True if ((x > (expected_x - tolerance)) and (x < (expected_x + tolerance)) and (y > (expected_y - tolerance)) and ((y < expected_y + tolerance))) else False

adxl355 = adi.adxl355(uri="serial:/dev/ttyACM0,57600,8n1n")

WINDOW_WIDTH = 959 * 2
WINDOW_HEIGHT = 507 * 2

image_pcb = pygame.image.load("images/0.png")
SCALE_FACTOR =  image_pcb.get_width() / WINDOW_WIDTH
image_pcb = pygame.transform.scale(image_pcb, (image_pcb.get_width()/SCALE_FACTOR, image_pcb.get_height()/SCALE_FACTOR))

image_res = pygame.image.load("images/1.png")
image_res = pygame.transform.scale(image_res, (image_res.get_width()/SCALE_FACTOR, image_res.get_height()/SCALE_FACTOR))

image_ic = pygame.image.load("images/2.png")
image_ic = pygame.transform.scale(image_ic, (image_ic.get_width()/SCALE_FACTOR, image_ic.get_height()/SCALE_FACTOR))

image_cap = pygame.image.load("images/3.png")
image_cap = pygame.transform.scale(image_cap, (image_cap.get_width()/SCALE_FACTOR, image_cap.get_height()/SCALE_FACTOR))

image_led = pygame.image.load("images/4.png")
image_led = pygame.transform.scale(image_led, (image_led.get_width()/SCALE_FACTOR, image_led.get_height()/SCALE_FACTOR))

image_bat = pygame.image.load("images/5.png")
image_bat = pygame.transform.scale(image_bat, (image_bat.get_width()/SCALE_FACTOR, image_bat.get_height()/SCALE_FACTOR))

led_off = pygame.image.load("images/5.png")
led_off = pygame.transform.scale(led_off, (led_off.get_width()/SCALE_FACTOR, led_off.get_height()/SCALE_FACTOR))

led_on = pygame.image.load("images/6.png")
led_on = pygame.transform.scale(led_on, (led_on.get_width()/SCALE_FACTOR, led_on.get_height()/SCALE_FACTOR))

component_ic = pygame.image.load("images/tsot-23-6.png")
component_ic = pygame.transform.scale(component_ic, (component_ic.get_width()/SCALE_FACTOR, component_ic.get_height()/SCALE_FACTOR))

component_c = pygame.image.load("images/c_1206_3216metric.png")
component_c = pygame.transform.scale(component_c, (component_c.get_width()/SCALE_FACTOR, component_c.get_height()/SCALE_FACTOR))

component_led = pygame.image.load("images/led_d3.0mm_clear.png")
component_led = pygame.transform.scale(component_led, (component_led.get_width()/SCALE_FACTOR, component_led.get_height()/SCALE_FACTOR))

component_battery = pygame.image.load("images/battery_cr1225.png")
component_battery = pygame.transform.scale(component_battery, (component_battery.get_width()/SCALE_FACTOR, component_battery.get_height()/SCALE_FACTOR))

pygame.init()

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('no-OS Hands-On')

screen.blit(image_pcb,(0,0))
pygame.display.update()

time.sleep(1)

screen.blit(image_res,(0,0))
pygame.display.update()

time.sleep(1)

font = pygame.font.SysFont(None, 75)
text_surf = font.render("It's your turn. Place the rest of the components...", True, (255, 255, 255))
text_surf.set_alpha(255)
screen.blit(text_surf, (380, 930))
pygame.display.update()

time.sleep(3)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	screen.blit(image_res,(0,0))

	x = adxl355.accel_x.raw * (-1) + 262144
	y = adxl355.accel_y.raw + 262144

	x = x / (524287 / (WINDOW_WIDTH - component_ic.get_width()))
	y = y / (524287 / (WINDOW_HEIGHT - component_ic.get_height()))

	screen.blit(component_ic,(x, y))

	pygame.display.update()

	if done(x, y, 1358 / SCALE_FACTOR, 1094 / SCALE_FACTOR, 10):
		break

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	screen.blit(image_ic,(0,0))

	x = adxl355.accel_x.raw * (-1) + 262144
	y = adxl355.accel_y.raw + 262144

	x = x / (524287 / (WINDOW_WIDTH - component_c.get_width()))
	y = y / (524287 / (WINDOW_HEIGHT - component_c.get_height()))

	screen.blit(component_c,(x, y))

	pygame.display.update()

	if done(x, y, 1698 / SCALE_FACTOR, 200 / SCALE_FACTOR, 10):
		break

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	screen.blit(image_cap,(0,0))

	x = adxl355.accel_x.raw * (-1) + 262144
	y = adxl355.accel_y.raw + 262144

	x = x / (524287 / (WINDOW_WIDTH - component_led.get_width()))
	y = y / (524287 / (WINDOW_HEIGHT - component_led.get_height()))

	screen.blit(component_led,(x, y))

	pygame.display.update()

	if done(x, y, 1284 / SCALE_FACTOR, 460 / SCALE_FACTOR, 10):
		break

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	screen.blit(image_led,(0,0))

	x = adxl355.accel_x.raw * (-1) + 262144
	y = adxl355.accel_y.raw + 262144

	x = x / (524287 / (WINDOW_WIDTH - component_battery.get_width()))
	y = y / (524287 / (WINDOW_HEIGHT - component_battery.get_height()))

	screen.blit(component_battery,(x, y))

	pygame.display.update()

	if done(x, y, 1994 / SCALE_FACTOR, 360 / SCALE_FACTOR, 10):
		break

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

	screen.blit(led_off,(0,0))
	pygame.display.update()
	time.sleep(1)

	screen.blit(led_on,(0,0))
	pygame.display.update()
	time.sleep(1)
