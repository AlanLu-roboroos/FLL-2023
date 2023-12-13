from threading import Thread

class CameraRun2(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(90)
        self.drive.drive.drive(150, 5)
        self.wait(2000)
        self.drive.drive.drive(50, 5)
        self.runArmAngle(-200, 300)
        self.drive.moveDist(-700)

        self.config.state.setState(1)
    
    def runArmAngle(self, speed, angle):
      self.config.LMmotor.run_angle(speed, angle, wait=False)
      self.config.RMmotor.run_angle(-speed, angle, wait=True)

