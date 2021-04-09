import jetson.inference
import jetson.utils

net = jetson.inference.detectNet("ssd-mobilenet-v2")
camera = jetson.utils.gstCamera(640,380,'0')
display = jetson.utils.glDisplay()

while display.IsOpen():
	img, width, height = camera.CaptureRGBA()
	detections = net.Detect(img, width, height)
	display.RenderOnce(img, width, height)
	display.SetTitle("Object Detection | Network {:.0f} FPS".format(1000.0 / net.GetNetworkTime()))
