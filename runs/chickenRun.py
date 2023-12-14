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
        self.wait(4000)
        self.drive.moveDist(-50, down=False)
        self.drive.moveArc(60, -60, speed=-400)
        self.drive.moveDist(-400, heading=-80, turn=False, up=False, down=False)

        self.config.state.setState(1)
