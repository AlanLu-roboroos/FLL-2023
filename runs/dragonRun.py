from threading import Thread
from pybricks.parameters import Stop
from modules.components import motor

class DragonRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.arm = config.RMmotor
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(0)

        Thread(target=self.arm.run_angle, args=[-90, 180]).start()
        self.drive.moveDist(320, heading=-3, turn=False)
        self.drive.turnTo(30)
        self.drive.moveDist(-350, up=False, down=False, heading=40, turn=False)

        self.config.state.setState(1)
