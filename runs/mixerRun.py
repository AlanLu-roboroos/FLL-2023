from threading import Thread


class MixerRun(Thread):
    def __init__(self, config):
        self.config = config
        self.drive = config.drive
        self.arm = config.LMmotor
        self.wait = config.timer.wait

    def run(self):
        self.drive.setHead(0)
        self.drive.moveDist(720, speed=1000, heading=15, turn=False)
        self.drive.turnTo(45)
        Thread(target=self.dropFigures).start()
        self.wait(500)
        self.drive.moveDist(-80, heading=45, speed=100)
        self.drive.turnTo(135)
        self.drive.moveDist(-100)
        self.drive.moveDist(30)
        self.drive.moveDist(-30)
        # self.drive.moveDist(30)
        self.drive.moveDist(520, heading=-170, turn=False)
        Thread(target=self.dropArm).start()
        self.drive.turnTo(40)
        self.drive.drive.drive(100, 0)
        self.wait(1000)
        self.drive.stop()
        # self.drive.stop()
        self.drive.moveDist(-35, heading=40)
        # Thread(target=self.drive.moveDist, args=[10]).start()
        Thread(target=self.arm.run_angle, args=[1000, 1200]).start()
        self.wait(1200)
        self.drive.turnTo(58)
        self.drive.moveDist(70)
        Thread(target=self.arm.run_angle, args=[-1000, 1200]).start()
        self.wait(800)
        Thread(target=self.raiseArm).start()
        self.drive.moveDist(-400, speed=1000, down=False, up=False)

        self.config.state.setState(1)

    def dropFigures(self):
        self.arm.run_angle(1000, 1600)

    def dropArm(self):
        self.arm.run_angle(-1000, 1600)
    
    def raiseArm(self):
        self.wait(2000)
        self.arm.run_angle(1000, 1600)