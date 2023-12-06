from threading import Thread


class ExampleRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(90)
        self.drive.moveDist(445, heading=90)
        self.drive.turnTo(45)

        self.config.state.setState(1)
