from threading import Thread


class ChickenRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.spinner = config.LMmotor
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(-45)

        self.drive.moveDist(400, heading=-45)
        self.spinner.run(-4000)
        self.wait(5000)
        self.drive.moveDist(-50)
        self.drive.moveArc(100, -90, speed=-100)
        self.drive.moveDist(-400, heading=-80, turn=False)

        self.config.state.setState(1)
