from threading import Thread


class RunBack(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(-90)
        self.drive.moveDist(-300, heading=-135, turn=False)
        self.drive.moveArc(-250, -50, speed=-120)
        self.drive.moveDist(-100, heading=-50)
        self.drive.moveDist(280, heading=-50)
        self.drive.turnTo(-160)
        self.config.LMmotor.run_angle(400, 410)
        self.drive.turnTo(-125)
        self.config.LMmotor.run_angle(-1000, 200)
        self.drive.moveDist(-1000, heading=-80)

        self.config.state.setState(1)
