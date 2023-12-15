from threading import Thread


class RunBack(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(-90)
        self.drive.moveDist(-300, heading=-135, turn=False)
        self.drive.moveArc(-250, -50, speed=-200)
        self.drive.moveDist(-60, heading=-50)
        self.drive.moveDist(210, heading=-50)
        Thread(target=self.putArmDown).start()
        self.drive.turnTo(-156)
        self.drive.turnTo(-110)
        self.drive.drive.turn(-18)
        Thread(target=self.config.LMmotor.run_angle, args=[-1000, 200]).start()
        self.wait(750)
        # self.drive.spinTo(-80)
        self.drive.moveArc(-100, -80, speed=-200)
        self.drive.moveDist(-1000, speed=1000, heading=-80, up=False, down=False, turn=False)

        self.config.state.setState(1)
    
    def putArmDown(self):
        self.wait(330)
        self.config.LMmotor.run_angle(400, 410)

