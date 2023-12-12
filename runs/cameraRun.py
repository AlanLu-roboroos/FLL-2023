from threading import Thread


class CameraRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.Rlight = config.Rlight
        self.arm = config.LMmotor
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(-90)
        self.drive.moveDist(100, heading=-86)
        self.drive.moveLight(self.Rlight, [0, 15])
        self.drive.moveDist(120, heading=-86)
        self.arm.run_angle(-500, 100)
        self.drive.moveDist(-20, heading=-90)
        self.drive.moveDist(300, heading=-90)
        self.drive.moveDist(-50, heading=-90)
        self.drive.turnTo(-60)
        self.drive.moveArc(-2000, -125, speed=700, timeout=3000)


        self.config.state.setState(1)
