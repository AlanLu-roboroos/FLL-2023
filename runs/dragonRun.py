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
        self.drive.moveDist(300, heading=0)
        self.drive.turnTo(30)
        self.drive.moveDist(-350, up=False, down=False)

        self.config.state.setState(1)
